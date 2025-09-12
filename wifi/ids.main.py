#!/usr/bin/env python3
"""
Passive WiFi IDS - ids_main.py
Run as root. Sniffs 802.11 frames and writes stats.json and alerts.json.
"""

import json
import time
import argparse
from collections import defaultdict, deque
from threading import Thread, Event, Lock
from scapy.all import sniff, Dot11, Dot11Deauth, RadioTap, ARP, Dot11Elt
from datetime import datetime

# --- Config load ---
import os
CONFIG_PATH = "config.json"
DEFAULT_CONFIG = {
    "flood_window_seconds": 5,
    "flood_packet_threshold": 100,
    "probe_window_seconds": 60,
    "probe_request_threshold": 200,
    "deauth_flag": True,
    "stats_write_interval": 1,
    "alerts_write_interval": 1
}
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH) as f:
        cfg = json.load(f)
else:
    cfg = DEFAULT_CONFIG

# --- Shared state ---
device_lock = Lock()
device_stats = {}   # mac -> {last_seen, pkt_count_total, deque(timestamps), vendor(optional)}
alerts = []        # list of dicts (append-only)

# for ARP detection
arp_map = {}  # ip -> mac

stop_event = Event()

def now_ts():
    return datetime.utcnow().isoformat() + "Z"

def atomic_write(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, path)

# --- Detection helpers ---
def add_alert(event_type, info):
    a = {
        "timestamp": now_ts(),
        "event_type": event_type,
        "info": info
    }
    # dedupe basic: avoid exact duplicates in short time
    with device_lock:
        if alerts and alerts[-1].get("event_type")==event_type and alerts[-1].get("info")==info:
            # skip identical immediate duplicate
            return
        alerts.append(a)

def check_deauth(pkt, src_mac):
    # Dot11Deauth layer or subtype detection
    if pkt.haslayer(Dot11Deauth):
        add_alert("DEAUTH_FRAME", {"src_mac": src_mac})
        return True
    # Some captures may present as Dot11 with subtype==12
    try:
        if pkt.haslayer(Dot11) and pkt.type == 0 and pkt.subtype == 12:
            add_alert("DEAUTH_FRAME", {"src_mac": src_mac})
            return True
    except Exception:
        pass
    return False

def check_flood(mac, timestamp):
    w = cfg.get("flood_window_seconds", 5)
    th = cfg.get("flood_packet_threshold", 100)
    d = device_stats.setdefault(mac, {"last_seen":timestamp,"pkt_count_total":0,"timestamps":deque()})
    dq = d["timestamps"]
    dq.append(timestamp)
    # remove older
    cutoff = timestamp - w
    while dq and dq[0] < cutoff:
        dq.popleft()
    if len(dq) > th:
        add_alert("FLOOD", {"src_mac": mac, "count_in_window": len(dq), "window_s": w})
        # reset deque so repeated alerts are rate-limited
        dq.clear()
        return True
    return False

def check_probe(pkt, src_mac, timestamp):
    # Probe requests are Dot11 management subtype 4
    if pkt.haslayer(Dot11) and pkt.type == 0 and pkt.subtype == 4:
        key = f"probe::{src_mac}"
        d = device_stats.setdefault(key, {"last_seen":timestamp,"pkt_count_total":0,"timestamps":deque()})
        dq = d["timestamps"]
        dq.append(timestamp)
        w = cfg.get("probe_window_seconds", 60)
        th = cfg.get("probe_request_threshold", 200)
        cutoff = timestamp - w
        while dq and dq[0] < cutoff:
            dq.popleft()
        if len(dq) > th:
            add_alert("PROBE_FLOOD", {"src_mac": src_mac, "count_in_window": len(dq), "window_s": w})
            dq.clear()
            return True
    return False

def check_arp(pkt):
    if pkt.haslayer(ARP):
        arp = pkt.getlayer(ARP)
        # arp.op = 1 (who-has), 2 (is-at)
        if arp.op == 2 and hasattr(arp, "psrc") and hasattr(arp, "hwsrc"):
            ip = arp.psrc
            mac = arp.hwsrc
            prev = arp_map.get(ip)
            if prev and prev != mac:
                add_alert("ARP_CONFLICT", {"ip": ip, "prev_mac": prev, "new_mac": mac})
            arp_map[ip] = mac

