import streamlit as st
import time
import random
import plotly.graph_objects as go

# ---- Page Config ----
st.set_page_config(page_title="TerraTrack", layout="wide")
image_path = "logo.png"
st.image(image_path, width=100)

# ---- Sidebar Controls ----
st.sidebar.header("⚙️ Device Controls")
led_status = st.sidebar.toggle("LED Light", value=True)
auto_refresh = st.sidebar.toggle("Auto Refresh", value=True)
refresh_interval = st.sidebar.slider("⏱ Refresh Interval (sec)", 2, 10, 5)

# ---- Simulated Sensor Data Generator ----
def generate_data():
    return {
        "energy_output": round(random.uniform(0.1, 1.5), 2),
        "battery_level": round(random.uniform(20, 100), 1),
        "humidity": round(random.uniform(50, 90), 1),
        "temperature": round(random.uniform(18, 28), 1),
        "soil_moisture": round(random.uniform(0.3, 0.9), 2),
        "co2_absorbed": round(random.uniform(0.02, 0.06), 3)
    }

# ---- UI Title ----
st.title("🌿 TerraTrack: Smart Terrarium Dashboard")
placeholder = st.empty()

def render_dashboard(data):
    with placeholder.container():
        st.subheader("📟 Live Sensor Readings")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("⚡ Energy Output", f"{data['energy_output']} W")
            st.metric("🔋 Battery Level", f"{data['battery_level']}%")
            st.metric("💡 LED Status", "On" if led_status else "Off")

        with col2:
            st.metric("🌡️ Temperature", f"{data['temperature']} °C")
            st.metric("💧 Humidity", f"{data['humidity']}%")
            st.metric("🌱 Soil Moisture", f"{data['soil_moisture'] * 100:.0f}%")

        with col3:
            st.metric("🌍 CO₂ Absorbed Today", f"{data['co2_absorbed']} kg")
            st.metric("🌳 Lifetime Offset", f"{round(data['co2_absorbed'] * 30, 2)} kg")
            st.caption("Equivalent to planting ~1 tree/month")

        st.divider()

        # ---- Energy Log Chart ----
        st.subheader("📊 Energy Usage Log")
        energy_data = [round(random.uniform(0.3, 1.5), 2) for _ in range(12)]
        time_labels = [f"{hour}:00" for hour in range(8, 20)]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=time_labels,
            y=energy_data,
            fill='tozeroy',
            line_shape='spline',
            line=dict(color='green', width=3),
            name="Power (W)"
        ))
        fig.update_layout(
            xaxis_title="Time of Day",
            yaxis_title="Energy Output (W)",
            template="plotly_white",
            height=300,
            margin=dict(l=20, r=20, t=30, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)

# ---- Real-Time Loop Simulation ----
if auto_refresh:
    while True:
        data = generate_data()
        render_dashboard(data)
        time.sleep(refresh_interval)
        placeholder.empty()
else:
    data = generate_data()
    render_dashboard(data)
