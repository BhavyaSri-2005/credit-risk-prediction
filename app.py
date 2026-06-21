import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/risk_model.pkl")

st.title("Credit Risk Assessment System")

st.subheader("Loan Applicant Details")

income = st.number_input("Annual Income", 100000, 5000000)
loan_amount = st.number_input("Loan Amount", 10000, 2000000)
bureau_score = st.slider("Credit Score", 300, 900, 650)
total_debt = st.number_input("Total Debt", 0, 2000000)
late_payments = st.slider("Late Payments", 0, 20, 0)

if st.button("Predict Risk"):

    debt_income_ratio = total_debt / (income + 1)

    sample = pd.DataFrame([{
        "annual_income": income,
        "loan_amount": loan_amount,
        "bureau_score": bureau_score,
        "total_debt": total_debt,
        "late_payments": late_payments,
        "debt_income_ratio": debt_income_ratio
    }])

    st.success("Prediction completed")
