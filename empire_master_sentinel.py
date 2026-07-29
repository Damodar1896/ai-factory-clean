import os, json, time, subprocess
from datetime import datetime

LOG_FILE = "empire_master_sentinel.log"

def log_msg(msg):
    timestamp = str(datetime.now())
    line = f"[{timestamp}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def check_and_revive(process_name, script_file, log_output):
    # Check if process is running
    res = subprocess.run(["pgrep", "-f", script_file], capture_output=True, text=True)
    if not res.stdout.strip():
        log_msg(f"[⚠️ AUTO-HEAL] Process [{process_name}] ({script_file}) is down! Restarting...")
        try:
            cmd = f"nohup python3 -u {script_file} > {log_output} 2>&1 &"
            os.system(cmd)
            log_msg(f"[✅ RECOVERED] Successfully restarted [{process_name}].")
        except Exception as e:
            log_msg(f"[❌ ERROR RECOVERING {process_name}]: {e}")
    else:
        pass # Process is alive and healthy

def run_sentinel():
    log_msg("=== [DAMODAR EMPIRE MASTER SENTINEL STARTED] ===")
    
    # Managed Empire Daemons
    daemons = [
        ("Hardware ADB Paced Factory", "military_grade_adb_daemon.py", "military_adb.log"),
        ("Ultimate Affiliate Swarm Engine", "master_ultimate_affiliate_engine.py", "ultimate_affiliate.log"),
        ("Telegram Empire Notifier", "telegram_empire_notifier.py", "telegram_notifier.log"),
        ("Supabase Cloud Sync Bridge", "supabase_empire_sync.py", "supabase_sync.log")
    ]
    
    while True:
        try:
            for name, script, log in daemons:
                if os.path.exists(script):
                    check_and_revive(name, script, log)
            
            # Health check heartbeat every 2 minutes
            time.sleep(120)
        except Exception as err:
            log_msg(f"[⚠️ SENTINEL EXCEPTION]: {err}")
            time.sleep(15)

if __name__ == "__main__":
    run_sentinel()
