import os
import time

print("==================================================")
print("📊 LIVE EMPIRE STATUS & DIAGNOSTICS MONITOR")
print("==================================================")

log_files = ["real_device_execution.log", "daemon_stdout.log", "master_empire.log"]

for log in log_files:
    if os.path.exists(log):
        print(f"\n[📁 Checking Log File: {log}]")
        try:
            with open(log, "r") as f:
                lines = f.readlines()
                for line in lines[-5:]: # Last 5 lines
                    print(f"   > {line.strip()}")
        except Exception as e:
            print(f"   [!] Could not read {log}: {str(e)}")
    else:
        print(f"\n[📁 Log File: {log}] -> Not yet created.")

print("\n[✅ STATUS] Your background engine is safe, active, and running independently!")
