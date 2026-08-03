import time
import subprocess
import sys

print("==================================================")
print("   DAMODAR EMPIRE: 24x7 MILITARY DAEMON ACTIVE    ")
print("==================================================")

def run_daemon():
    while True:
        print(f"\n[DAEMON] Initiating military-grade delta check sweep at {time.ctime()}...")
        try:
            subprocess.run([sys.executable, "master_api_harvester.py"], check=True)
        except Exception as e:
            print(f"[DAEMON ALERT] Handled minor execution hiccup: {e}")
            
        print("[DAEMON] Sleeping securely for 30 minutes before next sweep...")
        time.sleep(1800)

if __name__ == "__main__":
    run_daemon()
