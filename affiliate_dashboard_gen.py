import json

def register_affiliate_partner(partner_name, email):
    try:
        ref_code = f"DAMODAR-{partner_name[:4].upper()}-2026"
        aff_link = f"https://damodartechcraze.com/ref/{ref_code}"
        
        partner_profile = {
            "name": partner_name,
            "email": email,
            "referral_code": ref_code,
            "affiliate_link": aff_link,
            "commission_rate": "30%",
            "total_earnings": "₹0"
        }
        
        filename = f"affiliate_{partner_name.lower().replace(' ', '_')}.json"
        with open(filename, "w") as f:
            json.dump(partner_profile, f, indent=4)
            
        print(f"[✅ SUCCESS] Affiliate Partner Registered -> Name: {partner_name} | Unique Link: {aff_link}")
        return partner_profile
    except Exception as e:
        print(f"[!] Error registering affiliate: {e}")
        return None

if __name__ == "__main__":
    print("=== [SETTING UP MODULE 8: AFFILIATE DASHBOARD] ===")
    register_affiliate_partner("Suresh Kumar", "suresh@affiliate.com")