def extract_ssid(pkt):
    # For rogue AP detection (beacon/probe response), extract SSID if present
    if pkt.haslayer(Dot11Elt):
        try:
            ssid = pkt[Dot11Elt].info.decode('utf-8', errors='ignore')
            return ssid
        except Exception:
            return None
    return None

# --- Packet handler ---
def handle_packet(pkt):
    timestamp = time.time()
    if not pkt.haslayer(Dot11):
        return

    dot11 = pkt.getlayer(Dot11)
    src = dot11.addr2  # transmitter
    dst = dot11.addr1  # receiver
    if not src:
        return

    # update device basic stats
    with device_lock:
        d = device_stats.setdefault(src, {"last_seen": timestamp, "pkt_count_total":0, "timestamps": deque(), "vendor": None})
        d["last_seen"] = timestamp
        d["pkt_count_total"] += 1

    # detection rules
    # 1) Deauth
    if cfg.get("deauth_flag", True):
        if check_deauth(pkt, src):
            pass

    # 2) Flooding / high packet rate
    check_flood(src, timestamp)

    # 3) Probe request flood
    check_probe(pkt, src, timestamp)

    # 4) ARP anomalies
    check_arp(pkt)

    # 5) Optional: rogue AP detection by looking at Beacons/Probe responses with same SSID but different BSSID
    # Keep a small mapping of ssid->set(bssids)
    if dot11.type == 0 and dot11.subtype in (8,5,9):  # beacon/probe-resp/?? (8=beacon)
        ssid = extract_ssid(pkt)
        if ssid:
            bssid = dot11.addr3
            key = f"ssid::{ssid}"
            with device_lock:
                ent = device_stats.setdefault(key, {"bssids": set(), "last_seen": timestamp})
                ent["bssids"].add(bssid)
                ent["last_seen"] = timestamp
                # detect multiple BSSIDs advertising same SSID in short space could indicate evil twin
                if len(ent["bssids"]) > 3:
                    add_alert("ROGUE_AP_POSSIBLE", {"ssid": ssid, "bssids": list(ent["bssids"])})

# --- Writers to disk ---
def periodic_writer():
    while not stop_event.is_set():
        with device_lock:
            # prepare compact stats for UI
            compact = {}
            for mac, val in device_stats.items():
                if isinstance(val, dict):
                    compact[mac] = {
                        "last_seen": val.get("last_seen"),
                        "pkt_count_total": val.get("pkt_count_total", 0),
                        # window_count = len(timestamps) if timestamps in val else 0
                        "window_count": len(val.get("timestamps", []))
                    }
            alerts_copy = list(alerts[-200:])  # keep last 200 alerts
        try:
            atomic_write("stats.json", {"generated_at": now_ts(), "devices": compact})
            atomic_write("alerts.json", {"generated_at": now_ts(), "alerts": alerts_copy})
        except Exception as e:
            print("Error writing json:", e)
        time.sleep(cfg.get("stats_write_interval", 1))

def main():
    parser = argparse.ArgumentParser(description="Passive WiFi IDS")
    parser.add_argument("--iface", required=True, help="monitor mode interface (e.g. wlan0mon)")
    args = parser.parse_args()
    iface = args.iface

    writer_thread = Thread(target=periodic_writer, daemon=True)
    writer_thread.start()

    print(f"Starting sniff on interface: {iface} (press Ctrl+C to stop)")
    try:
        sniff(iface=iface, prn=handle_packet, store=0)
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        stop_event.set()
        writer_thread.join(timeout=2)
        # one last flush
        with device_lock:
            atomic_write("stats.json", {"generated_at": now_ts(), "devices": device_stats})
            atomic_write("alerts.json", {"generated_at": now_ts(), "alerts": alerts})
        print("Shutdown complete.")

if __name__ == "__main__":
    main()
