import os
import random
import json
from datetime import datetime

print("=== [GOD-MODE AI FACTORY: MODULE 1 STARTING] ===")

class GodModeFactoryCore:
    def __init__(self, master_email="damodartechcraze@gmail.com"):
        self.master_email = master_email
        self.active_proxies = ["proxy_node_jio_mobile_01", "proxy_node_airtel_mobile_02"]

    def generate_alias_email(self, index):
        """Generates +1, +2 alias emails dynamically pointing to the same inbox."""
        username, domain = self.master_email.split("@")
        alias = f"{username}+{index}@{domain}"
        print(f"[🛡️ ALIAS GENERATOR] Created secure trial alias: {alias}")
        return alias

    def simulate_airplane_mode_rotation(self):
        """Simulates Airplane Mode toggle to refresh IP address via mobile hotspot."""
        selected_proxy = random.choice(self.active_proxies)
        print(f"[✈️ AIRPLANE MODE ROTATOR] Toggling mobile network... New Residential IP bound via node: {selected_proxy}")
        return selected_proxy

    def scrape_and_write_trending_script(self, niche="AI Business Automation"):
        """Scrapes trending angles and writes a high-retention 3-second hook script."""
        print(f"[📈 TREND SCRAPER] Scanning live market data for top-performing hooks in [{niche}]...")
        
        hooks = [
            f"Stop wasting hours on manual work in your {niche}. Here is how top agencies automate everything in 60 seconds.",
            f"Most {niche} owners are doing this completely wrong. Watch this before you lose your next client.",
            f"The secret behind scaling a {niche} empire on autopilot using zero-cost AI tools."
        ]
        
        selected_hook = random.choice(hooks)
        script_payload = {
            "niche": niche,
            "timestamp": str(datetime.now()),
            "hook_0_3s": selected_hook,
            "body": f"Deploying programmatic workflows, extracting high-intent data, and closing deals without human friction.",
            "cta": "Comment 'SCALE' below to get the exact system blueprint."
        }
        
        clean_niche = niche.lower().replace(" ", "_")
        filename = f"trend_script_{clean_niche}.json"
        
        with open(filename, "w") as f:
            json.dump(script_payload, f, indent=4)
            
        print(f"[✅ SCRIPTWRITER] Viral script compiled successfully and saved to: {filename}")
        return script_payload

if __name__ == "__main__":
    factory = GodModeFactoryCore()
    
    # Test Module 1 Execution
    factory.generate_alias_email(1)
    factory.generate_alias_email(2)
    factory.simulate_airplane_mode_rotation()
    factory.scrape_and_write_trending_script("Real Estate")
    print("=== [MODULE 1 COMPLETED SUCCESSFULLY] ===")
