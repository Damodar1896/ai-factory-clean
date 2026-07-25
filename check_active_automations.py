import os

print("==================================================")
print("🤖 ACTIVE AUTOMATIONS & MODULES DIAGNOSTIC REPORT")
print("==================================================")

modules = {
    "1. Real Device & IP Rotation Engine": "real_device_engine.py",
    "2. 24x7 Permanent Background Daemon": "permanent_empire_daemon.py",
    "3. Master Unified Empire Engine": "master_empire_engine.py",
    "4. Cloud Database Connector": "supabase_real_client.py"
}

for name, filename in modules.items():
    status = "[✅ AVAILABLE / BUILT]" if os.path.exists(filename) else "[❌ MISSING]"
    print(f"{name}: {status}")

print("\n[📁 Recent Cloud Sync & Execution Logs Status]:")
log_files = ["real_device_execution.log", "daemon_stdout.log", "master_empire.log"]
for log in log_files:
    if os.path.exists(log):
        print(f"   - {log}: Active (Size: {os.path.getsize(log)} bytes)")
    else:
        print(f"   - {log}: Not active yet")

print("==================================================")
