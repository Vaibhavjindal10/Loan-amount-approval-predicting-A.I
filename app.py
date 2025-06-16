import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Loan Prediction", layout="centered")

# Injecting custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f7;
    }
    h1 {
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        font-size: 18px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("model.pkl")

st.title("🏦 Loan Approval Predictor")
st.write("Fill in the details to know if your loan will be approved.")

with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])

    with col2:
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        applicant_income = st.number_input("Applicant Income", min_value=0)
        coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
        loan_amount = st.number_input("Loan Amount", min_value=0)
        loan_term = st.number_input("Loan Term", min_value=0)
        credit_history = st.selectbox("Credit History", [1.0, 0.0])
        property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

    submitted = st.form_submit_button("🚀 Predict")

if submitted:
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Married': [married],
        'Dependents': [dependents],
        'Education': [education],
        'Self_Employed': [self_employed],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount],import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Loan Prediction", layout="centered")

# Injecting custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f7;
    }
    h1 {
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        font-size: 18px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("model.pkl")

st.title("🏦 Loan Approval Predictor")
st.write("Fill in the details to know if your loan will be approved.")

with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])

    with col2:
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        applicant_income = st.number_input("Applicant Income", min_value=0)
        coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
        loan_amount = st.number_input("Loan Amount", min_value=0)
        loan_term = st.number_input("Loan Term", min_value=0)
        credit_history = st.selectbox("Credit History", [1.0, 0.0])
        property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

    submitted = st.form_submit_button("🚀 Predict")

if submitted:
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Married': [married],
        'Dependents': [dependents],
        'Education': [education],
        'Self_Employed': [self_employed],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_term],
        'Credit_History': [credit_history],
        'Property_Area': [property_area]
    })

    # Encode object columns
    for col in input_data.select_dtypes(include='object').columns:
        input_data[col] = input_data[col].astype('category').cat.codes

    result = model.predict(input_data)[0]
    if result == 1:
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Rejected.")

        'Loan_Amount_Term': [loan_term],
        'Credit_History': [credit_history],
        'Property_Area': [property_area]
    })

    # Encode object columns
    for col in input_data.select_dtypes(include='object').columns:
        input_data[col] = input_data[col].astype('category').cat.codes

    result = model.predict(input_data)[0]
    if result == 1:
        st.success("✅ Loan Approved!")
    else:
        st.error("❌ Loan Rejected.")
