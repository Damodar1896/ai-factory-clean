import os, json, time, urllib.request, urllib.parse

# Configuration (Apna Telegram Bot Token aur Chat ID yahan daal sakte ho)
TELEGRAM_BOT_TOKEN = os.getenv("8844329469:AAGebHJye04B2iSQA99_jWvd-HB9N9Qqo44")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", “8720676587”)

VAULT_FILE = "persistent_email_vault.json"
AFFILIATE_LOG = "affiliate_swarm_execution.json"
STATE_TRACKER = "telegram_alert_state.json"

def send_telegram_alert(message):
    if TELEGRAM_BOT_TOKEN == "YOUR_BOT_TOKEN":
        print(f"[📱 TELEGRAM MOCK ALERT]: {message}", flush=True)
        return
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = urllib.parse.urlencode({"chat_id": TELEGRAM_CHAT_ID, "text": message}).encode("utf-8")
        req = urllib.request.Request(url, data=data)
        urllib.request.urlopen(req, timeout=10)
    except Exception as e:
        print(f"[⚠️ TELEGRAM ERROR]: {e}", flush=True)

def run_notifier_daemon():
    print("=== [DAMODAR TELEGRAM EMPIRE NOTIFIER DAEMON STARTED] ===", flush=True)
    
    # Load last known state
    last_email_count = 0
    last_affiliate_count = 0
    if os.path.exists(STATE_TRACKER):
        with open(STATE_TRACKER, "r", encoding="utf-8") as f:
            state = json.load(f)
            last_email_count = state.get("email_count", 0)
            last_affiliate_count = state.get("affiliate_count", 0)

    while True:
        try:
            # 1. Check Email Vault Updates
            if os.path.exists(VAULT_FILE):
                with open(VAULT_FILE, "r", encoding="utf-8") as f:
                    vault = json.load(f)
                    logs = vault.get("logs", [])
                    current_email_count = len(logs)
                    
                    if current_email_count > last_email_count:
                        new_ones = logs[last_email_count:]
                        for item in new_ones:
                            msg = f"✨ [DAMODAR EMPIRE] New Corporate Email Generated!\n📧 Email: {item.get("email")}\n🛡️ Status: {item.get("status")}"
                            send_telegram_alert(msg)
                        last_email_count = current_email_count

            # 2. Check Affiliate Partnerships Updates
            if os.path.exists(AFFILIATE_LOG):
                with open(AFFILIATE_LOG, "r", encoding="utf-8") as f:
                    aff_data = json.load(f)
                    partnerships = aff_data.get("partnerships", [])
                    current_affiliate_count = len(partnerships)
                    
                    if current_affiliate_count > last_affiliate_count:
                        new_affs = partnerships[last_affiliate_count:]
                        for item in new_affs:
                            msg = f"💰 [DAMODAR AFFILIATE SWARM] Partnership Locked!\n🌐 Network: {item.get("network_name")}\n📧 Email: {item.get("corporate_email")}\n🔗 Link: {item.get("referral_link")}"
                            send_telegram_alert(msg)
                        last_affiliate_count = current_affiliate_count

            # Save state
            with open(STATE_TRACKER, "w", encoding="utf-8") as f:
                json.dump({"email_count": last_email_count, "affiliate_count": last_affiliate_count}, f, indent=4)

            time.sleep(60) # Poll every 60 seconds
        except Exception as err:
            print(f"[⚠️ NOTIFIER ERROR]: {err}", flush=True)
            time.sleep(30)

if __name__ == "__main__":
    run_notifier_daemon()
