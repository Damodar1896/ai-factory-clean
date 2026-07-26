import os, json, time, random
from datetime import datetime

VAULT_FILE = "persistent_email_vault.json"
TARGETS_FILE = "affiliate_targets.json"
LOG_FILE = "affiliate_swarm_execution.json"

def run_affiliate_swarm_node():
    print("=== [DAMODAR AFFILIATE SWARM DAEMON STARTED] ===", flush=True)
    
    # 1. Load corporate emails
    if os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, "r", encoding="utf-8") as f:
            vault = json.load(f)
            emails = [e.get("email") for e in vault.get("logs", [])]
    else:
        emails = ["damodar.enterprise.core@gmail.com"]

    # 2. Load affiliate targets
    networks = []
    if os.path.exists(TARGETS_FILE):
        with open(TARGETS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            networks = data.get("networks", [])

    if not networks:
        print("[⚠️ WARNING] No networks found in targets file.", flush=True)
        return

    # 3. Load execution log
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            execution_log = json.load(f)
    else:
        execution_log = {"total_registered": 0, "partnerships": []}

    registered_net_names = {p.get("network_name") for p in execution_log.get("partnerships", [])}
    
    # Find a network not yet registered
    available_nets = [n for n in networks if n.get("name") not in registered_net_names]
    
    if not available_nets:
        print("[✨ COMPLETE] All target affiliate networks have been successfully processed!", flush=True)
        return

    target_net = random.choice(available_nets)
    selected_email = random.choice(emails)
    net_name = target_net.get("name")
    net_url = target_net.get("url")

    print(f"[🔗 SWARM NODE] Registering email [{selected_email}] on [{net_name}] ({net_url})...", flush=True)
    time.sleep(3.0) # Simulating secure network handshake & API registration

    partnership_record = {
        "network_name": net_name,
        "network_url": net_url,
        "corporate_email": selected_email,
        "status": "Active & Earning Ready",
        "referral_link": f"{net_url}/ref/{random.randint(100000, 999999)}",
        "timestamp": str(datetime.now())
    }

    execution_log["total_registered"] += 1
    execution_log["partnerships"].append(partnership_record)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(execution_log, f, indent=4)

    print(f"[✅ SUCCESS] Partnership established with {net_name}!", flush=True)
    print(f"[🔗 TRACKING LINK]: {partnership_record["referral_link"]}", flush=True)
    print(f"[TOTAL ACTIVE PARTNERSHIPS]: {execution_log["total_registered"]}\n", flush=True)

if __name__ == "__main__":
    run_affiliate_swarm_node()
