
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Heart Disease AI",
    page_icon="❤️",
    layout="wide"
)

model = joblib.load("heart_disease_svm.pkl")

st.title("❤️ Heart Disease Prediction")
st.write("AI-powered Heart Health Assessment")

st.info("Enter patient medical information below.")

with st.form("patient_form"):

    st.subheader("Patient Information")

    col1, col2 = st.columns(2)

    with col1:
        Age = st.number_input("Age", 1, 120, 45)

        Sex = st.selectbox(
            "Sex", ["M", "F"]
        )

        ChestPainType = st.selectbox(
            "Chest Pain Type",
            ["TA", "ATA", "NAP", "ASY"]
        )

        RestingBP = st.number_input(
            "Resting Blood Pressure", 0, 300, 120
        )

        Cholesterol = st.number_input(
            "Cholesterol", 0, 700, 200
        )

        FastingBS = st.selectbox(
            "Fasting Blood Sugar",
            [0, 1]
        )

    with col2:
        RestingECG = st.selectbox(
            "Resting ECG",
            ["Normal", "ST", "LVH"]
        )

        MaxHR = st.number_input(
            "Maximum Heart Rate", 0, 250, 150
        )

        ExerciseAngina = st.selectbox(
            "Exercise Angina", ["N", "Y"]
        )

        Oldpeak = st.number_input(
            "Oldpeak", 0.0, 10.0, 0.0
        )

        ST_Slope = st.selectbox(
            "ST Slope", ["Up", "Flat", "Down"]
        )

    submit = st.form_submit_button(
        "Predict Heart Disease",
        use_container_width=True
    )

    if submit:
       
if submit:

    # Create input DataFrame
    input_data = pd.DataFrame([{
        "Age": Age,
        "Sex": Sex,
        "ChestPainType": ChestPainType,
        "RestingBP": RestingBP,
        "Cholesterol": Cholesterol,
        "FastingBS": FastingBS,
        "RestingECG": RestingECG,
        "MaxHR": MaxHR,
        "ExerciseAngina": ExerciseAngina,
        "Oldpeak": Oldpeak,
        "ST_Slope": ST_Slope
    }])

  
    # Prediction result
    prediction = model.predict(input_data)[0]

    st.divider()
    st.subheader("Heart Health Assessment")

    if prediction == 1:

        st.error(
            "Heart Disease Prediction: Positive"
        )

        st.write(
            "The model predicts a positive heart disease result."
        )

    else:

        st.success(
            "Heart Disease Prediction: Negative"
        )

        st.write(
            "The model predicts a negative heart disease result."
        )

    st.warning(
        "This AI application is for educational purposes only. "
        "It cannot diagnose or rule out heart disease. "
        "Consult a qualified healthcare professional."
    )

