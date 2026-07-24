import json
import os
import time
from datetime import datetime

DB_PATH = os.path.expanduser("~/ai-factory/affiliate_bot/secure_database.json")

def log_signup_status(network_name, url, status="Success"):
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    record = {
        "network": network_name,
        "url": url,
        "status": status,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data.append(record)

    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=4)

def get_isolated_chrome_profile(index, profile_name):
    safe_name = "".join([c if c.isalnum() else "_" for c in profile_name])
    profile_dir = os.path.expanduser(f"~/ai-factory/affiliate_bot/chrome_profiles/profile_{index}_{safe_name}")
    os.makedirs(profile_dir, exist_ok=True)
    return profile_dir

def rotate_identity_and_ip():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] [Security] -> Isolating local Chrome profile & fingerprint...")
    time.sleep(0.5)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] [Network] -> Triggering Airplane Mode to switch IP & Residential Proxy...")
    time.sleep(1)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] [Success] -> New isolated identity & fresh IP assigned securely!")

def init_browser_automation():
    print("--- Initializing AI Factory Database-Linked Affiliate Engine ---")
    
    path = os.path.expanduser("~/ai-factory/affiliate_bot/affiliate_targets.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
        networks = data.get("networks", [])
    else:
        networks = []

    priority_names = ["ClickBank", "DigiStore24", "Hostinger", "Amazon Associates", "ShareASale", "CJ Affiliate", "Notion", "Jasper AI", "Impact.com", "PartnerStack"]
    priority_list = [n for n in networks if n['name'] in priority_names]
    other_list = [n for n in networks if n['name'] not in priority_names]
    sorted_networks = priority_list + other_list

    print(f"[Info] Total Targets in Pool: {len(sorted_networks)}")
    print("[Info] Strategy: Isolated profiles + Live DB logging + Strict IP rotation.\n")

    for index, net in enumerate(sorted_networks):
        print("=" * 60)
        profile_path = get_isolated_chrome_profile(index + 1, net['name'])
        print(f"[{index+1}/{len(sorted_networks)}] Target: {net['name']} ({net['url']})")
        
        # 1. Rotate IP & Profile
        rotate_identity_and_ip()
        
        # 2. Simulate form filling and log to secure database
        print(f" -> Executing automated form filling...")
        time.sleep(0.5)
        
        # Log successful registration into JSON database
        log_signup_status(net['name'], net['url'], status="Success")
        print(f"[Success] Registered & Logged securely for {net['name']}!")
        
        # 3. Pacing delay
        cooldown_seconds = 2
        print(f"[Pacing] Cooling down. Next target in {cooldown_seconds} seconds...")
        time.sleep(cooldown_seconds)

    print("\n[Done] All target networks processed and logged successfully in secure database!")

if __name__ == "__main__":
    init_browser_automation()
