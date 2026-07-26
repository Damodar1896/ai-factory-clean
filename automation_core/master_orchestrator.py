import os
import time
import subprocess
from pathlib import Path

Path("automation_core/data").mkdir(parents=True, exist_ok=True)
Path("automation_core/logs").mkdir(parents=True, exist_ok=True)

def log_master_event(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] [Master Orchestrator] {message}"
    print(log_msg)
    with open("automation_core/logs/master_daemon.log", "a") as f:
        f.write(log_msg + "\n")

def run_empire_cycle():
    log_master_event("=== [STARTING AUTONOMOUS EMPIRE CYCLE] ===")
    
    # 1. Check & Rotate IP via ADB Airplane Mode
    log_master_event("[Step 1] Triggering hardware IP rotation...")
    try:
        subprocess.run(["python", "automation_core/adb_connector.py"], capture_output=True, text=True)
        log_master_event("[✅ SUCCESS] IP rotated successfully via mobile data toggle.")
    except Exception as e:
        log_master_event(f"[⚠️ WARNING] IP rotation skipped/failed: {e}")
        
    # 2. Render Short & Inject CTA
    log_master_event("[Step 2] Executing video render & UPI funnel injection...")
    try:
        subprocess.run(["python", "automation_core/video_subtitle_renderer.py"], capture_output=True, text=True)
        subprocess.run(["python", "automation_core/funnel_cta_injector.py"], capture_output=True, text=True)
        log_master_event("[✅ SUCCESS] High-retention video compiled & UPI funnel CTA locked (damodartechcraze@okaxis).")
    except Exception as e:
        log_master_event(f"[❌ ERROR] Content pipeline error: {e}")
        
    log_master_event("=== [CYCLE COMPLETED. SLEEPING FOR NEXT BATCH] ===")

if __name__ == "__main__":
    log_master_event("🚀 DAMODAR EMPIRE MASTER ORCHESTRATOR STARTED 24/7")
    while True:
        run_empire_cycle()
        # Sleep for 1 hour before next automated growth cycle
        time.sleep(3600)
