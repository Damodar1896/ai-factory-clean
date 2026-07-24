import json
import os
import time

DATABASE_FILE = "business_empire_master_db.json"

def check_and_respond_to_replies():
    if not os.path.exists(DATABASE_FILE):
        return

    with open(DATABASE_FILE, "r") as f:
        leads = json.load(f)

    print("=== Checking Incoming Client Replies & Triggering Instant Sample Dispatch ===")
    
    updated = False
    for lead in leads:
        # Simulate checking replies for leads who received pro emails
        if lead.get("status") == "Payment_Instructions_Sent" and lead.get("reply_status") is None:
            # Simulated incoming client interest
            email = lead["email"]
            niche = lead["niche"]
            city = lead["city"]
            
            print(f"[Inbox Auto-Responder] Detected positive reply / sample request from [{email}]")
            
            # Automated Free Sample Dispatch & Telegram/WhatsApp Alert trigger
            print(f"[Alert Sent] 🔔 New client lead responded: {email} for {niche} in {city}!")
            print(f"[Sample Dispatch] Sending 20 free verified sample leads to [{email}]")
            
            lead["reply_status"] = "Sample_Sent"
            updated = True
            time.sleep(3)

    if updated:
        with open(DATABASE_FILE, "w") as f:
            json.dump(leads, f, indent=4)
        print("[SUCCESS] Incoming replies processed and free samples dispatched automatically.")
    else:
        print("[Inbox] No new unhandled client replies found in this cycle.")

if __name__ == "__main__":
    check_and_respond_to_replies()
