from dagster import op
from typing import List
import pandas as pd
import requests
import os
import sys
import pandas as pd

# Added these lines of code since the program wasn't able to properly find the settings.py file
# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from etl.settings import PREDICTION_API_URL

# from src.etl.settings import PREDICTION_API_URL

def _row_to_json(row: pd.DataFrame) -> dict:
    # Get the JSON format for all the columns except the index column
    cols = row.index[1:]
    json_payload = row[cols].to_dict()
    return json_payload

def _predict_customer_churn(customer_data):
    url = f"{PREDICTION_API_URL}/predict"
    relevant_fields = _row_to_json(customer_data)
    response = requests.post(url, json=relevant_fields)
    return response.json()['prediction_label']

@op
def predict_churn(raw_data_df: pd.DataFrame) -> pd.DataFrame:
    processed_rows = []
    for index, row in raw_data_df.iterrows():
        prediction_label = _predict_customer_churn(row)
        row['churn'] = prediction_label
        processed_rows.append(row)
    
    processed_data_df = pd.concat(processed_rows, axis=1).T
    return processed_data_df