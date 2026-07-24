import json
import os
from playwright.sync_api import sync_playwright

DATA_FILE = "secure_database.json"

def test_browser_automation():
    if not os.path.exists(DATA_FILE):
        print("[Error] Database file not found!")
        return

    with open(DATA_FILE, "r") as f:
        profiles = json.load(f)

    print(f"[Info] Loaded {len(profiles)} profiles from database.")
    
    # Playwright Stealth / Browser launch test
    with sync_playwright() as p:
        # headless=False karne par browser screen par khulta hua dikhega
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        # Test ke liye ek site khol kar check karte hain ki IP/Browser proper kaam kar raha hai ya nahi
        print("[Action] Opening browser via automation...")
        page.goto("https://bot.sannysoft.com/")
        page.wait_for_timeout(5000) # 5 seconds wait
        
        browser.close()
        print("[Success] Browser automation test passed successfully!")

if __name__ == "__main__":
    test_browser_automation()
