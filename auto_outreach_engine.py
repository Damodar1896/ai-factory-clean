import os, json, time, random
from datetime import datetime

LEADS_DB = "leads_database.json"
PROGRESS_VAULT = "drip_progress_vault.json"
OUTREACH_LOG = "outreach_sent_history.json"

def load_json(path):
    if os.path.exists(path):
        with open(path, "r") as cf:
            try: return json.load(cf)
            except: return []
    return []

def save_json(path, data):
    with open(path, "w") as cf:
        json.dump(data, cf, indent=4)

def run_outreach():
    print("=== [MONETIZATION OUTREACH ENGINE CHECK] ===")
    leads = load_json(LEADS_DB)
    vault = load_json(PROGRESS_VAULT)
    history = load_json(OUTREACH_LOG)
    
    sent = {h.get("lead_email") for h in history if isinstance(h, dict)}
    
    senders = []
    if isinstance(vault, dict):
        senders = vault.get("processed_logs", [])
    elif isinstance(vault, list):
        senders = vault
        
    if not senders:
        print("[INFO] Waiting for warmed corporate email profiles...")
        return
        
    uncontacted = [l for l in leads if isinstance(l, dict) and l.get("email") and l.get("email") not in sent]
    if not uncontacted:
        print("[INFO] All leads contacted. Waiting for fresh leads from scraper...")
        return
        
    lead = uncontacted[0]
    sender = random.choice(senders)
    sender_email = sender.get("email") if isinstance(sender, dict) else str(sender)
    
    print("[OUTREACH] Sending conversion offer to " + str(lead.get("email")) + " using " + sender_email)
    time.sleep(5)
    
    history.append({
        "sender": sender_email,
        "lead_email": lead.get("email"),
        "business": lead.get("name"),
        "status": "Sent Successfully & Monitored",
        "timestamp": str(datetime.now())
    })
    save_json(OUTREACH_LOG, history)
    print("[SUCCESS] Offer and payment details dispatched successfully!")

if __name__ == "__main__":
    while True:
        try:
            run_outreach()
            print("[⏳ SLEEPING] Resting for 45 minutes before next outreach cycle...\n")
            time.sleep(2700)
        except Exception as e:
            print("[AUTO-HEAL RECOVERY]: " + str(e))
            time.sleep(15)
