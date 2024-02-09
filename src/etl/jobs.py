from dagster import job
from src.etl.ops import extract, transform, load

@job(description="ETL job for extracting raw data from bank, predicting customer churn, and saving processed data.")
def bank_etl_job():

    raw_data_df, raw_data_files = extract.get_bank_raw_data()
    processed_data_df = transform.predict_churn(raw_data_df)
    save_to_bq_done = load.save_processed_data_to_bq(processed_data_df)
    load.save_raw_data_files(raw_data_files, save_to_bq_done)

