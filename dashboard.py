import streamlit as st
import pandas as pd
import psutil
import joblib
from datetime import datetime

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI System Monitoring",
    page_icon="🖥️",
    layout="wide"
)

# -----------------------------
# Load trained AI model
# -----------------------------
model = joblib.load("anomaly_model.pkl")

# -----------------------------
# Store live data
# -----------------------------
if "live_data" not in st.session_state:
    st.session_state.live_data = []

# -----------------------------
# Collect current system data
# -----------------------------
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

timestamp = datetime.now()

# -----------------------------
# AI prediction
# -----------------------------
current_data = pd.DataFrame(
    [[cpu, ram, disk]],
    columns=["cpu", "ram", "disk"]
)

prediction = model.predict(current_data)[0]

if prediction == -1:
    status = "ANOMALY"
else:
    status = "NORMAL"

# -----------------------------
# Add current record
# -----------------------------
st.session_state.live_data.append({
    "timestamp": timestamp,
    "cpu": cpu,
    "ram": ram,
    "disk": disk,
    "status": status
})

# Keep last 100 records
st.session_state.live_data = st.session_state.live_data[-100:]

live_df = pd.DataFrame(st.session_state.live_data)

# -----------------------------
# Dashboard
# -----------------------------
st.title("🖥️ AI-Based Real-Time System Monitoring")

st.write(
    "Monitor CPU, RAM and disk usage and detect unusual "
    "system behavior using machine learning."
)

# Current metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPU Usage", f"{cpu:.1f}%")

with col2:
    st.metric("RAM Usage", f"{ram:.1f}%")

with col3:
    st.metric("Disk Usage", f"{disk:.1f}%")

# Current AI status
st.subheader("🤖 AI System Status")

if status == "ANOMALY":
    st.error("⚠️ Anomalous system behavior detected!")
else:
    st.success("✅ System performance is normal.")

# -----------------------------
# Live chart
# -----------------------------
st.subheader("📊 Real-Time System Performance")

if not live_df.empty:
    chart_df = live_df.set_index("timestamp")[["cpu", "ram", "disk"]]
    st.line_chart(chart_df)

# -----------------------------
# Recent records
# -----------------------------
st.subheader("📋 Recent Monitoring Records")

if not live_df.empty:
    st.dataframe(
        live_df.tail(10),
        use_container_width=True
    )

# -----------------------------
# Auto refresh
# -----------------------------
st.caption("Dashboard refreshes automatically every 5 seconds.")

st.markdown(
    """
    <meta http-equiv="refresh" content="5">
    """,
    unsafe_allow_html=True
)
# -----------------------------
# Anomaly records
# -----------------------------
st.subheader("🚨 Detected Anomalies")

anomaly_df = live_df[live_df["status"] == "ANOMALY"]

if not anomaly_df.empty:
    st.warning(
        f"{len(anomaly_df)} anomalous readings detected "
        "during this monitoring session."
    )

    st.dataframe(
        anomaly_df,
        use_container_width=True
    )
else:
    st.success("No anomalies detected in the current session.")