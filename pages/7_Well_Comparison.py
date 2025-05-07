
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Offset Well Comparison Tool")

file_a = st.file_uploader("Upload Well A CSV", type="csv", key="a")
file_b = st.file_uploader("Upload Well B CSV", type="csv", key="b")
compare_param = st.selectbox("Parameter to Compare", ["ROP", "WOB", "RPM"])

if file_a and file_b:
    df_a = pd.read_csv(file_a)
    df_b = pd.read_csv(file_b)

    if "Depth" in df_a.columns and compare_param in df_a.columns and compare_param in df_b.columns:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_a["Depth"], y=df_a[compare_param],
                                 mode='lines', name='Well A', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=df_b["Depth"], y=df_b[compare_param],
                                 mode='lines', name='Well B', line=dict(color='red')))
        fig.update_layout(title=f"{compare_param} vs Depth", xaxis_title="Depth (ft)",
                          yaxis_title=compare_param, legend_title="Well")

        st.plotly_chart(fig, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Avg Well A", round(df_a[compare_param].mean(), 2))
        with col2:
            st.metric("Avg Well B", round(df_b[compare_param].mean(), 2))
    else:
        st.error("Both CSVs must contain 'Depth' and the selected parameter.")
else:
    st.info("Please upload two well CSV files to begin comparison.")
