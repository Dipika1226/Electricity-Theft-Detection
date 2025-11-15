from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)
CORS(app)

# Load model
model = joblib.load("../model/electricity_theft_model_v2.pkl")

@app.route("/")
def home():
    return jsonify({"message": "Electricity Theft Detection API Running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["data"]  # list of 1034 daily readings

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Handle missing values
        df.fillna(0, inplace=True)

        # Make prediction
        prediction = model.predict(df)[0]

        return jsonify({"prediction": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
