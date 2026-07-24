import time
import subprocess
import os
import sys
from datetime import datetime

LOG_PATH = os.path.expanduser("~/ai-factory/affiliate_bot/bulletproof_daemon.log")

def log_message(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted)
    try:
        with open(LOG_PATH, "a") as f:
            f.write(formatted + "\n")
    except Exception:
        pass

def run_autopilot():
    log_message("=== Bulletproof Email & Affiliate Autopilot Initialized ===")
    
    while True:
        try:
            log_message("Executing automated daily email rotation & warm-up sync...")
            engine_script = os.path.expanduser("~/ai-factory/affiliate_bot/daily_email_engine.py")
            
            # Run the engine securely with strict error capture
            result = subprocess.run(["python3", engine_script], capture_output=True, text=True, check=True)
            log_message(f"Execution Success: {result.stdout.strip()}")
            
        except subprocess.CalledProcessError as cpe:
            log_message(f"[Error] Subprocess failed with exit code {cpe.returncode}: {cpe.stderr.strip()}")
        except Exception as e:
            log_message(f"[Critical Exception] Self-healing activated. Error: {str(e)}")
            
        log_message("Autopilot resting for 2 hours before next stealth cycle...")
        try:
            time.sleep(7200) # 2 hours interval for safe pacing
        except KeyboardInterrupt:
            log_message("Manual shutdown requested. Exiting safely.")
            sys.exit(0)

if __name__ == "__main__":
    run_autopilot()
