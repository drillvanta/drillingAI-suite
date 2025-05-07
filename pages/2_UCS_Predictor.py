import streamlit as st
import joblib
import numpy as np

st.title("UCS Estimator")

model = joblib.load("models/ucs_predictor_model.pkl")

rop = st.slider("ROP (ft/hr)", 10, 250, 100)
rpm = st.slider("RPM", 50, 200, 120)
di = st.slider("Drillability Index", 1.0, 10.0, 4.0)

features = np.array([[rop, rpm, di]])
prediction = model.predict(features)[0]
st.success(f"Predicted UCS: {prediction:.2f} psi")
