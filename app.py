import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_processing import detect_faults

st.set_page_config(layout="wide", page_title="SolarGuardian Real-Time")

st.title("🔆 SolarGuardian - Real-Time Monitoring Dashboard")

# Simulate loading real-time data
data = pd.read_csv("data/realtime_data.csv")

st.subheader("🔍 Real-Time Metrics")
st.dataframe(data.tail(10))

# Plot
fig = px.line(data, x="timestamp", y="energy_generated", title="Real-time Energy Output")
st.plotly_chart(fig, use_container_width=True)

# Fault Detection
st.subheader("⚠️ Detected Faults")
faults = detect_faults(data)
st.write(faults)

