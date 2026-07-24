import os
import json
from datetime import datetime

TRACKING_DB = os.path.expanduser("~/ai-factory/affiliate_bot/conversion_log.json")

def init_tracker():
    if not os.path.exists(TRACKING_DB):
        initial_data = {
            "total_clicks": 0,
            "active_campaigns": 45,
            "conversions": []
        }
        with open(TRACKING_DB, "w") as f:
            json.dump(initial_data, f, indent=4)
    print("[Success] Conversion & Click Tracking Database initialized.")

def log_click(network_name, email_used):
    if not os.path.exists(TRACKING_DB):
        init_tracker()
        
    with open(TRACKING_DB, "r") as f:
        data = json.load(f)
        
    data["total_clicks"] += 1
    event = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "network": network_name,
        "assigned_email": email_used,
        "status": "Routed & Tracked Securely"
    }
    data["conversions"].append(event)
    
    with open(TRACKING_DB, "w") as f:
        json.dump(data, f, indent=4)
        
    print(f"[Tracker] Logged click for {network_name} via {email_used} | Total Clicks: {data['total_clicks']}")

if __name__ == "__main__":
    init_tracker()
    # Test logging simulation
    log_click("ClickBank", "support@damodartechcraze.com")
