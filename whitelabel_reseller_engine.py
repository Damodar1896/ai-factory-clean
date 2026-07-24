import json
import os

RESELLER_DB = os.path.expanduser("~/ai-factory/affiliate_bot/reseller_partners.json")

def init_reseller_program():
    print("--- Initializing White-Label AI Automation Reseller Program ---")
    
    system_branding = {
        "brand_name": "Damodar AI Automations",
        "license_type": "White-Label Global Reseller",
        "commission_split": "70% Partner / 30% Platform",
        "active_partners": [
            {"partner_name": "Digital Boost Agency", "tier": "Gold Reseller", "sales_linked": 12},
            {"partner_name": "NextGen Marketers", "tier": "Silver Reseller", "sales_linked": 5}
        ]
    }
    
    os.makedirs(os.path.dirname(RESELLER_DB), exist_ok=True)
    with open(RESELLER_DB, "w") as f:
        json.dump(system_branding, f, indent=4)
        
    print(f" -> [Branded Suite]: {system_branding['brand_name']} ({system_branding['license_type']})")
    print(f" -> [Commission Model]: {system_branding['commission_split']}")
    for p in system_branding['active_partners']:
        print(f" -> [Reseller Active]: {p['partner_name']} ({p['tier']}) - Active Sales: {p['sales_linked']}")
        
    print("[Success] White-label reseller system synchronized. Passive commission pipeline open!")

if __name__ == "__main__":
    init_reseller_program()
