import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model safely (bypass InputLayer config issues)
model = load_model("diabetes_model.h5", compile=False)

st.title("Diabetes Prediction App 🩺")
st.write("Enter patient details:")

# User Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=25)
gender = st.selectbox("Gender", ["Female", "Male"])
bmi = st.number_input("BMI", value=25.0)
glucose = st.number_input("Blood Glucose Level", value=100)
hypertension = st.selectbox("Hypertension", ["No", "Yes"])
smoking = st.selectbox("Smoking History", ["Never", "Former", "Current", "Unknown"])
medical_report = st.number_input("Medical Report Code (0-9)", min_value=0, max_value=9, value=5)

# Encode inputs (same as training)
gender = 1 if gender == "Male" else 0
hypertension = 1 if hypertension == "Yes" else 0

smoking_map = {"Never": 0, "Former": 1, "Current": 2, "Unknown": 3}
smoking = smoking_map[smoking]

# Prediction button
if st.button("Predict"):
    # Prepare input for model
    input_data = np.array([[age, gender, bmi, glucose, hypertension, smoking, medical_report]])

    # Make prediction
    prediction = model.predict(input_data)

    # Show result
    if prediction[0][0] > 0.5:
        st.error("⚠️ Diabetic")
    else:
        st.success("✅ Not Diabetic")