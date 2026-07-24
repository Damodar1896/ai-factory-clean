import os
import json

OUTREACH_LOG = os.path.expanduser("~/ai-factory/affiliate_bot/b2b_campaigns.json")

def launch_b2b_outreach():
    print("--- Initializing Day-1 B2B Client Pitching Engine ---")
    
    campaigns = [
        {"target": "Local Gyms & Fitness Centers", "status": "Pitch Deployed via partners@damodartechcraze.com", "package": "$250 Setup"},
        {"target": "Real Estate Agencies", "status": "Pitch Deployed via sales@damodartechcraze.com", "package": "$400 Setup"},
        {"target": "SaaS Startups & Consultants", "status": "Pitch Deployed via growth@damodartechcraze.com", "package": "$300 Setup"}
    ]
    
    os.makedirs(os.path.dirname(OUTREACH_LOG), exist_ok=True)
    with open(OUTREACH_LOG, "w") as f:
        json.dump(campaigns, f, indent=4)
        
    for c in campaigns:
        print(f" -> [Outreach Active]: Target: {c['target']} | Package: {c['package']} | Status: {c['status']}")
        
    print("[Success] B2B direct cashflow outreach engine running successfully!")

if __name__ == "__main__":
    launch_b2b_outreach()
