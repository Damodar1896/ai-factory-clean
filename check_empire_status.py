import os
import json
import subprocess
from datetime import datetime

def check_status():
    print("="*70)
    print("[*] [EMPIRE HEALTH MONITOR] Inspecting 24/7 Autopilot & Email Database...")
    print("="*70)

    # 1. Check background process (PID)
    print("\n--- 1. Background Daemon Status ---")
    try:
        ps_output = subprocess.check_output(["ps", "aux"], text=True)
        if "launch_autopilot_daemon.py" in ps_output or "corporate_email_empire_engine.py" in ps_output:
            print("[ONLINE] Autopilot daemon process is actively running in the background!")
        else:
            print("[WARNING] Background daemon process not found in active process list.")
    except Exception as e:
        print(f"[ERROR] Could not check process list: {e}")

    # 2. Check generated emails count and today's quota
    print("\n--- 2. Email Vault & Quota Audit ---")
    state_path = "automation_core/data/generated_emails.json"
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    if os.path.exists(state_path):
        try:
            with open(state_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            all_emails = data.get("generated_emails", [])
            todays_emails = [item for item in all_emails if item.get("date") == today_str]
            
            print(f"[*] Total Lifetime Emails Generated : {len(all_emails)}")
            print(f"[*] Generated Today ({today_str})   : {len(todays_emails)}")
            print(f"[*] Daily Quota Target              : 50 to 70 emails")
            
            if todays_emails:
                print("\n[-] Last 3 Generated Emails Today:")
                for entry in todays_emails[-3:]:
                    print(f"    -> {entry['email']}")
        except Exception as e:
            print(f"[ERROR] Failed to parse generated_emails.json: {e}")
    else:
        print("[!] Email vault file not created yet.")

    # 3. Check recent logs
    print("\n--- 3. Recent Execution Logs ---")
    log_path = "automation_core/logs/engine_execution.log"
    if os.path.exists(log_path):
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            for line in lines[-5:]:
                print(f"    {line.strip()}")
        except Exception:
            print("[!] Could not read execution logs.")
    else:
        print("[!] Execution log file not found yet.")

    print("="*70)

if __name__ == "__main__":
    check_status()
