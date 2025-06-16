import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Title
st.title("Loan Prediction App")

# Input Fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term", min_value=0)
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

# Predict button
if st.button("Predict"):
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Married': [married],
        'Dependents': [dependents],
        'Education': [education],
        'Self_Employed': [self_employed],
        'ApplicantIncome': [applicant_income],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_term],
        'Credit_History': [credit_history],
        'Property_Area': [property_area]
    })

    # Encode if needed (same logic as used during training)
    for col in input_data.select_dtypes(include='object').columns:
        input_data[col] = input_data[col].astype('category').cat.codes

    result = model.predict(input_data)[0]
    st.success(f"Loan Status: {'Approved ✅' if result == 1 else 'Rejected ❌'}")
