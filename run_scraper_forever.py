import time
import subprocess

print("=== [LEADER SCRAPER 24/7 DAEMON STARTED] ===")
while True:
    try:
        print("\n[🔄 SCRAPER RESTART] Triggering fresh multi-city lead scraping batch...")
        subprocess.run(["python3", "lead_scraper.py"], check=True)
        print("[⏳ SLEEPING] Batch completed. Resting for 2 hours before next extraction cycle...\n")
        time.sleep(7200)
    except Exception as err:
        print(f"[⚠️ AUTO-HEAL TRIGGERED] Error: {err}. Re-engaging scraper in 15 seconds...")
        time.sleep(15)
