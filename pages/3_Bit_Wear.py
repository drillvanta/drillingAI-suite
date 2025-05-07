
import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.title("Bit Wear Predictor")

model = joblib.load("models/bit_wear_model.pkl")
enc = joblib.load("models/bit_wear_encoders.pkl")

bit_type = st.selectbox("Bit Type", enc['Bit_Type'].classes_)
formation = st.selectbox("Formation", enc['Formation'].classes_)
wob = st.slider("WOB (lbs)", 1000, 50000, 25000)
rpm = st.slider("RPM", 50, 250, 120)
rop = st.slider("ROP (ft/hr)", 10, 200, 80)
bit_diameter = st.slider("Bit Diameter (in)", 6.0, 17.5, 8.5)
di = st.slider("Drillability Index", 1, 10, 5)
hours_run = st.slider("Bit Run Time (hours)", 1, 300, 50)

area = (np.pi / 4) * bit_diameter**2
mse = wob / area + 1.1 * (rpm / rop)

input_df = pd.DataFrame([{
    "Bit_Type_enc": enc["Bit_Type"].transform([bit_type])[0],
    "Formation_enc": enc["Formation"].transform([formation])[0],
    "Hours_Run": hours_run,
    "WOB": wob, "RPM": rpm, "ROP": rop,
    "MSE": mse, "DI": di
}])

if st.button("Predict Bit Wear"):
    wear = model.predict(input_df)[0]
    st.metric("Predicted Bit Wear (%)", round(wear, 2))
