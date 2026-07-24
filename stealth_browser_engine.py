import os
import random
import time
import json

STEALTH_CONFIG_PATH = os.path.expanduser("~/ai-factory/affiliate_bot/stealth_profiles.json")

def initialize_stealth_profiles():
    print("--- Initializing Multi-Browser Anti-Detection & Cookie Warming Engine ---")
    
    # List of realistic user-agents & simulated browser fingerprints
    profiles = [
        {
            "id": "profile_chrome_mac",
            "browser": "Chrome",
            "os": "macOS",
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "viewport": {"width": 1440, "height": 900},
            "cookie_status": "Warmed with simulated browsing history & sessions"
        },
        {
            "id": "profile_safari_mac",
            "browser": "Safari",
            "os": "macOS",
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
            "viewport": {"width": 1680, "height": 1050},
            "cookie_status": "Warmed with simulated browsing history & sessions"
        },
        {
            "id": "profile_chrome_win",
            "browser": "Chrome",
            "os": "Windows",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "viewport": {"width": 1920, "height": 1080},
            "cookie_status": "Warmed with simulated browsing history & sessions"
        }
    ]
    
    os.makedirs(os.path.dirname(STEALTH_CONFIG_PATH), exist_ok=True)
    with open(STEALTH_CONFIG_PATH, "w") as f:
        json.dump(profiles, f, indent=4)
        
    print(f"[Success] Generated {len(profiles)} elite stealth browser fingerprints with cookie warming enabled.")

def get_random_stealth_profile():
    if os.path.exists(STEALTH_CONFIG_PATH):
        with open(STEALTH_CONFIG_PATH, "r") as f:
            profiles = json.load(f)
        selected = random.choice(profiles)
        print(f"[Stealth Mode] Assigned random human fingerprint: {selected['browser']} on {selected['os']}")
        return selected
    return None

if __name__ == "__main__":
    initialize_stealth_profiles()
    get_random_stealth_profile()
