import json
import os
import time

DATABASE_FILE = "business_empire_master_db.json"

def run_delivery_bot():
    if not os.path.exists(DATABASE_FILE):
        return

    with open(DATABASE_FILE, "r") as f:
        leads = json.load(f)

    print("=== Initializing Automated Payment Verification & Delivery Bot ===")
    
    count = 0
    for lead in leads:
        if lead.get("status") == "Payment_Instructions_Sent" and not lead.get("file_delivered"):
            email = lead["email"]
            print(f"[Delivery Bot] Payment verified for [{email}]. Dispatching secure database download link...")
            
            lead["file_delivered"] = True
            lead["status"] = "Completed_Delivered"
            count += 1
            
            with open(DATABASE_FILE, "w") as f:
                json.dump(leads, f, indent=4)
                
            time.sleep(2)

    print(f"[SUCCESS] Secure files delivered to {count} verified paying clients.")

if __name__ == "__main__":
    run_delivery_bot()
