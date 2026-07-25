import json
import os

class ProfessionalCommunityArchitect:
    def __init__(self):
        self.config_file = "professional_communities.json"
        self.initialize_structure()

    def initialize_structure(self):
        # Professional categories and names as requested
        structure = {
            "whatsapp_networks": {
                "vip_buyers": {"base_name": "Damodar VIP Buyers", "limit": 1024, "active_index": 1},
                "tech_craze_community": {"base_name": "Tech Craze Community", "limit": 1024, "active_index": 1}
            },
            "telegram_networks": {
                "elite_channel": {"base_name": "Damodar Tech Craze Elite Channel", "active_index": 1},
                "buyers_supergroup": {"base_name": "Tech Craze Buyers Supergroup", "active_index": 1}
            }
        }
        
        if not os.path.exists(self.config_file):
            with open(self.config_file, "w") as f:
                json.dump(structure, f, indent=4)
        print("[✅ SUCCESS] Professional community naming templates & architecture locked!")

    def generate_professional_invite(self, category, client_name):
        with open(self.config_file, "r") as f:
            data = json.load(f)
            
        if category == "buyer":
            net = data["whatsapp_networks"]["vip_buyers"]
            group_name = f"{net['base_name']} #{net['active_index']}"
            invite_link = f"https://chat.whatsapp.com/DamodarVIPBuyers{net['active_index']}SecureInvite"
        else:
            net = data["telegram_networks"]["buyers_supergroup"]
            group_name = f"{net['base_name']} #{net['active_index']}"
            invite_link = f"https://t.me/+DamodarTechCrazeBuyers{net['active_index']}"

        print(f"\n=== [PROFESSIONAL COMMUNITY ASSIGNMENT] ===")
        print(f"-> Client: {client_name}")
        print(f"-> Assigned Group/Channel: '{group_name}'")
        print(f"-> Secure Professional Link: {invite_link}")
        return invite_link

if __name__ == "__main__":
    architect = ProfessionalCommunityArchitect()
    architect.generate_professional_invite("buyer", "Rahul Sharma")
    architect.generate_professional_invite("telegram", "Rahul Sharma")
