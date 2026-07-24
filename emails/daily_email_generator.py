import json
import os
from faker import Faker

fake = Faker()
DATA_FILE = "secure_database.json"

def generate_daily_batch(count=5):
    db_path = os.path.expanduser(f"~/ai-factory/{DATA_FILE}")
    
    if os.path.exists(db_path):
        with open(db_path, "r") as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    new_profiles = []
    print(f"\n[Info] Generating a fresh batch of {count} automated email profiles...")

    for _ in range(count):
        profile = {
            "name": fake.name(),
            "email": f"{fake.user_name()}@outlook.com",
            "password": fake.password(length=14, special_chars=True, digits=True),
            "status": "Fresh_Generated_And_Ready"
        }
        new_profiles.append(profile)
        print(f"[Generated New Email] {profile['email']}")

    existing_data.extend(new_profiles)
    
    with open(db_path, "w") as f:
        json.dump(existing_data, f, indent=4)

    print(f"\n[Done] Successfully added {count} new profiles. Total active database size: {len(existing_data)}")

if __name__ == "__main__":
    print("--- Starting AI Factory Daily Email Generator ---")
    generate_daily_batch(5)
