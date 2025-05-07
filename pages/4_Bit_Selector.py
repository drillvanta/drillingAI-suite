
import streamlit as st
import joblib
import pandas as pd

st.title("Bit Type Recommender")

model = joblib.load("models/bit_selector_model.pkl")
enc = joblib.load("models/bit_selector_encoders.pkl")

formation = st.selectbox("Formation", enc['Formation'].classes_)
section = st.selectbox("Section Type", enc['Section'].classes_)
ucs = st.slider("UCS (psi)", 3000, 25000, 10000)
di = st.slider("Drillability Index (1–10)", 1, 10, 5)

form_enc = enc['Formation'].transform([formation])[0]
sect_enc = enc['Section'].transform([section])[0]

input_df = pd.DataFrame([{
    "Formation_enc": form_enc,
    "UCS": ucs,
    "DI": di,
    "Section_enc": sect_enc
}])

if st.button("Recommend Bit"):
    bit = model.predict(input_df)[0]
    st.success(f"Recommended Bit Type: **{bit}**")
