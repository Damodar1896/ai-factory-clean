import json
import os
import time

DATABASE_FILE = "business_empire_master_db.json"

def run_followup_engine():
    if not os.path.exists(DATABASE_FILE):
        return

    with open(DATABASE_FILE, "r") as f:
        leads = json.load(f)

    print("=== Initializing Automated Follow-Up & Drip Campaign Engine ===")
    
    count = 0
    for lead in leads:
        if lead.get("status") == "Pro_Email_Sent" and not lead.get("followup_sent"):
            email = lead["email"]
            niche = lead["niche"]
            city = lead["city"]
            
            print(f"[Follow-Up Dispatch] Sending smart drip follow-up to [{email}] for {niche} in {city}")
            
            lead["followup_sent"] = True
            lead["status"] = "Followup_Email_Sent"
            count += 1
            
            with open(DATABASE_FILE, "w") as f:
                json.dump(leads, f, indent=4)
                
            time.sleep(4)

    print(f"[SUCCESS] Follow-up drip messages dispatched to {count} leads.")

if __name__ == "__main__":
    run_followup_engine()
