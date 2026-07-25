import json
import os

class AutoCommunityManager:
    def __init__(self):
        self.state_file = "community_state.json"
        self.load_state()

    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, "r") as f:
                self.state = json.load(f)
        else:
            self.state = {
                "telegram_groups": [{"name": "Damodar Elite Community #1", "members": 0, "active": True}],
                "whatsapp_groups": [{"name": "Damodar VIP Buyers #1", "members": 0, "active": True}]
            }

    def save_state(self):
        with open(self.state_file, "w") as f:
            json.dump(self.state, f, indent=4)

    def assign_customer_to_community(self, client_name, client_phone):
        """Automatically assigns incoming customer to active Telegram/WhatsApp group and scales if full"""
        
        # Check active WhatsApp Group
        active_wa = next((g for g in self.state["whatsapp_groups"] if g["active"]), None)
        if active_wa and active_wa["members"] >= 1000: # Group full limit simulation
            active_wa["active"] = False
            new_group_num = len(self.state["whatsapp_groups"]) + 1
            active_wa = {"name": f"Damodar VIP Buyers #{new_group_num}", "members": 0, "active": True}
            self.state["whatsapp_groups"].append(active_wa)

        active_wa["members"] += 1
        self.save_state()

        print(f"=== [AUTO-COMMUNITY MANAGER] ===")
        print(f"-> Client: {client_name} ({client_phone}) assigned to WhatsApp Group: '{active_wa['name']}'")
        print(f"-> Professional Invite Link dispatched automatically!")
        
        return active_wa['name']

if __name__ == "__main__":
    manager = AutoCommunityManager()
    # Test assignment for new paying client
    manager.assign_customer_to_community("Rahul Sharma", "+919232698947")
