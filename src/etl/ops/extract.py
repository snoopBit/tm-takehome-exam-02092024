from typing import List
from dagster import op, Out
from google.cloud import storage
import pandas as pd

from src.etl.settings import BANK_RAW_DATA_LOCATION, BANK_PROCESSED_DATA_LOCATION


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

    # TODO: Get list of new raw data files based
    # on contents of raw data and processed data
    # buckets
    new_data_blobs = [] 
    new_data_filenames = []
    # END

    raw_data_df = pd.concat([
        pd.read_csv(data_file) for data_file in new_data_filenames
    ], ignore_index=True)

    return {
        "raw_data_df": raw_data_df,
        "raw_data_files": new_data_filenames
    }