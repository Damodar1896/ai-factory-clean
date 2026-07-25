import os
import json

print("==================================================")
print("🔔 EMPIRE LIVE NOTIFICATION & ALERT DIAGNOSTIC")
print("==================================================")

env_path = ".env"
telegram_configured = False

if os.path.exists(env_path):
    with open(env_path, "r") as f:
        content = f.read()
        if "TELEGRAM_BOT_TOKEN" in content or "TELEGRAM_CHAT_ID" in content:
            telegram_configured = True

if telegram_configured:
    print("[✅ FOUND] Telegram credentials found in environment.")
else:
    print("[!] Notice: Telegram Bot Token / Chat ID missing in .env configuration.")
    print("[*] To activate instant alerts, ensure TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are set.")

print("[*] Checking notification dispatch scripts...")
notifiers = ["owner_notifier.py", "live_alert_dispatcher.py", "config_telegram.py"]
for n in notifiers:
    status = "[✅ READY]" if os.path.exists(n) else "[❌ MISSING]"
    print(f"   - {n}: {status}")

print("==================================================")
