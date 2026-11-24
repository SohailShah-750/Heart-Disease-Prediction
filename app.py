
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page configuration
st.set_page_config(
    page_title="Heart Disease AI",
    page_icon="❤️",
    layout="wide"
)

# Load trained model
model = joblib.load("heart_disease_svm.pkl")

# Application title
st.title("❤️ Heart Disease Prediction")
st.write(
    "AI-powered heart disease risk prediction application."
)

st.info(
    "Enter the patient's medical information below."
)

st.warning(
    "This application is for educational purposes only. "
    "It is not a medical diagnosis."
)

)
