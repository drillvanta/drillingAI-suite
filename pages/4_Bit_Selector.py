import streamlit as st
import joblib
import numpy as np

st.title("Bit Type Selector")

model = joblib.load("models/bit_selector_model.pkl")
enc = joblib.load("models/bit_selector_encoders.pkl")

formation = st.selectbox("Formation", enc['Formation'].classes_)
di = st.slider("Drillability Index", 1.0, 10.0, 5.0)

formation_enc = enc['Formation'].transform([formation])[0]
features = np.array([[formation_enc, di]])
bit_type_idx = model.predict(features)[0]
bit_type = enc['Bit Type'].inverse_transform([bit_type_idx])[0]

st.success(f"Recommended Bit Type: {bit_type}")
