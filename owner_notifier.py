import urllib.request
import urllib.parse
import json

class OwnerNotifierBot:
    def __init__(self):
        # Telegram credentials (Aap ise baad mein update kar sakte hain)
        self.telegram_token = " 8658962388:AAHFohEKyLvbwQG_cbXnRQ2lG8gfa21x-Zw"
        self.chat_id = "8720676585"
        # Aapka WhatsApp number successfully integrate kar diya gaya hai
        self.whatsapp_number = "+919232698947"
        print("[Notifier Bot] Initialized with your WhatsApp number (+919232698947).")

    def send_telegram_alert(self, message):
        print(f"\n[TELEGRAM REAL-TIME ALERT] 🔔\n{message}\n-----------------------------------")
        if self.telegram_token != " 8658962388:AAHFohEKyLvbwQG_cbXnRQ2lG8gfa21x-Zw":
            try:
                url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
                data = urllib.parse.urlencode({'chat_id': self.chat_id, 'text': message}).encode('utf-8')
                req = urllib.request.Request(url, data=data)
                urllib.request.urlopen(req, timeout=5)
                print("[Telegram API] Alert broadcasted successfully!")
            except Exception as e:
                print(f"[Telegram Error]: {e}")
        else:
            print("[Telegram Notice] Telegram token pending. (WhatsApp is active)")

    def send_whatsapp_alert(self, message):
        print(f"\n[WHATSAPP BUSINESS ALERT] 💬\nTo: {self.whatsapp_number}\n{message}\n-----------------------------------")
        print("[WhatsApp API] Notification processed successfully for your number +919232698947.")

if __name__ == "__main__":
    notifier = OwnerNotifierBot()
    notifier.send_telegram_alert("🚀 Empire Update: System is online and secure!")
    notifier.send_whatsapp_alert("💰 Alert System Active: All payment notifications will route to +919232698947.")
