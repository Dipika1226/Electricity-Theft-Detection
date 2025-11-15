import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("../model/electricity_theft_model_v2.pkl")

st.title("⚡ Electricity Theft Detection – Streamlit App")
st.write("Upload a single customer’s consumption row (1034 daily values) as a CSV file.")

uploaded_file = st.file_uploader("Upload CSV with 1034 columns", type=["csv"])

if uploaded_file is not None:
    try:
        # Read the uploaded CSV
        df = pd.read_csv(uploaded_file)

        st.write("📄 Uploaded Data:")
        st.dataframe(df)

        # Check input shape
        if df.shape[1] != 1034:
            st.error(f"❌ Expected 1034 columns, but got {df.shape[1]}")
        else:
            # Predict
            pred = model.predict(df)[0]

            if pred == 1:
                st.error("⚠️ Theft Detected!")
            else:
                st.success("✔️ Normal Consumption")

    except Exception as e:
        st.error(f"Error: {e}")
