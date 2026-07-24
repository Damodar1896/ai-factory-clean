import json
import os

DATABASE_FILE = "business_empire_master_db.json"

def run_master_bridge():
    print("=== [MASTER AUTOMATION BRIDGE] Initializing Single-Gmail & Storefront Sync ===")
    
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as f:
            leads = json.load(f)
    else:
        leads = []

    active_sync_count = 0
    for lead in leads:
        # Syncing all automated touchpoints with master master storefront & single gmail
        if lead.get("status") == "Payment_Instructions_Sent":
            lead["master_channel"] = "Automated_Storefront_Checkout"
            lead["support_email"] = "damodartechcraze@gmail.com"
            active_sync_count += 1

    with open(DATABASE_FILE, "w") as f:
        json.dump(leads, f, indent=4)
        
    print(f"[SUCCESS] Master Bridge synced {active_sync_count} leads to the automated checkout & delivery pipeline.")

if __name__ == "__main__":
    run_master_bridge()
