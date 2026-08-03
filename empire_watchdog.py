import time
import subprocess
import os
import datetime

WATCH_LIST = [
    {"name": "Empire Master Brain", "cmd": "python3 empire_master_brain.py", "dir": "/Users/shubhamdewangan/ai-factory"},
    {"name": "Master Autopilot", "cmd": "python3 master_autopilot.py", "dir": "/Users/shubhamdewangan/ai-factory/affiliate_bot"},
    {"name": "Permanent Empire Daemon", "cmd": "python3 permanent_empire_daemon.py", "dir": "/Users/shubhamdewangan/ai-factory"}
]

def log_msg(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [WATCHDOG] {msg}")

def is_running(script_name):
    try:
        output = subprocess.check_output(f"ps aux | grep {script_name} | grep -v grep", shell=True).decode()
        return len(output.strip()) > 0
    except:
        return False

if __name__ == "__main__":
    log_msg("--- INFINITE EMPIRE WATCHDOG & SELF-HEALING ENGINE INITIALIZED ---")
    while True:
        for item in WATCH_LIST:
            script_file = item["cmd"].split()[1]
            if not is_running(script_file):
                log_msg(f"[ALERT] {item['name']} is down! Restarting automatically...")
                launch_cmd = f"cd {item['dir']} && nohup {item['cmd']} > {script_file.split('.')[0]}_watchdog_live.log 2>&1 &"
                subprocess.run(launch_cmd, shell=True)
                log_msg(f"[RECOVERED] {item['name']} successfully restarted in background.")
        
        # Har 60 seconds mein poore empire ki health check karega
        time.sleep(60)
