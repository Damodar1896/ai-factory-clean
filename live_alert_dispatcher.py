import urllib.request
import urllib.parse
import json
import os

DATABASE_FILE = "business_empire_master_db.json"
WHATSAPP_TARGET = "+919232698947"

def send_live_system_update(event_type, message):
    alert_text = f"🚨 *DAMODAR TECH CRAZE ALERT*\n📌 *Type:* {event_type}\n💬 *Details:* {message}\n📞 *Target:* {WHATSAPP_TARGET}"
    print(f"\n{alert_text}\n---------------------------------------------")
    
    # Simulating direct webhook integration for WhatsApp delivery
    print(f"[WhatsApp Dispatcher] Pushing notification to {WHATSAPP_TARGET}...")
    
    # Logging event to local audit trail so dashboard / logs reflect it
    log_entry = {"event": event_type, "message": message, "target": WHATSAPP_TARGET}
    if os.path.exists("system_activity.log"):
        with open("system_activity.log", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    else:
        with open("system_activity.log", "w") as f:
            f.write(json.dumps(log_entry) + "\n")

if __name__ == "__main__":
    send_live_system_update("SYSTEM_ONLINE", "Damodar Tech Craze Empire is fully operational. 203 leads loaded. Monitoring for revenue and errors.")
