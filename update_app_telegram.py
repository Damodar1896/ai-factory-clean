import os

with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Add telegram import and trigger if not already present
if "send_instant_telegram_alert" not in content:
    helper_code = """
import requests
from config_telegram import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_instant_telegram_alert(name: str, email: str, message: str):
    try:
        text = f"🔥 New Lead Captured!\\n\\n👤 Name: {name}\\n📧 Email: {email}\\n💬 Message: {message}"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        print(f"[Telegram Alert Error]: {e}")
"""
    
    # Prepend helper code and insert background task in add_lead
    updated_content = helper_code + "\n" + content
    
    # Save back
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(updated_content)
    print("[Success] Telegram alert function injected into app.py!")
else:
    print("[Notice] Telegram alert function already present in app.py.")

if __name__ == "__main__":
    pass
