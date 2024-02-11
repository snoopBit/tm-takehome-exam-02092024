from dagster import op
import pandas as pd
from typing import List
from google.cloud import storage, bigquery
import os
import sys
import time

# Added these lines of code since the program wasn't able to properly find the settings.py file
# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# from src.etl.settings import BANK_RAW_DATA_LOCATION, BANK_PROCESSED_DATA_LOCATION, BANK_PROCESSED_DATA_BQ_LOCATION

from etl.settings import BANK_RAW_DATA_LOCATION, BANK_PROCESSED_DATA_LOCATION, BANK_PROCESSED_DATA_BQ_LOCATION

# Added service account credentials for accessing the Google Cloud services
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'servicekey_googlecloud.json'

@op(
    description="Save processed bank data to BigQuery"
)
# def save_processed_data_to_bq(context, processed_data_df: pd.DataFrame) -> bool:
def save_processed_data_to_bq(processed_data_df: pd.DataFrame) -> bool:
    # Manually added the schema to not have wrongly assigned data types
    schema = [
        bigquery.SchemaField("CreditScore", "INTEGER"),
        bigquery.SchemaField("Age", "INTEGER"),
        bigquery.SchemaField("Tenure", "INTEGER"),
        bigquery.SchemaField("Balance", "FLOAT"),
        bigquery.SchemaField("NumOfProducts", "INTEGER"),
        bigquery.SchemaField("HasCreditCard", "INTEGER"),
        bigquery.SchemaField("IsActiveMember", "INTEGER"),
        bigquery.SchemaField("EstimatedSalary", "FLOAT"),
        bigquery.SchemaField("Branch_Makati City", "INTEGER"),
        bigquery.SchemaField("Branch_Manila", "INTEGER"),
        bigquery.SchemaField("Branch_Quezon City", "INTEGER"),
        bigquery.SchemaField("Gender_Female", "INTEGER"),
        bigquery.SchemaField("Gender_Male", "INTEGER"),
        bigquery.SchemaField("churn", "INTEGER")
    ]

    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(
        schema=schema,
        source_format=bigquery.SourceFormat.CSV
    )

    job = client.load_table_from_dataframe(processed_data_df, BANK_PROCESSED_DATA_BQ_LOCATION, job_config=job_config)

    # Added this part to keep track of the job status (for long-running ones)
    while job.state != 'DONE':
        time.sleep(2)
        job.reload()
        print(job.state)

    print(job.result())

    return True

@op(
    description="Save raw data files to GCS to avoid duplicate processing"
)
def save_raw_data_files(context, raw_data_files: List[str], save_to_bq_done: bool):

    storage_client = storage.Client()
    processed_data_bucket = storage_client.get_bucket(BANK_PROCESSED_DATA_LOCATION)

    for data_file in raw_data_files:
        raw_data_df = pd.read_csv(f'gs://{BANK_RAW_DATA_LOCATION}/{data_file}', index_col=0)
        processed_data_bucket.blob(data_file).upload_from_string(raw_data_df.to_csv(), 'text/csv')