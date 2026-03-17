import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

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

# Encode inputs
gender = 1 if gender == "Male" else 0
hypertension = 1 if hypertension == "Yes" else 0
smoking_map = {"Never": 0, "Former": 1, "Current": 2, "Unknown": 3}
smoking = smoking_map[smoking]

# Prediction button
if st.button("Predict"):
    input_data = np.array([[age, gender, bmi, glucose, hypertension, smoking, medical_report]])
    prediction = model.predict(input_data)
    
    if prediction[0] > 0.5:
        st.error("⚠️ Diabetic")
    else:
        st.success("✅ Not Diabetic")