import json
import os
from datetime import datetime

DB_PATH = os.path.expanduser("~/ai-factory/affiliate_bot/secure_database.json")

def log_signup_status(network_name, url, status="Success"):
    # Load existing database or create new
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # New record entry
    record = {
        "network": network_name,
        "url": url,
        "status": status,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    data.append(record)

    # Save back to secure database
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"[Database] -> Saved record for {network_name} as [{status}]")

if __name__ == "__main__":
    log_signup_status("Test Network", "https://example.com", "Success")
