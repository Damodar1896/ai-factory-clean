import os
import time
import subprocess
import sys
from datetime import datetime

EMPIRE_SCRIPTS = [
    "scraper.py",
    "business_empire_master.py",
    "ai_personalizer.py",
    "affiliate_parser.py",
    "smart_sales_engine.py",
    "smtp_dispatcher.py",
    "outreach_dispatcher_pro.py",
    "followup_engine.py",
    "payment_and_delivery_engine.py",
    "payment_delivery_bot.py",
    "affiliate_engine.py",
    "ai_inbox_responder.py",
    "master_crm_tracker.py",
    "setup_professional_communities.py",
    "ai_voice_agent.py",
    "gst_invoice_generator.py",
    "lead_scoring_engine.py",
    "currency_switcher.py",
    "social_auto_scheduler.py",
    "churn_predictor.py",
    "affiliate_dashboard_gen.py",
    "cart_abandonment_bot.py",
    "mini_app_store.py"
]

LOG_FILE = "immortal_watchdog.log"

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] {message}"
    print(formatted_msg)
    try:
        with open(LOG_FILE, "a") as f:
            f.write(formatted_msg + "\n")
    except Exception:
        pass

def launch_immortal_engine():
    log_event("=== [IMMORTAL WATCHDOG INITIALIZED] Protecting Damodar Tech Craze Empire 24x7 ===")
    
    while True:
        for script in EMPIRE_SCRIPTS:
            if os.path.exists(script):
                try:
                    result = subprocess.run(f"pgrep -f {script}", shell=True, capture_output=True, text=True)
                    if not result.stdout.strip():
                        log_event(f"[🛡️ SELF-HEALING] Script '{script}' was inactive or crashed. Restarting instantly...")
                        subprocess.Popen(f"{sys.executable} {script}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                except Exception as e:
                    log_event(f"[❌ ERROR in Watchdog for {script}]: {e}")
        time.sleep(10)

if __name__ == "__main__":
    launch_immortal_engine()
