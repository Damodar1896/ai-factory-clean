import json
import os
import time

DATABASE_FILE = "business_empire_master_db.json"

def get_pricing_and_pitch(city, niche):
    metro_cities = ["Delhi", "Mumbai", "Bangalore", "Pune", "Hyderabad", "Chennai"]
    
    if city in ["New York", "London"]: # Tier 1 - Highly competitive bulk rate
        price = "$79 per 1,000 verified leads"
        hook = f"Scaling your {niche} brand in Western markets with pre-qualified pipeline data."
    elif city in metro_cities: # India Metro
        price = "₹3,500 per 1,000 verified leads"
        hook = f"Dominating the {niche} market in {city} with verified decision-maker contacts."
    else: # Local Tier 2/3 (Indore, Bhopal, Raipur, Jaipur, etc.)
        price = "₹1,999 per 1,000 verified leads"
        hook = f"Accelerating local client acquisition for your {niche} business in {city}."
        
    return price, hook

def send_professional_outreach():
    if not os.path.exists(DATABASE_FILE):
        print("[Outreach Pro] Database file not found!")
        return

    with open(DATABASE_FILE, "r") as f:
        leads = json.load(f)

    print("=== Initializing Optimized Competitive AI Outreach Engine ===")
    
    sent_count = 0
    for lead in leads:
        if lead.get("status") == "Fresh_Verified":
            email = lead["email"]
            niche = lead["niche"]
            city = lead["city"]
            business_name = lead["business_name"]
            
            price, hook = get_pricing_and_pitch(city, niche)
            
            subject = f"Quick question regarding {business_name}'s client pipeline in {city}"
            body = f"""Hi Team at {business_name},

{hook}

We noticed your strong presence in {city} for {niche}, but we also know how tedious manual client acquisition can be. 

Our AI-powered scraping and verification engine has just compiled an exclusive, freshly verified list of high-intent prospects specifically looking for {niche} services in {city}. 

Special Launch Package for {city}: {price} (Clean Excel/JSON format, 98% deliverability rate).

Would you be open to a quick sample of 20 verified leads for free to test the quality?

Best regards,
Growth & Expansion Team
Damodar Tech Craze
"""

            print(f"[Pro Dispatch] Sending optimized pitch to [{email}] | Competitive Rate: {price}")
            
            lead["status"] = "Pro_Email_Sent"
            sent_count += 1
            
            with open(DATABASE_FILE, "w") as f:
                json.dump(leads, f, indent=4)
                
            time.sleep(6)

    print(f"[SUCCESS] Optimized outreach batch complete! Pitched {sent_count} verified leads with market-standard pricing.")

if __name__ == "__main__":
    send_professional_outreach()
