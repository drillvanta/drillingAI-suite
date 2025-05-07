import streamlit as st
import joblib
import pandas as pd

st.title("Drilling Parameter Recommender")

# Load model and encoders
model = joblib.load("models/recommender_model.pkl")
enc = joblib.load("models/recommender_encoders.pkl")

formation = st.selectbox("Formation", enc['Formation'].classes_)
bit_type = st.selectbox("Bit Type", enc['Bit Type'].classes_)
hole_size = st.selectbox("Hole Size", enc['Hole Size'].classes_)
section_type = st.selectbox("Section Type", enc['Section Type'].classes_)
wob = st.slider("WOB (lbs)", 1000, 50000, 10000)
rpm = st.slider("RPM", 30, 250, 100)
rop = st.slider("ROP (ft/hr)", 10, 200, 60)
di = st.slider("Drillability Index", 1.0, 10.0, 4.0)

input_df = pd.DataFrame({
    "Formation_enc": [enc['Formation'].transform([formation])[0]],
    "Bit Type_enc": [enc['Bit Type'].transform([bit_type])[0]],
    "Hole Size_enc": [enc['Hole Size'].transform([hole_size])[0]],
    "Section Type_enc": [enc['Section Type'].transform([section_type])[0]],
    "WOB": [wob],
    "RPM": [rpm],
    "ROP": [rop],
    "DI": [di]
})

prediction = model.predict(input_df)[0]
st.success(f"Recommended RPM: {prediction:.2f}")
