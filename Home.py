
import streamlit as st

st.set_page_config(page_title="Drilling Optimization Suite", layout="wide")

st.title("Modular Drilling Optimization Suite")
st.markdown("""
This unified platform brings together multiple intelligent modules designed to optimize drilling planning,
execution, and post-job analysis. Each module operates independently but is integrated into a cohesive suite.

### Available Modules:
- **Recommender System**: Predict optimal WOB, RPM, and Flow Rate.
- **UCS Predictor**: Estimate formation UCS from operational data.
- **Bit Wear Predictor**: Forecast bit wear based on usage and MSE.
- **Bit Selector**: Recommend bit types based on geology and mechanics.
- **What-If Simulator**: Visualize how changes in drilling inputs impact results.
- **Real-Time Health Monitor**: Simulate and monitor drilling parameters for anomalies.
- **Offset Well Comparison**: Compare performance across offset wells.
- **Risk Warnings Generator**: Detect operational risks from reports using AI and NLP.

Use the sidebar to navigate to each module.
""")

st.info("This is a demo-ready Streamlit multipage app. All modules are included for testing and presentation.")
