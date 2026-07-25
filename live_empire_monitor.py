import time
import os

log_path = "daemon_stdout.log"
print("==================================================")
print("🚀 LIVE EMPIRE AUTOMATION MONITOR & 24x7 STATUS")
print("[-] Showing live background sync logs (Press Ctrl+C to exit monitor - bot will keep running)")
print("==================================================")

if not os.path.exists(log_path):
    with open(log_path, "w") as f:
        f.write("[*] Live monitor initialized log.\n")

try:
    with open(log_path, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            print(line, end="")
except KeyboardInterrupt:
    print("\n[+] Monitor closed. Background 24x7 empire service is still running safely in background!")
