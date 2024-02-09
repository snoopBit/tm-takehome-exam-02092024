from dagster import op
import pandas as pd
from typing import List
from google.cloud import storage
from src.etl.settings import BANK_PROCESSED_DATA_LOCATION

@op(
    description="Save processed bank data to BigQuery"
)
def save_processed_data_to_bq(context, processed_data_df: pd.DataFrame) -> bool:

    return True


@op(
    description="Save raw data files to GCS to avoid duplicate processing"
)
def save_raw_data_files(context, raw_data_files: List[str], save_to_bq_done: bool):

    storage_client = storage.Client()
    processed_data_bucket = storage_client.get_bucket(BANK_PROCESSED_DATA_LOCATION)

    # TODO: Implement GCS upload of raw data files
    for data_file in raw_data_files:
        pass
    # END