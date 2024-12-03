import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('diabetes_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit App
st.title("Diabetes Prediction App")
st.write("Enter the details below to predict the likelihood of diabetes:")

# Input fields
age = st.number_input("Age", min_value=0, step=1)
gender = st.selectbox("Gender (0: Female, 1: Male)", options=[0, 1])
height = st.number_input("Height (in cm)", min_value=0, step=1)
weight = st.number_input("Weight (in kg)", min_value=0, step=1)
blood_type = st.selectbox("Blood Type (1: A, 2: B, 3: AB, 4: O)", options=[1, 2, 3, 4])
bmi = st.number_input("BMI", min_value=0.0, step=0.1)
temperature = st.number_input("Body Temperature (°C)", min_value=0.0, step=0.1)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=0, step=1)
blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=0, step=1)
cholesterol = st.number_input("Cholesterol Level (mg/dL)", min_value=0, step=1)
smoking = st.selectbox("smoking (0: No, 1: Yes)", options=[0, 1])

# Button to predict
if st.button("Predict Diabetes"):
    # Collect input features
    features = np.array([[
        age, gender, height, weight, blood_type, bmi,
        temperature, heart_rate, blood_pressure, cholesterol,smoking
    ]])
    
    input_data_reshaped = features.reshape(1,-1)

    prediction = model.predict(input_data_reshaped)
    
    # Display result
    if prediction[0] == 1:
        st.error("The model predicts that the individual is at risk of diabetes.")
    else:
        st.success("The model predicts that the individual is not at risk of diabetes.")
