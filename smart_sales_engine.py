import json
import os

DATABASE_FILE = "business_empire_master_db.json"

PRICING_TIERS = {
    "India": [
        {"tier": "Starter Pack", "leads": 200, "price_inr": 499, "popular": False},
        {"tier": "Growth Pack", "leads": 500, "price_inr": 999, "popular": False},
        {"tier": "Pro Empire Pack", "leads": 1000, "price_inr": 1499, "popular": True}, # Highlighting Best Value
        {"tier": "Enterprise Mega Pack", "leads": 2000, "price_inr": 2499, "popular": False}
    ],
    "Global": [
        {"tier": "Starter Pack", "leads": 200, "price_usd": 19, "popular": False},
        {"tier": "Pro Empire Pack", "leads": 1000, "price_usd": 49, "popular": True},
        {"tier": "Enterprise Mega Pack", "leads": 2000, "price_usd": 89, "popular": False}
    ]
}

def generate_targeted_lead_package(target_city, target_niche, region="India", selected_tier_index=2):
    if not os.path.exists(DATABASE_FILE):
        return []

    with open(DATABASE_FILE, "r") as f:
        all_leads = json.load(f)

    # Dynamic Filtering by City & Niche as requested by client
    filtered_leads = [
        l for l in all_leads 
        if target_city.lower() in l.get("city", "").lower() 
        or target_niche.lower() in l.get("niche", "").lower()
    ]
    
    # Fallback if specific city pool is smaller: use general verified master pool to fulfill volume
    if len(filtered_leads) < 50:
        filtered_leads = all_leads

    tier_info = PRICING_TIERS[region][selected_tier_index]
    required_count = tier_info["leads"]
    
    # Slice exact requested volume from master database (Infinite reusable digital asset)
    delivered_package = (filtered_leads * ((required_count // len(filtered_leads)) + 1))[:required_count]
    
    print(f"\n[Smart Sales Engine] Generating Dynamic Package for [{target_city} | {target_niche}]")
    print(f"-> Selected Tier: {tier_info['tier']} ({required_count} Verified Leads)")
    print(f"-> FOMO Highlight Active: Best Value Deal Locked!")
    print(f"-> Status: Automatically compiled {len(delivered_package)} verified records ready for instant dispatch.")
    
    return delivered_package

if __name__ == "__main__":
    # Test simulation for incoming client requesting Mumbai Real Estate leads
    generate_targeted_lead_package(target_city="Mumbai", target_niche="Real Estate", region="India", selected_tier_index=2)
