from dagster import op
from typing import List
import pandas as pd
import requests
from src.etl.settings import PREDICTION_API_URL


def _predict_customer_churn(customer_data):
    # TODO: Implement model API call
    url = f"{PREDICTION_API_URL}/<endpoint>"
    churn = True
    relevant_fields = {}
    requests.post(url, json=relevant_fields)
    # END
    return churn

@op
def predict_churn(context, raw_data_df: pd.DataFrame) -> pd.DataFrame:
    processed_data_df = raw_data_df.copy()

    # TODO: Integrate with model API service to add prediction
    processed_data_df["churn"] = raw_data_df.apply(_predict_customer_churn)
    # END

    return processed_data_df

