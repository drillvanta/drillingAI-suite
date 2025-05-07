
import streamlit as st
import pandas as pd
from transformers import pipeline

st.title("Risk Warnings Generator")

# Risk categories
RISK_LABELS = ["Stuck Pipe", "High Torque", "Vibration", "Lost Circulation", "Packoff"]

# Rules
RISK_RULES = {
    "Stuck Pipe": {"keywords": ["stuck", "pipe stuck", "unable to move"], "severity": "High", "mitigation": "Backoff, circulate, jar"},
    "High Torque": {"keywords": ["torque", "torque limit"], "severity": "Medium", "mitigation": "Adjust WOB/RPM, monitor torque"},
    "Vibration": {"keywords": ["vibration", "shock sub"], "severity": "Medium", "mitigation": "Optimize RPM and WOB"},
    "Lost Circulation": {"keywords": ["lost returns", "no returns"], "severity": "High", "mitigation": "Apply LCM, reduce flow"},
    "Packoff": {"keywords": ["packoff", "restricted flow"], "severity": "High", "mitigation": "Circulate, reduce flow, monitor cuttings"}
}

mode = st.radio("Detection Mode", ["Rule-Based", "AI (Zero-Shot)"])
text_input = st.text_area("Paste report or incident note:", height=300)

if st.button("Analyze"):
    lowered = text_input.lower()
    results = []

    if mode == "Rule-Based":
        for risk, rule in RISK_RULES.items():
            detected = any(kw in lowered for kw in rule["keywords"])
            results.append({
                "Risk Type": risk,
                "Detected": "Yes" if detected else "No",
                "Severity": rule["severity"] if detected else "-",
                "Mitigation": rule["mitigation"] if detected else "-"
            })
    else:
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        prediction = classifier(text_input, RISK_LABELS)
        for label, score in zip(prediction["labels"], prediction["scores"]):
            results.append({
                "Risk Type": label,
                "Detected": "Yes" if score > 0.5 else "No",
                "Severity": RISK_RULES[label]["severity"] if score > 0.5 else "-",
                "Mitigation": RISK_RULES[label]["mitigation"] if score > 0.5 else "-",
                "Confidence": f"{score:.2f}"
            })

    st.subheader("Detected Risks Summary")
    st.dataframe(pd.DataFrame(results))
