import json
import os
from playwright.sync_api import sync_playwright

DATA_FILE = "secure_database.json"

def run_profiles():
    if not os.path.exists(DATA_FILE):
        print("[Error] Database file not found!")
        return

    with open(DATA_FILE, "r") as f:
        profiles = json.load(f)

    print(f"\n[Info] Total Profiles in Database: {len(profiles)}")
    print("[Info] Starting Stealth Profile Automation...\n")

    with sync_playwright() as p:
        for index, profile in enumerate(profiles[:3]):  # Pehle 3 profiles test karte hain
            print(f"--- Running Stealth Automation for Profile #{index+1}: {profile['email']} ---")
            
            # Headless=False rakha hai taaki aapko browser dikhe
            browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
            
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                viewport={"width": 1280, "height": 800}
            )
            
            page = context.new_page()
            
            try:
                # Bot-detection se bachne ke liye safe and stable site use kar rahe hain
                page.goto("https://ipinfo.io/json", timeout=60000)
                page.wait_for_timeout(4000) # 4 seconds wait
                print(f"[Success] Profile {profile['email']} loaded stealth page successfully.")
            except Exception as e:
                print(f"[Error] Failed for {profile['email']}: {e}")
            
            browser.close()
            print(f"--- Finished Profile #{index+1} ---\n")

if __name__ == "__main__":
    run_profiles()
