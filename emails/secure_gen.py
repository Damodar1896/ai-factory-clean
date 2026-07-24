import os
import json
from faker import Faker

fake = Faker()
DATA_FILE = "secure_database.json"

def generate_secure_identities(count=5):
    os.makedirs(".", exist_ok=True)
    existing_data = []
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                existing_data = json.load(f)
        except Exception:
            existing_data = []

    new_identities = []
    for i in range(count):
        profile = {
            "name": fake.name(),
            "email": f"{fake.user_name()}@outlook.com",
            "password": fake.password(length=14, special_chars=True, digits=True),
            "status": "Ready_To_Automate"
        }
        new_identities.append(profile)
        print(f"[Success] Profile Created: {profile['email']}")

    existing_data.extend(new_identities)
    with open(DATA_FILE, "w") as f:
        json.dump(existing_data, f, indent=4)
        
    print(f"\n[Done] Total {len(new_identities)} profiles saved safely in {DATA_FILE}")

if __name__ == "__main__":
    print("--- Running Secure Identity Generator ---")
    generate_secure_identities(5)
