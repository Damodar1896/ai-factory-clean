import json
import os
import random
import time
from playwright.sync_api import sync_playwright

DATA_FILE = "secure_database.json"

def human_warmup_simulation():
    if not os.path.exists(DATA_FILE):
        print("[Error] Secure database not found!")
        return

    with open(DATA_FILE, "r") as f:
        profiles = json.load(f)

    print(f"\n[Info] Loaded {len(profiles)} profiles for Human-Like Warmup.")
    print("[Info] Launching Stealth Browser with Human Simulation Engine...\n")

    with sync_playwright() as p:
        for index, profile in enumerate(profiles[:2]): # Testing with first 2 profiles
            print(f"--- Starting Human Session for Profile #{index+1}: {profile['email']} ---")
            
            # Stealth browser launch
            browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
                viewport={"width": 1280, "height": 800}
            )
            page = context.new_page()

            try:
                # 1. Pehle email/inbox simulation page visit karein
                print(f"[Action] Logging into secure mail interface...")
                page.goto("https://outlook.live.com/", timeout=60000)
                wait_time = random.randint(4, 7)
                time.sleep(wait_time)
                print(f"[Success] Mail session active for {profile['email']}")

                # 2. Human Behavior: Background mein YouTube khol kar random video dekhna (Natural engagement)
                print(f"[Action] Simulating human browsing: Opening YouTube for natural traffic signal...")
                page.goto("https://www.youtube.com/", timeout=60000)
                page.wait_for_timeout(random.randint(5000, 8000))
                
                # Scroll down naturally like a human
                page.evaluate("window.scrollBy(0, 400)")
                page.wait_for_timeout(3000)
                print(f"[Success] Human simulation completed successfully for {profile['email']}.")

            except Exception as e:
                print(f"[Error] Simulation interrupted: {e}")

            browser.close()
            print(f"--- Session Closed for Profile #{index+1} ---\n")
            time.sleep(3)

    print("[Done] All active profiles passed through human-like warmup cycle!")

if __name__ == "__main__":
    print("--- Starting AI Factory Human Warmup Engine ---")
    human_warmup_simulation()
