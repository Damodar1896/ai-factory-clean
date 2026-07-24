import json
import os
from playwright.sync_api import sync_playwright

DATA_FILE = "secure_database.json"

def run_instagram_automation():
    # Path set kar rahe hain jahan database hai
    db_path = os.path.expanduser("~/ai-factory/secure_database.json")
    
    if not os.path.exists(db_path):
        print("[Error] Secure database not found!")
        return

    with open(db_path, "r") as f:
        profiles = json.load(f)

    print(f"\n[Info] Loaded {len(profiles)} profiles for Automation.")
    print("[Info] Initializing Stealth Browser for Social Automation...\n")

    with sync_playwright() as p:
        # Pehli profile utha kar test automation run karte hain
        profile = profiles[0]
        print(f"--- Automating Task for Profile: {profile['email']} ---")

        browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        page = context.new_page()

        try:
            # Instagram login page ya target landing page load kar rahe hain
            print("[Action] Navigating to Instagram...")
            page.goto("https://www.instagram.com/", timeout=60000)
            page.wait_for_timeout(5000)
            print(f"[Success] Instagram loaded successfully for profile {profile['email']}.")
        except Exception as e:
            print(f"[Error] Automation failed: {e}")

        browser.close()
        print("--- Automation Task Finished Successfully ---")

if __name__ == "__main__":
    print("--- Starting AI Factory Social Automation ---")
    run_instagram_automation()
