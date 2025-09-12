import streamlit as st
import pandas as pd
import time
import json
from datetime import datetime

st.set_page_config(page_title="WiFi IDS Dashboard", layout="wide")

st.title("WiFi IDS — Live Dashboard")

def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return None

col1, col2 = st.columns([2,1])

with col1:
    st.header("Connected / Seen Devices")
    dev_table = st.empty()
    st.header("Traffic (window counts)")

with col2:
    st.header("Alerts (recent)")
    alerts_box = st.empty()
    st.header("Control")
    st.text("Files: stats.json, alerts.json")
    st.write("Refresh interval (seconds):")
    interval = st.number_input("", min_value=1, max_value=10, value=2)

# autorefresh
placeholder = st.empty()
last_generated = None

while True:
    stats = load_json("stats.json")
    alerts = load_json("alerts.json")

    if stats and "generated_at" in stats:
        last_generated = stats["generated_at"]
    if stats and "devices" in stats:
        devs = stats["devices"]
        rows = []
        for mac, info in devs.items():
            rows.append({
                "mac": mac,
                "last_seen": info.get("last_seen"),
                "total_pkts": info.get("pkt_count_total", 0),
                "window_count": info.get("window_count", 0)
            })
        df = pd.DataFrame(rows)
        if not df.empty:
            df['last_seen'] = df['last_seen'].apply(lambda x: datetime.fromtimestamp(x).strftime("%H:%M:%S") if isinstance(x, (int, float)) else x)
            dev_table.dataframe(df.sort_values(by="window_count", ascending=False).head(200), use_container_width=True)
        else:
            dev_table.text("No devices seen yet.")

    if alerts and "alerts" in alerts:
        a = alerts["alerts"]
        if a:
            df_a = pd.DataFrame(a)
            df_a['timestamp'] = df_a['timestamp'].astype(str)
            alerts_box.dataframe(df_a.sort_values(by="timestamp", ascending=False).head(50))
        else:
            alerts_box.text("No alerts yet.")

    placeholder.markdown(f"Last stats generation: **{last_generated}**")
    time.sleep(interval)
