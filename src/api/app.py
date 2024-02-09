import joblib
import pandas as pd
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
model = joblib.load('dt_tuned.pkl')

@app.route("/predict", methods=["POST"])
def main():
    input_data = read_data(request)
    pred_label = predict(model, input_data)

    response = {'prediction_label': str(pred_label)}
    return jsonify(response)

def read_data(request) -> pd.DataFrame:
    data = request.get_json()

    # Check if the request wasn't properly parsed (str instead of dict object)
    if not isinstance(data, dict):
        data = json.loads(data)

    # Properly format the column types
    type_mapping = {'CreditScore': 'int64', 'Age': 'int64', 'Tenure': 'int64', 'Balance': 'float64',
                    'NumOfProducts': 'int64', 'HasCreditCard': 'int64', 'IsActiveMember': 'int64', 'EstimatedSalary': 'float64',
                    'Branch_Makati City': 'uint8', 'Branch_Manila': 'uint8', 'Branch_Quezon City': 'uint8', 'Gender_Female': 'uint8',
                    'Gender_Male': 'uint8'}
    
    col_list = [key for key, val in type_mapping.items()]

    val_list = [data[x] for x in col_list]

    input_variables = pd.DataFrame([val_list],
                                   columns=col_list)
      
    # Correct the dtype parameter for each column
    input_variables = input_variables.astype(type_mapping)
    
    return input_variables


def predict(model, input_data: pd.DataFrame) -> int:
    pred_label = model.predict(input_data)[0]

    print(f"Prediction label: {pred_label}")
    return pred_label

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1616)