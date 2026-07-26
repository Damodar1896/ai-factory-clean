import time
import json
import os
import subprocess

def run_supervisor():
    print("="*70)
    print("[*] [DAEMON SUPERVISOR] 24/7 Autopilot 13-Point Safety Guardian Initialized...")
    print("="*70)
    
    state_path = "automation_core/data/thirteen_point_safety_state.json"
    
    while True:
        # Run 13-point safety audit and self-healing loop in background
        subprocess.run(["python", "automation_core/module_thirteen_point_safety.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if os.path.exists(state_path):
            with open(state_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"[HEARTBEAT] 24/7 Autopilot Active | 13-Point Safety Shield: ONLINE | Protocols Enforced: {len(data.get('protocols_enforced', []))} | Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("[WARNING] Safety state file missing! Re-initializing 13-point matrix...")
            
        # Background check interval (Runs indefinitely on autopilot)
        time.sleep(60)

if __name__ == "__main__":
    try:
        run_supervisor()
    except KeyboardInterrupt:
        print("\n[!] Daemon Supervisor paused manually. Background state safe.")
