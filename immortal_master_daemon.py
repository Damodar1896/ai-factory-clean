import os, time, subprocess, sys
from datetime import datetime

SCRIPTS = [
    "scraper.py", "business_empire_master.py", "ai_personalizer.py", "affiliate_parser.py",
    "smart_sales_engine.py", "smtp_dispatcher.py", "outreach_dispatcher_pro.py", "followup_engine.py",
    "payment_and_delivery_engine.py", "payment_delivery_bot.py", "affiliate_engine.py", "ai_inbox_responder.py",
    "master_crm_tracker.py", "setup_professional_communities.py", "ai_voice_agent.py", "gst_invoice_generator.py",
    "lead_scoring_engine.py", "currency_switcher.py", "social_auto_scheduler.py", "churn_predictor.py",
    "affiliate_dashboard_gen.py", "cart_abandonment_bot.py", "mini_app_store.py"
]

def log(msg):
    line = f"[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] {msg}"
    print(line)
    try:
        with open("immortal_master.log", "a") as f: f.write(line + "\n")
    except: pass

log("=== [DAMODAR EMPIRE MASTER DAEMON ACTIVE 24x7] ===")
while True:
    for s in SCRIPTS:
        if os.path.exists(s):
            try:
                res = subprocess.run(f"pgrep -f {s}", shell=True, capture_output=True, text=True)
                if not res.stdout.strip():
                    log(f"[🛡️ SELF-HEALING] Restarting crashed component: {s}")
                    subprocess.Popen(f"{sys.executable} {s}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception as e:
                log(f"[❌ ERROR on {s}]: {e}")
    time.sleep(15)
