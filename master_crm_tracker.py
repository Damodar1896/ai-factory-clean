import json
import os
from datetime import datetime

class MasterCRMTracker:
    def __init__(self):
        self.leads_file = "crm_potential_leads.json"
        self.buyers_file = "crm_verified_buyers.json"
        self.loyal_file = "crm_loyal_customers.json"
        self.initialize_files()

    def initialize_files(self):
        for file_path in [self.leads_file, self.buyers_file, self.loyal_file]:
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    json.dump([], f, indent=4)
        print("[✅ CRM INITIALIZED] Customer tracking files are active and secured on your laptop.")

    def add_or_update_contact(self, name, phone, email, status="Lead", purchase_count=1):
        """
        Status types: 'Lead' (Potential), 'Buyer' (Customer), 'Loyal' (Repeat Customer)
        """
        target_file = self.leads_file
        if status == "Buyer":
            target_file = self.buyers_file
        elif status == "Loyal":
            target_file = self.loyal_file

        with open(target_file, "r") as f:
            contacts = json.load(f)

        # Check if contact already exists
        existing = next((c for c in contacts if c["phone"] == phone or c["email"] == email), None)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if existing:
            existing["purchase_count"] = existing.get("purchase_count", 1) + (1 if status in ["Buyer", "Loyal"] else 0)
            existing["last_updated"] = timestamp
            print(f"[🔄 CRM UPDATE] Updated contact: {name} ({status})")
        else:
            new_entry = {
                "name": name,
                "phone": phone,
                "email": email,
                "status": status,
                "purchase_count": purchase_count,
                "date_added": timestamp
            }
            contacts.append(new_entry)
            print(f"[➕ CRM ADDED] New {status} recorded: {name} | {phone} | {email}")

        with open(target_file, "w") as f:
            json.dump(contacts, f, indent=4)

if __name__ == "__main__":
    crm = MasterCRMTracker()
    # Test recording a potential lead
    crm.add_or_update_contact("Amit Verma", "+919876543210", "amit@targetbusiness.com", status="Lead")
    # Test recording a paying buyer
    crm.add_or_update_contact("Rahul Sharma", "+919232698947", "client@targetbusiness.com", status="Buyer", purchase_count=1)
    # Test recording a loyal repeat customer
    crm.add_or_update_contact("Priya Gupta", "+919988776655", "priya@enterprise.com", status="Loyal", purchase_count=3)
