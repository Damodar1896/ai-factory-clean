import os
import json
import random

class CorporateEmailFactory:
    def __init__(self, vault_path="automation_core/config/credentials/email_vault.json"):
        self.vault_path = vault_path
        os.makedirs(os.path.dirname(self.vault_path), exist_ok=True)
        self.prefixes = ["damodartechcraze", "venturesdamodar", "techcrazedamodar"]
        self.departments = ["support", "sales", "admin", "corp", "hq", "official"]
        self.domains = ["gmail.com", "workspace-mail.com"]

    def generate_corporate_identities(self, count=5):
        vault_data = {"identities": []}
        
        for i in range(count):
            pref = random.choice(self.prefixes)
            dept = random.choice(self.departments)
            number = random.randint(10, 99)
            email = f"{pref}{dept}{number}@{random.choice(self.domains)}"
            
            identity = {
                "id": i + 1,
                "email": email,
                "status": "initialized",
                "warmup_day": 0,
                "linked_channels": []
            }
            vault_data["identities"].append(identity)

        with open(self.vault_path, "w", encoding="utf-8") as f:
            json.dump(vault_data, f, indent=4)
            
        print(f"[+] Successfully generated {count} elite corporate identities at: {self.vault_path}")
        return vault_data

if __name__ == "__main__":
    factory = CorporateEmailFactory()
    factory.generate_corporate_identities(5)
