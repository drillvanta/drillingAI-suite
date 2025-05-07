
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("What-If Simulator")

rec_model = joblib.load("models/recommender_model.pkl")
rec_enc = joblib.load("models/recommender_encoders.pkl")
wear_model = joblib.load("models/bit_wear_model.pkl")
wear_enc = joblib.load("models/bit_wear_encoders.pkl")
ucs_model = joblib.load("models/ucs_predictor_model.pkl")

bit_type = st.selectbox("Bit Type", wear_enc['Bit_Type'].classes_)
formation = st.selectbox("Formation", wear_enc['Formation'].classes_)
bit_diameter = st.slider("Bit Diameter (in)", 6.0, 17.5, 8.5)
wob = st.slider("WOB (lbs)", 1000, 50000, 25000)
rpm = st.slider("RPM", 30, 250, 120)
rop = st.slider("ROP (ft/hr)", 10, 200, 60)
di = st.slider("Drillability Index", 1, 10, 5)

wob_adj = st.slider("WOB Adjustment (%)", -30, 30, 0)
rpm_adj = st.slider("RPM Adjustment (%)", -30, 30, 0)
rop_adj = st.slider("ROP Adjustment (%)", -30, 30, 0)

def calc_mse(wob, rpm, rop, bit_diameter):
    area = (np.pi / 4) * bit_diameter**2
    return wob / area + 1.1 * (rpm / rop)

if st.button("Run What-If Analysis"):
    mse_orig = calc_mse(wob, rpm, rop, bit_diameter)

    wear_input = pd.DataFrame([{
        "Bit_Type_enc": wear_enc["Bit_Type"].transform([bit_type])[0],
        "Formation_enc": wear_enc["Formation"].transform([formation])[0],
        "Hours_Run": 40, "WOB": wob, "RPM": rpm, "ROP": rop,
        "MSE": mse_orig, "DI": di
    }])
    ucs_input = pd.DataFrame([{
        "ROP": rop, "RPM": rpm, "WOB": wob,
        "Bit_Diameter": bit_diameter, "MSE": mse_orig
    }])
    wear_orig = round(wear_model.predict(wear_input)[0], 2)
    ucs_orig = round(ucs_model.predict(ucs_input)[0], 2)

    rec_input = pd.DataFrame([{
        "Formation_enc": rec_enc["Formation"].transform([formation])[0],
        "Bit_Type_enc": rec_enc["Bit Type"].transform([bit_type])[0],
        "Hole_Size_enc": rec_enc["Hole Size"].transform(["8.5"])[0],
        "Section_Type_enc": rec_enc["Section Type"].transform(["Vertical"])[0]
    }])
    rec_params = rec_model.predict(rec_input)[0]

    wob_new = wob * (1 + wob_adj / 100)
    rpm_new = rpm * (1 + rpm_adj / 100)
    rop_new = rop * (1 + rop_adj / 100)
    mse_new = calc_mse(wob_new, rpm_new, rop_new, bit_diameter)

    wear_input.at[0, "WOB"] = wob_new
    wear_input.at[0, "RPM"] = rpm_new
    wear_input.at[0, "ROP"] = rop_new
    wear_input.at[0, "MSE"] = mse_new

    ucs_input.at[0, "WOB"] = wob_new
    ucs_input.at[0, "RPM"] = rpm_new
    ucs_input.at[0, "ROP"] = rop_new
    ucs_input.at[0, "MSE"] = mse_new

    wear_new = round(wear_model.predict(wear_input)[0], 2)
    ucs_new = round(ucs_model.predict(ucs_input)[0], 2)

    st.subheader("What-If Results")
    st.table(pd.DataFrame({
        "Metric": ["Bit Wear (%)", "UCS (psi)", "WOB (pred)", "RPM (pred)", "Flow Rate (pred)"],
        "Original": [wear_orig, ucs_orig, round(rec_params[0], 1), round(rec_params[1], 1), round(rec_params[2], 1)],
        "What-If": [wear_new, ucs_new, "-", "-", "-"]
    }))
