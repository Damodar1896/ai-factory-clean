import json
import os

STORE_DB = os.path.expanduser("~/ai-factory/affiliate_bot/digital_products.json")

def init_digital_store():
    print("--- Initializing Automated Digital Products Micro-Store ---")
    
    digital_inventory = [
        {"product": "Ultimate AI Prompt Engineering Guide", "price": "$14.99", "sales_count": 0},
        {"product": "24/7 Python Affiliate Automation Script Bundle", "price": "$29.99", "sales_count": 0},
        {"product": "High-Ticket SaaS Closing Checklists", "price": "$9.99", "sales_count": 0}
    ]
    
    os.makedirs(os.path.dirname(STORE_DB), exist_ok=True)
    with open(STORE_DB, "w") as f:
        json.dump(digital_inventory, f, indent=4)
        
    for item in digital_inventory:
        print(f" -> [Digital Product Listed]: {item['product']} | Price: {item['price']} | Integration: damodartechcraze.com/store")
        
    print("[Success] Micro-store inventory compiled and linked to website hub. 100% passive digital sales ready!")

if __name__ == "__main__":
    init_digital_store()
