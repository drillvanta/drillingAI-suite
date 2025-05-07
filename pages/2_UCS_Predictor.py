
import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.title("UCS Estimator")

model = joblib.load("models/ucs_predictor_model.pkl")

rop = st.slider("ROP (ft/hr)", 10, 250, 100)
rpm = st.slider("RPM", 50, 200, 120)
wob = st.slider("WOB (lbs)", 1000, 50000, 25000)
bit_diameter = st.slider("Bit Diameter (in)", 6.0, 17.5, 8.5)

area = (np.pi / 4) * bit_diameter**2
mse = wob / area + 1.1 * (rpm / rop)

input_df = pd.DataFrame([{
    "ROP": rop,
    "RPM": rpm,
    "WOB": wob,
    "Bit_Diameter": bit_diameter,
    "MSE": mse
}])

if st.button("Estimate UCS"):
    ucs = model.predict(input_df)[0]
    st.metric("Estimated UCS (psi)", round(ucs, 2))
