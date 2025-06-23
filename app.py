import streamlit as st
import time
import random
import plotly.graph_objects as go

image_path = "logo.png"
st.image(image_path, width = 100)
#st.set_page_config(page_title="TerraTrack", layout="wide")
# ---- Sidebar Controls ----
st.sidebar.title("⚙️ Device Controls")
led_status = st.sidebar.toggle("LED Light", value=True)
auto_refresh = st.sidebar.toggle("Auto Refresh", value=True)
refresh_interval = st.sidebar.slider("Data Refresh Interval (sec)", 2, 10, 5)

# ---- Simulated Sensor Data ----
def generate_data():
    return {
        "energy_output": round(random.uniform(0.1, 1.5), 2),  # watts
        "battery_level": round(random.uniform(20, 100), 1),  # %
        "humidity": round(random.uniform(50, 90), 1),        # %
        "temperature": round(random.uniform(18, 28), 1),     # °C
        "soil_moisture": round(random.uniform(0.3, 0.9), 2), # normalized
        "co2_absorbed": round(random.uniform(0.02, 0.06), 3) # kg/day
    }

# ---- Main UI ----
st.title("🌿 TerraTrack: Smart Terrarium Dashboard")

placeholder = st.empty()

# ---- Real-Time Simulation Loop ----
while True if auto_refresh else False:
    data = generate_data()
    
    with placeholder.container():
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
            st.write("Equivalent to planting ~1 tree/month")

        st.divider()

        st.subheader("📊 Energy Usage Log")
        energy_data = [round(random.uniform(0.3, 1.5), 2) for _ in range(12)]
        time_labels = [f"{hour}:00" for hour in range(8, 20)]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_labels, y=energy_data, fill='tozeroy', line_shape='spline', name="Power (W)"))
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=20), height=300)
        st.plotly_chart(fig, use_container_width=True)

    time.sleep(refresh_interval)
    placeholder.empty()
    if not auto_refresh:
        break
