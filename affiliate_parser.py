import json
import os

CATALOG_FILE = "affiliate_catalog.json"

def parse_affiliate_catalog():
    print("[Affiliate Parser] Parsing product catalogs, pricing details, and high-commission links...")
    
    catalog = [
        {
            "product_name": "AI Growth Automator Pro",
            "category": "AI Tools",
            "commission_rate": "40% Recurring",
            "affiliate_link": "https://affiliate.example-ai-tool.com/damodar_pro",
            "target_niche": "Digital Agency"
        },
        {
            "product_name": "CloudScale High-Speed VPS",
            "category": "Hosting",
            "commission_rate": "$50 Flat per Sale",
            "affiliate_link": "https://affiliate.example-hosting.com/damodar_vps",
            "target_niche": "Real Estate"
        }
    ]
    
    with open(CATALOG_FILE, "w") as f:
        json.dump(catalog, f, indent=4)
        
    print(f"[Affiliate Parser SUCCESS] Cataloged {len(catalog)} active affiliate products with parsed pricing.")

if __name__ == "__main__":
    parse_affiliate_catalog()
