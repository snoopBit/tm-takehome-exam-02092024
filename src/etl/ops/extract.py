from typing import List
from dagster import op, Out
from google.cloud import storage
import pandas as pd
import os
import sys

# Added service account credentials for accessing the Google Cloud services
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'servicekey_googlecloud.json'

# Added these lines of code since the program wasn't able to properly find the settings.py file
# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from etl.settings import BANK_RAW_DATA_LOCATION, BANK_PROCESSED_DATA_LOCATION

@op(
    description="Extract new raw bank data",
    out={
        "raw_data_df": Out(),
        "raw_data_files": Out(),
    }
)
def get_latest_bank_raw_data(context) -> pd.DataFrame:
    context.log.info(f"Extracting raw data from {BANK_RAW_DATA_LOCATION}")

    storage_client = storage.Client()
    raw_data_bucket = storage_client.get_bucket(BANK_RAW_DATA_LOCATION)
    processed_data_bucket = storage_client.get_bucket(BANK_PROCESSED_DATA_LOCATION)

    # Get list of all raw data files
    raw_data_files = [blob.name for blob in raw_data_bucket.list_blobs()]

    # Get list of all processed data files
    processed_data_files = [blob.name for blob in processed_data_bucket.list_blobs()]

    # Filter out the files that are not present in the processed data bucket
    new_data_filenames = [file for file in raw_data_files if file not in processed_data_files]

    raw_data_df = pd.concat([
        pd.read_csv(f'gs://{BANK_RAW_DATA_LOCATION}/{data_file}') for data_file in new_data_filenames
    ], ignore_index=True)

    return {
        "raw_data_df": raw_data_df,
        "raw_data_files": new_data_filenames
    }
