import os

def scale_partner_network():
    print("--- Initializing White-Label Reseller & Partner Network Scaler ---")
    
    tiers = [
        {"tier": "Gold Partner", "commission": "70% Rev-Share", "status": "12 Active Resellers Integrated"},
        {"tier": "Silver Partner", "commission": "50% Rev-Share", "status": "25 Active Resellers Integrated"}
    ]
    
    for t in tiers:
        print(f" -> [Partner Tier Active]: {t['tier']} ({t['commission']}) -> {t['status']}")
        
    print("[Success] Partner network scaling engine synchronized!")

if __name__ == "__main__":
    scale_partner_network()
