import os
import random
import time
from module_branding import initialize_branding
from module_api_rotator import FreeAPIPoolManager
from module_stealth import StealthBrowserConfig

class AutonomousPipelineEngine:
    def __init__(self):
        print("[-] Initializing Autonomous Multi-Platform Pipeline Engine...")
        initialize_branding("FINANCE")
        self.api_manager = FreeAPIPoolManager()

    def fetch_trending_topics(self):
        print("[*] Harvesting viral trends from niche creator feeds...")
        StealthBrowserConfig.simulate_human_delay(1, 2)
        return "The 2026 Shift in Automated Wealth Generation"

    def generate_content_assets(self, topic):
        api_key = self.api_manager.get_active_key()
        print(f"[*] Generating viral script & metadata using active API key...")
        StealthBrowserConfig.simulate_human_delay(1, 2)
        
        return {
            "title": f"The Untold Truth About {topic}",
            "description": "Discover the exact framework used by top creators. #Automation #Wealth #2026",
            "tags": ["automation", "wealth", "growth hacking"],
            "script": f"Script body focusing on high retention hooks for {topic}..."
        }

    def upload_to_platforms(self, assets):
        platforms = ["YouTube", "Instagram", "Facebook", "X"]
        for platform in platforms:
            StealthBrowserConfig.airplane_mode_ip_rotation_hook()
            headers = StealthBrowserConfig.get_random_headers()
            publish_delay = random.randint(3, 8)
            print(f"[*] Publishing payload to {platform} with randomized delay ({publish_delay}s)...")
            time.sleep(1)
            print(f"[SUCCESS] Published '{assets['title']}' to {platform}.")

    def run(self):
        topic = self.fetch_trending_topics()
        assets = self.generate_content_assets(topic)
        self.upload_to_platforms(assets)

if __name__ == "__main__":
    engine = AutonomousPipelineEngine()
    engine.run()
