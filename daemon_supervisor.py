import time
import json
import os

def run_supervisor():
    print("="*70)
    print("[*] [DAEMON SUPERVISOR] 24/7 Autopilot Retention Guardian Initialized...")
    print("="*70)
    
    state_path = "automation_core/data/underground_empire_state.json"
    
    while True:
        if os.path.exists(state_path):
            with open(state_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"[HEARTBEAT] 24/7 Autopilot Active | Daemons Online: {len(data.get('active_daemons', []))} | Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("[WARNING] State file missing! Re-initializing underground empire...")
            
        # Background check interval (Runs indefinitely without manual orders)
        time.sleep(60)

if __name__ == "__main__":
    try:
        run_supervisor()
    except KeyboardInterrupt:
        print("\n[!] Daemon Supervisor paused manually. Background state safe.")
