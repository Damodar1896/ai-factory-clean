import os
import subprocess
import sys

def launch_daemon():
    print("[*] [AUTOPILOT ARCHITECT] Initializing 24/7 Background Daemon Launcher...")
    
    # Ensure log directory exists
    os.makedirs("automation_core/logs", exist_ok=True)
    
    # Kill any existing instances safely
    os.system("pkill -f daemon_supervisor.py")
    
    # Launch daemon in background using subprocess (Cross-platform and clean)
    log_file = open("automation_core/logs/daemon_output.log", "w")
    process = subprocess.Popen(
        [sys.executable, "daemon_supervisor.py"],
        stdout=log_file,
        stderr=log_file,
        stdin=subprocess.DEVNULL,
        start_new_session=True
    )
    
    print(f"[SUCCESS] 24/7 Autopilot Background Daemon launched successfully with PID: {process.pid}")
    print("[INFO] Empire is now running fully autonomously. Terminal can be closed safely.")

if __name__ == "__main__":
    launch_daemon()
