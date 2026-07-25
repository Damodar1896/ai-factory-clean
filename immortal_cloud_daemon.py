import os
import time
import subprocess
import sys
from datetime import datetime

# Cloud-Optimized Empire Services
CLOUD_SERVICES = [
    "scraper.py",
    "business_empire_master.py",
    "ai_personalizer.py",
    "smart_sales_engine.py",
    "smtp_dispatcher.py",
    "outreach_dispatcher_pro.py",
    "followup_engine.py",
    "payment_and_delivery_engine.py",
    "payment_delivery_bot.py",
    "ai_inbox_responder.py",
    "master_crm_tracker.py"
]

def cloud_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[CLOUD-DAEMON {timestamp}] {message}")

def run_cloud_empire():
    cloud_log("=== [DAMODAR CLOUD EMPIRE DEPLOYED & ACTIVE] Running 24x7 on Cloud (Zero Local Load) ===")
    while True:
        for service in CLOUD_SERVICES:
            if os.path.exists(service):
                try:
                    check = subprocess.run(f"pgrep -f {service}", shell=True, capture_output=True, text=True)
                    if not check.stdout.strip():
                        cloud_log(f"[☁️ CLOUD HEALING] Service '{service}' restarted on cloud instance.")
                        subprocess.Popen(f"{sys.executable} {service}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                except Exception as e:
                    cloud_log(f"[❌ CLOUD ERROR on {service}]: {e}")
        time.sleep(30)

if __name__ == "__main__":
    run_cloud_empire()
