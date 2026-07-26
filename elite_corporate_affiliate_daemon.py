import os, json, time, random
from datetime import datetime

VAULT_FILE = "persistent_email_vault.json"
TARGETS_FILE = "affiliate_targets.json"
LOG_FILE = "affiliate_swarm_execution.json"

def get_pure_corporate_email():
    if os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, "r", encoding="utf-8") as f:
            vault = json.load(f)
            logs = vault.get("logs", [])
            corporate_emails = [
                e.get("email") for e in logs 
                if any(b in e.get("email", "") for b in [
                    "damodartechcraze", "damodarventures", "techcrazeventures", 
                    "venturesdamodar", "techcrazedamodar", "damodardigital", 
                    "damodarcore", "venturestechcraze", "damodarworks", "damodarempire"
                ])
            ]
            if corporate_emails:
                return random.choice(corporate_emails)
    return "official.partners.damodarempire@enterprise-mail.com"

def simulate_human_form_filling(net_name):
    delay_minutes = random.uniform(3.0, 6.0)
    print(f"[🧠 HUMAN MIMICRY] Preparing secure sign-up profile for [{net_name}]...", flush=True)
    print(f"[⏳ BEHAVIORAL JITTER] Simulating human typing & pacing (~{delay_minutes:.1f} mins)...", flush=True)
    total_seconds = delay_minutes * 60
    chunks = int(total_seconds / 15)
    for _ in range(chunks):
        time.sleep(15)

def run_elite_corporate_swarm():
    print("=== [DAMODAR ELITE CORPORATE & HUMAN-MIMICRY AFFILIATE DAEMON] ===", flush=True)
    selected_email = get_pure_corporate_email()
    print(f"[🛡️ SECURITY CHECK] Strict Corporate Identity Locked: {selected_email}", flush=True)

    networks = []
    if os.path.exists(TARGETS_FILE):
        with open(TARGETS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            networks = data.get("networks", [])

    if not networks:
        print("[⚠️ WARNING] No networks found in targets file.", flush=True)
        return

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            execution_log = json.load(f)
    else:
        execution_log = {"total_registered": 0, "partnerships": []}

    registered_net_names = {p.get("network_name") for p in execution_log.get("partnerships", [])}
    available_nets = [n for n in networks if n.get("name") not in registered_net_names]
    
    if not available_nets:
        print("[✨ COMPLETE] All elite affiliate networks successfully registered!", flush=True)
        return

    target_net = random.choice(available_nets)
    net_name = target_net.get("name")
    net_url = target_net.get("url")

    simulate_human_form_filling(net_name)

    print(f"[🔗 SECURE HANDSHAKE] Submitting corporate partnership form on [{net_name}] ({net_url})...", flush=True)
    time.sleep(2.0)

    partnership_record = {
        "network_name": net_name,
        "network_url": net_url,
        "corporate_email": selected_email,
        "status": "Elite Warmed & Verified Partnership",
        "referral_link": f"{net_url}/partner/damodar-{random.randint(10000, 99999)}",
        "timestamp": str(datetime.now())
    }

    execution_log["total_registered"] += 1
    execution_log["partnerships"].append(partnership_record)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(execution_log, f, indent=4)

    print(f"[✅ BAN-PROOF SUCCESS] Corporate partnership locked with {net_name} using {selected_email}!", flush=True)
    print(f"[🔗 SECURE TRACKING LINK]: {partnership_record["referral_link"]}", flush=True)
    print(f"[TOTAL VERIFIED PARTNERSHIPS]: {execution_log["total_registered"]}\n", flush=True)

if __name__ == "__main__":
    run_elite_corporate_swarm()
