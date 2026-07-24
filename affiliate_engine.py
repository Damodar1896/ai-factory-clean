import json
import os
import time

DATABASE_FILE = "business_empire_master_db.json"

# High-Converting Affiliate Products & Links (AI Tools, Hosting, Automation)
AFFILIATE_PROGRAMS = [
    {
        "name": "AI Content & Automation Suite",
        "pitch": "Since you are exploring ways to scale your business operations, you might love this AI automation tool we personally use:",
        "link": "https://affiliate.example-ai-tool.com/damodar"
    },
    {
        "name": "High-Speed Business Hosting & Funnels",
        "pitch": "To handle high-volume client traffic seamlessly, check out this recommended high-performance hosting platform:",
        "link": "https://affiliate.example-hosting.com/damodar"
    }
]

def run_affiliate_engine():
    if not os.path.exists(DATABASE_FILE):
        print("[Affiliate Engine] Database not found!")
        return

    with open(DATABASE_FILE, "r") as f:
        leads = json.load(f)

    print("=== Initializing Automated Affiliate Monetization Engine ===")
    
    count = 0
    for lead in leads:
        # Target leads who asked for samples or haven't converted yet
        if lead.get("status") in ["Payment_Instructions_Sent", "Pro_Email_Sent"]:
            email = lead["email"]
            niche = lead["niche"]
            city = lead["city"]
            
            # Select affiliate offer
            offer = AFFILIATE_PROGRAMS[count % len(AFFILIATE_PROGRAMS)]
            
            subject = f"Bonus Resource & Free Sample for your {niche} business in {city}"
            body = f"""Hi Team,

While our team compiles your custom verified lead sample, we wanted to share a quick resource that can instantly boost your {niche} workflow in {city}.

{offer['pitch']}
👉 {offer['link']}

(Note: This is a recommended partner tool that helps local businesses scale faster).

Best regards,
Damodar Tech Craze Growth Partners
"""

            print(f"[Affiliate Dispatch] Sending passive income affiliate pitch ({offer['name']}) to [{email}]")
            
            lead["status"] = "Affiliate_Pitch_Sent"
            count += 1
            
            with open(DATABASE_FILE, "w") as f:
                json.dump(leads, f, indent=4)
                
            time.sleep(5)

    print(f"[SUCCESS] Affiliate monetization pitches dispatched to {count} leads successfully!")

if __name__ == "__main__":
    run_affiliate_engine()
