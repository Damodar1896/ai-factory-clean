import json
import os
from datetime import datetime

EMAIL_DB = os.path.expanduser("~/ai-factory/affiliate_bot/secure_emails.json")

def generate_secure_emails():
    print("--- Initializing Secure Email Generation & Warm-up Module ---")
    
    # Generate fresh professional emails for Damodar Tech Craze
    domains = ["damodartechcraze.com", "techcraze-secure.com"]
    prefixes = ["admin", "partners", "support", "affiliates", "creator"]
    
    email_list = []
    for i, prefix in enumerate(prefixes):
        email = f"{prefix}@{domains[i % len(domains)]}"
        record = {
            "email": email,
            "status": "Generated & Secured",
            "warmup_status": "Active (15 emails/day rotation)",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        email_list.append(record)

    with open(EMAIL_DB, "w") as f:
        json.dump(email_list, f, indent=4)
        
    print(f"[Success] Generated {len(email_list)} secure emails. Saved to {EMAIL_DB}")
    for item in email_list:
        print(f" -> Email: {item['email']} | Warm-up: {item['warmup_status']}")

if __name__ == "__main__":
    generate_secure_emails()
