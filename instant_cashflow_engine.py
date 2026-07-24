import os
import json

CASHFLOW_DB = os.path.expanduser("~/ai-factory/affiliate_bot/instant_cashflow_status.json")

def initialize_instant_cashflow():
    print("============================================================")
    print("     💰 DAMODAR TECH CRAZE - 10-POINT CASHFLOW ENGINE 💰    ")
    print("============================================================")
    
    methods = [
        {"id": 1, "name": "AI Content Writing & Translation Gigs", "target": "Fiverr / Upwork", "payout": "$10 - $50 per article"},
        {"id": 2, "name": "Social Media Content Clipping", "target": "Local Agencies & Creators", "payout": "$50 - $100 / month retainer"},
        {"id": 3, "name": "Micro-Task & Data Labeling", "target": "Amazon MTurk / Clickworker", "payout": "$5 - $20 per day"},
        {"id": 4, "name": "Digital Micro-Store E-books / Prompts", "target": "damodartechcraze.com/store", "payout": "100% Margin Direct Sales"},
        {"id": 5, "name": "Local Business GMB Optimization", "target": "Local Shops & Clinics", "payout": "₹1,000 - ₹3,000 per setup"},
        {"id": 6, "name": "Affiliate Review Content Placement", "target": "Hostinger / NordVPN", "payout": "$40 - $100 per sale"},
        {"id": 7, "name": "Logo & Graphic Design using AI", "target": "Canva / Midjourney Brands", "payout": "$15 - $30 per design"},
        {"id": 8, "name": "Telegram / WhatsApp Deal Promotion", "target": "Flash Sale Channels", "payout": "Daily Commission Payouts"},
        {"id": 9, "name": "Website Bug Fixing & Landing Pages", "target": "HTML/CSS / WordPress", "payout": "$50 per landing page"},
        {"id": 10, "name": "CPA & Free Sign-up Lead Generation", "target": "Software Free Trials", "payout": "$1.50 - $5.00 per lead"}
    ]
    
    os.makedirs(os.path.dirname(CASHFLOW_DB), exist_ok=True)
    with open(CASHFLOW_DB, "w") as f:
        json.dump(methods, f, indent=4)
        
    for m in methods:
        print(f" -> [{m['id']}] {m['name']} | Target: {m['target']} | Payout: {m['payout']}")
        
    print("-" * 60)
    print("[Success] All 10 Instant Cashflow & Day-1 Earning methods synchronized & active!")
    print("============================================================")

if __name__ == "__main__":
    initialize_instant_cashflow()
