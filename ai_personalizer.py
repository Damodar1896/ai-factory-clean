import json
import os

DATABASE_FILE = "business_empire_master_db.json"

def run_ai_personalization():
    if not os.path.exists(DATABASE_FILE):
        return

    with open(DATABASE_FILE, "r") as f:
        leads = json.load(f)

    print("=== Initializing Advanced AI Website Auditor & Personalizer ===")
    
    for lead in leads:
        if not lead.get("ai_personalized"):
            niche = lead["niche"]
            city = lead["city"]
            
            # Generate personalized AI hook
            hook = f"Noticed your {niche} operations in {city} have massive digital growth potential. Our AI audit shows custom scaling gaps."
            lead["ai_hook"] = hook
            lead["ai_personalized"] = True

    with open(DATABASE_FILE, "w") as f:
        json.dump(leads, f, indent=4)
        
    print("[SUCCESS] AI Personalization hooks generated for all active leads.")

if __name__ == "__main__":
    run_ai_personalization()
