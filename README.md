
# Drilling Optimization Suite (Streamlit Multipage App)

This platform is a modular, demo-ready prototype for an AI-powered Drilling Engineering and Operations SaaS. It combines data science, machine learning, and intuitive interfaces for intelligent decision support.

## Features

- **Multi-module Streamlit app with sidebar navigation**
- **Live parameter simulators, ML-powered predictions, and real-time insights**
- Built using open-source tools and pre-trained models

## Modules

1. **Recommender System** – Predict WOB, RPM, and Flow Rate
2. **UCS Predictor** – Estimate formation UCS using drilling parameters
3. **Bit Wear Predictor** – Predict bit wear % based on run hours and MSE
4. **Bit Type Selector** – Recommend PDC, Tricone, or Hybrid bits
5. **What-If Simulator** – Analyze impact of changing drilling inputs
6. **Real-Time Health Monitor** – Simulated feed for ROP/WOB/Flow alerts
7. **Offset Well Comparison** – Plot well log comparisons side-by-side
8. **Risk Warnings Generator** – NLP + AI-based risk detection from text

## How to Use

### Install Required Packages
```bash
pip install streamlit pandas scikit-learn joblib numpy plotly transformers torch
```

### Launch the Suite
```bash
streamlit run Home.py
```

### Navigate Modules
Use the **sidebar** to open each module from the `/pages/` folder.

## Deployment

- Upload to [https://github.com](https://github.com)
- Deploy on [https://share.streamlit.io](https://share.streamlit.io)

---

**Author**: Kunle  
**Built With**: Python, Streamlit, Scikit-learn, HuggingFace Transformers
