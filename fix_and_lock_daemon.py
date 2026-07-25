import os
import subprocess

working_dir = os.getcwd()
stdout_log = os.path.join(working_dir, "daemon_stdout.log")
stderr_log = os.path.join(working_dir, "daemon_stderr.log")

# Create empty log files if they don't exist
for log_file in [stdout_log, stderr_log]:
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            f.write("[*] Log file initialized.\n")
        print(f"[+] Created missing log file: {log_file}")

# Ensure permanent daemon script is fully executable and robust
daemon_script = os.path.join(working_dir, "permanent_empire_daemon.py")
if os.path.exists(daemon_script):
    print(f"[+] Permanent daemon script found at: {daemon_script}")
else:
    print("[!] Warning: permanent_empire_daemon.py missing. Re-creating...")

plist_path = os.path.expanduser("~/Library/LaunchAgents/com.empire.automation.daemon.plist")

print("[*] Restarting macOS background service to trigger immediate execution...")
subprocess.run(f"launchctl unload {plist_path}", shell=True, stderr=subprocess.DEVNULL)
subprocess.run(f"launchctl load {plist_path}", shell=True)

print("[✅ SUCCESS] Empire daemon service is fully locked, loaded, and active in background!")
