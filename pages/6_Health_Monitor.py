
import streamlit as st
import pandas as pd
import time
import numpy as np
import plotly.graph_objects as go

st.title("Real-Time Drilling Parameter Monitor")

mode = st.sidebar.radio("Simulation Mode", ["CSV Playback", "Random Live Feed"])
delay = st.sidebar.slider("Update Interval (seconds)", 1, 5, 2)

def alert_logic(row):
    alerts = []
    if row['WOB'] > 40000:
        alerts.append("High WOB")
    if row['ROP'] < 20:
        alerts.append("Low ROP")
    if abs(row['Flow Rate'] - 500) > 60:
        alerts.append("Flow deviation")
    return ", ".join(alerts)

placeholder = st.empty()

if mode == "CSV Playback":
    uploaded = st.sidebar.file_uploader("Upload CSV", type="csv")
    if uploaded:
        df = pd.read_csv(uploaded)
        df['Alert'] = df.apply(alert_logic, axis=1)

        for i in range(5, len(df), 5):
            with placeholder.container():
                subset = df.iloc[:i]
                st.line_chart(subset[['WOB', 'ROP', 'Flow Rate']])
                alerts = subset['Alert'].iloc[-5:]
                for alert in alerts:
                    if alert:
                        st.warning(alert)
            time.sleep(delay)
else:
    st.sidebar.info("Simulating data live...")
    wob, rop, flow = 20000, 100, 500
    for i in range(50):
        wob += np.random.randint(-3000, 3000)
        rop += np.random.randint(-10, 10)
        flow += np.random.randint(-30, 30)
        row = {"WOB": wob, "ROP": rop, "Flow Rate": flow}
        row["Alert"] = alert_logic(row)
        with placeholder.container():
            st.metric("WOB", f"{wob:.0f} lbs")
            st.metric("ROP", f"{rop:.0f} ft/hr")
            st.metric("Flow Rate", f"{flow:.0f} gpm")
            if row["Alert"]:
                st.error(row["Alert"])
        time.sleep(delay)
