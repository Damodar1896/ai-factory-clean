import os
import json
import random
import time

class AutonomousContentPipeline:
    def __init__(self, brand_config_path="automation_core/config/branding/active_brand.json"):
        self.brand_config_path = brand_config_path
        self.load_brand_identity()

    def load_brand_identity(self):
        if os.path.exists(self.brand_config_path):
            with open(self.brand_config_path, "r", encoding="utf-8") as f:
                self.brand_data = json.load(f)
            print(f"[+] Content Pipeline linked to Active Brand: '{self.brand_data['assigned_brand']}' ({self.brand_data['selected_niche']})")
        else:
            self.brand_data = {
                "assigned_brand": "Capital Club",
                "selected_niche": "FINANCE",
                "default_hooks": ["The silent asset allocation strategy of generational dynasties..."]
            }
            print("[WARNING] Active brand config not found. Loaded default fallback identity.")

    def generate_viral_payload(self):
        hook = random.choice(self.brand_data.get("default_hooks", ["They are hiding this from you..."]))
        
        payload = {
            "brand_name": self.brand_data["assigned_brand"],
            "niche": self.brand_data["selected_niche"],
            "viral_hook": hook,
            "estimated_rpm": self.brand_data.get("estimated_rpm", "$30 - $60"),
            "posting_jitter_delay": random.randint(120, 900), # Randomized human-like jitter in seconds
            "affiliate_embedded": True,
            "status": "ready_for_cloud_render"
        }
        
        output_path = "automation_core/data/viral_payload.json"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4)
            
        print(f"[+] Viral Content Payload generated successfully with Hook: '{hook}'")
        return payload

if __name__ == "__main__":
    pipeline = AutonomousContentPipeline()
    pipeline.generate_viral_payload()
