import json
import os
import time

DATABASE_FILE = "business_empire_master_db.json"

def send_automated_outreach():
    if not os.path.exists(DATABASE_FILE):
        print("[Outreach] Database file not found yet. Run scraper first!")
        return

    with open(DATABASE_FILE, "r") as f:
        leads = json.load(f)

    print("=== Initializing Automated Cold Email & Pitch Dispatcher ===")
    
    outreach_sent_count = 0
    for lead in leads:
        if lead.get("status") == "Fresh_Verified":
            # Simulate personalized AI pitch generation based on business niche
            email = lead["email"]
            niche = lead["niche"]
            city = lead["city"]
            
            print(f"[Dispatching] Sending high-converting AI growth pitch to [{email}] for their {niche} business in {city}...")
            
            # Here real SMTP or Email API (like SendGrid/Gmail API) will be triggered
            # Mark lead as contacted to prevent duplicate emailing
            lead["status"] = "Email_Sent_Waiting_Reply"
            outreach_sent_count += 1
            
            # Save updated status
            with open(DATABASE_FILE, "w") as f:
                json.dump(leads, f, indent=4)
                
            # Human-like delay to ensure high inbox delivery and avoid spam filters
            time.sleep(5)

    print(f"[SUCCESS] Outreach batch completed! Sent pitches to {outreach_sent_count} fresh leads.")

if __name__ == "__main__":
    send_automated_outreach()
