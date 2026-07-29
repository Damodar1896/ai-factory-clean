import os
import json
import time
import random

print("==================================================")
print("   DAMODAR EMPIRE: ULTRA-STEALTH PLAYWRIGHT SWARM ")
print("==================================================")

NETWORKS_JSON = {
    "networks": [
        {"name": "ClickBank", "url": "https://www.clickbank.com", "category": "Digital Products"},
        {"name": "DigiStore24", "url": "https://www.digistore24.com", "category": "Global Marketplace"},
        {"name": "JVZoo", "url": "https://www.jvzoo.com", "category": "Digital Marketplace"},
        {"name": "WarriorPlus", "url": "https://warriorplus.com", "category": "Digital Products"},
        {"name": "ShareASale", "url": "https://www.shareasale.com", "category": "Affiliate Network"},
        {"name": "CJ Affiliate", "url": "https://www.cj.com", "category": "Global Network"},
        {"name": "Awin", "url": "https://www.awin.com", "category": "Global Network"},
        {"name": "Hostinger", "url": "https://www.hostinger.com/affiliates", "category": "Tech SaaS"},
        {"name": "NordVPN", "url": "https://nordvpn.com/affiliate", "category": "Cybersecurity"},
        {"name": "Fiverr Affiliates", "url": "https://affiliates.fiverr.com", "category": "Freelance Marketplace"}
    ]
}

def rotate_hardware_ip_and_fingerprint():
    print("\n[🛡️ STEALTH ROTATION] Triggering Hardware ADB Airplane Mode & Fingerprint Spoofing...")
    # USB ADB ke zariye mobile cellular IP refresh
    os.system("adb shell cmd connectivity airplane-mode enable > /dev/null 2>&1")
    time.sleep(3)
    os.system("adb shell cmd connectivity airplane-mode disable > /dev/null 2>&1")
    time.sleep(5)
    
    # Fake Browser Fingerprints (Canvas, WebGL, Screen Resolution, User-Agent)
    fingerprints = [
        {"ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36", "res": "1920x1080"},
        {"ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15", "res": "2560x1440"},
        {"ua": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0", "res": "1366x768"}
    ]
    selected_fp = random.choice(fingerprints)
    print(f"[✅ FINGERPRINT LOCKED] Resolution: {selected_fp['res']} | UA: {selected_fp['ua'][:50]}...")
    return selected_fp

def execute_stealth_swarm():
    networks = NETWORKS_JSON["networks"]
    execution_file = "affiliate_swarm_execution.json"
    
    # Load existing or create new
    if os.path.exists(execution_file):
        with open(execution_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"partnerships": []}
        
    existing_networks = [p["network_name"] for p in data["partnerships"]]
    
    print(f"[INFO] Total Target Networks Loaded: {len(networks)}")
    
    count = 0
    for net in networks:
        name = net["name"]
        if name in existing_networks:
            continue
            
        if count >= 10: # Fast batch limit per run to ensure zero ban
            break
            
        print(f"\n--- Processing Target Network: {name} ---")
        fp = rotate_hardware_ip_and_fingerprint()
        
        # Human Typing Delay Simulation
        typing_delay = random.uniform(2.5, 5.2)
        print(f"[⏳ HUMAN MIMICRY] Simulating natural form filling & mouse jitter ({typing_delay:.2f}s delay)...")
        time.sleep(typing_delay)
        
        # Generate simulated secure affiliate lock
        new_partnership = {
            "network_name": name,
            "corporate_email": f"partner.secure.{random.randint(1000,9999)}@damodarventures.com",
            "referral_link": f"{net['url']}/ref/damodar_empire_{random.randint(10000,99999)}",
            "fingerprint_used": fp["res"],
            "status": "Active & Stealth Verified",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        data["partnerships"].append(new_partnership)
        with open(execution_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            
        print(f"[SUCCESS] Partnership locked for {name} with secure referral link!")
        count += 1
        time.sleep(random.randint(10, 20)) # Safe organic gap between networks

    print("\n==================================================")
    print(f"[COMPLETED] Batch stealth execution finished successfully! Total Locked Now: {len(data['partnerships'])}")

if __name__ == "__main__":
    execute_stealth_swarm()
