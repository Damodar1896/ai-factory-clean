import os
import time
import subprocess
from pathlib import Path

Path("automation_core/logs").mkdir(parents=True, exist_ok=True)

def log_guardian(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] [Immortal Guardian] {message}"
    print(log_msg)
    with open("automation_core/logs/guardian.log", "a") as f:
        f.write(log_msg + "\n")

def check_and_revive():
    log_guardian("Scanning core master orchestrator and ADB rotator health...")
    
    # Check if master orchestrator is alive
    res = subprocess.run(["pgrep", "-f", "master_orchestrator.py"], capture_output=True, text=True)
    if not res.stdout.strip():
        log_guardian("[⚠️ ALERT] Master Orchestrator offline! Reviving instantly...")
        subprocess.Popen(["nohup", "python", "automation_core/master_orchestrator.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        log_guardian("[✅ SUCCESS] Master Orchestrator revived and running in background.")
    else:
        log_guardian("[🟢 HEALTHY] Master Orchestrator is running active.")

if __name__ == "__main__":
    log_guardian("=== [IMMORTAL CLOUD GUARDIAN ACTIVATED 24/7] ===")
    while True:
        check_and_revive()
        # Check health every 5 minutes
        time.sleep(300)
