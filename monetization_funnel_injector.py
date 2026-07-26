import os, json

def inject_monetization_funnel():
    print("=== [MONETIZATION FUNNEL] Embedding Payment & Affiliate Hooks ===")
    
    funnel_data = {
        "upi_id": "damodar.business@okhdfcbank",
        "service_package": "Complete Digital Transformation & Lead Gen Setup",
        "pricing": "Rs. 4,999 / $65 only",
        "lead_magnet": "Free Python Automation Repository (Pinned in Comments)",
        "status": "Active & Embedded"
    }
    
    with open("monetization_funnel_config.json", "w") as f:
        json.dump(funnel_data, f, indent=4)
        
    print("[SUCCESS] Monetization Funnel locked into production queue!")

if __name__ == "__main__":
    inject_monetization_funnel()
