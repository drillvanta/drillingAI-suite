
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

input_encoded = pd.DataFrame([{
    "Formation_enc": enc["Formation"].transform([formation])[0],
    "Bit_Type_enc": enc["Bit Type"].transform([bit_type])[0],
    "Hole_Size_enc": enc["Hole Size"].transform([hole_size])[0],
    "Section_Type_enc": enc["Section Type"].transform([section_type])[0]
}])

if st.button("Recommend Parameters"):
    prediction = model.predict(input_encoded)[0]
    st.success("Predicted Optimal Parameters:")
    st.metric("WOB (lbs)", round(prediction[0], 2))
    st.metric("RPM", round(prediction[1], 2))
    st.metric("Flow Rate (gpm)", round(prediction[2], 2))
