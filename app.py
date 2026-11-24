import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load('heart_disease_svm.pkl')

# Page configuration
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

# App title
st.title("❤️ Heart Disease Prediction System")

st.write(
    "An educational Machine Learning application "
    "using Support Vector Machine (SVM)."
)
