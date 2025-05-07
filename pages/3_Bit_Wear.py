import streamlit as st
import joblib
import numpy as np

st.title("Bit Wear Predictor")

model = joblib.load("models/bit_wear_model.pkl")
enc = joblib.load("models/bit_wear_encoders.pkl")  # Placeholder in case future encoders added

wob = st.slider("WOB (lbs)", 1000, 50000, 15000)
rpm = st.slider("RPM", 30, 250, 120)
rop = st.slider("ROP (ft/hr)", 10, 250, 70)
di = st.slider("Drillability Index", 1.0, 10.0, 5.0)

features = np.array([[wob, rpm, rop, di]])
prediction = model.predict(features)[0]
st.success(f"Predicted Bit Wear: {prediction:.2f} %")
