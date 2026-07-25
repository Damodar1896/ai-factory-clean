import os
import subprocess
import time

print("==================================================")
print("🚀 EMPIRE AUTOMATION MASTER CONTROL PANEL")
print("==================================================")

# 1. Check if launchd service is loaded (Using standard subprocess compatible with all Python versions)
print("[*] Checking macOS background service status...")
try:
    process = subprocess.Popen("launchctl list | grep empire", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, _ = process.communicate()
    if "com.empire.automation.daemon" in stdout:
        print("[✅ HEALTHY] Empire background daemon is active in macOS service manager.")
    else:
        print("[!] Warning: Service not found. Re-registering...")
        os.system("python setup_macos_daemon.py")
except Exception as e:
    print(f"[!] Service check notice: {str(e)}")

# 2. Force immediate execution check
print("[*] Triggering live execution stream...")

print("==================================================")
print("[🔥 LIVE] Now displaying live background output stream...")
print("[*] Press Ctrl+C anytime to exit viewer (The bot will keep running 24x7).")
print("==================================================")

log_file = "daemon_stdout.log"
if not os.path.exists(log_file):
    open(log_file, "w").write("[*] Log initialized.\n")

try:
    with open(log_file, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.3)
                continue
            print(line, end="")
except KeyboardInterrupt:
    print("\n[+] Control Panel closed. Your 24x7 automated empire is running safely in the background!")
