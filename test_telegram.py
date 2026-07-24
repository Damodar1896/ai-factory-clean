import requests
from config_telegram import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def send_test_alert():
    if "APNA_BOT_TOKEN" in TELEGRAM_BOT_TOKEN or "APNI_CHAT_ID" in TELEGRAM_CHAT_ID:
        print("[Error] Pehle config_telegram.py mein apna real Token aur Chat ID daaliye!")
        return
        
    message = "🚀 Test Alert: Damodar Tech Empire Telegram Bot is live and connected successfully!"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("[Success] Telegram test message successfully sent to your phone!")
    else:
        print(f"[Failed] Error: {response.text}")

if __name__ == "__main__":
    send_test_alert()
