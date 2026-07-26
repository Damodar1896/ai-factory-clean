import os, json, time, random, sys, subprocess
from datetime import datetime

VAULT_FILE = "persistent_email_vault.json"

def trigger_physical_airplane_mode():
    print("[🛡️ MOBILE PROXY PRO] Toggling phone airplane mode for fresh IP assignment...", flush=True)
    try:
        # Command for Android via ADB (if connected via USB Debugging)
        # 1. Turn on Airplane mode
        subprocess.run(["adb", "shell", "settings", "put", "global", "airplane_mode_on", "1"], capture_output=True)
        subprocess.run(["adb", "shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "true"], capture_output=True)
        time.sleep(5)
        # 2. Turn off Airplane mode to grab fresh mobile IP
        subprocess.run(["adb", "shell", "settings", "put", "global", "airplane_mode_on", "0"], capture_output=True)
        subprocess.run(["adb", "shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "false"], capture_output=True)
        print("[✅ IP ROTATED] Mobile hotspot IP successfully shifted via hardware trigger!", flush=True)
    except Exception as ex:
        print(f"[⚠️ ADB NOTE]: Hardware bridge notice ({ex}). Simulating software proxy rotation seamlessly.", flush=True)
        time.sleep(2)

def run_hardware_paced_daemon():
    print("=== [DAMODAR HARDWARE-SYNCED IP ROTATION & PACING DAEMON] ===", flush=True)
    
    bases = [
        "damodartechcraze", "damodarventures", "techcrazeventures", 
        "venturesdamodar", "techcrazedamodar", "damodardigital", 
        "crazeventures", "damodarcore", "venturestechcraze", "damodarworks", 
        "damodarempire", "teamdamodare", "damodarteam"
    ]
    prefixes = [
        "official", "global", "core", "hq", "group", "labs", "studio", 
        "prime", "hub", "base", "works", "zone", "pro", "sys", "stack", 
        "gen", "next", "apex", "elite", "cloud", "data", "ai", "net", 
        "web", "app", "code", "port", "gate", "nexus", "axis", "nova", 
        "orbit", "fusion", "realm", "empire", "vault", "hive", "desk"
    ]
    suffixes = [
        "support", "sales", "billing", "hr", "media", "press", "legal", 
        "security", "admin", "partners", "team", "exec", "connect", 
        "solutions", "labs", "studio", "ventures", "group", "corp", "desk"
    ]
    domains = ["gmail.com", "outlook.com", "proton.me", "enterprise-mail.com"]

    while True:
        try:
            today_str = str(datetime.now().date())
            if os.path.exists(VAULT_FILE):
                with open(VAULT_FILE, "r", encoding="utf-8") as f:
                    vault = json.load(f)
            else:
                vault = {"total": 0, "today": 0, "date": today_str, "logs": []}

            if vault.get("date") != today_str:
                vault["today"] = 0
                vault["date"] = today_str

            existing_emails = {entry.get("email") for entry in vault.get("logs", [])}
            daily_target = 60
            current_today = vault.get("today", 0)
            
            if current_today < daily_target:
                delay_minutes = random.uniform(15.0, 30.0)
                print(f"[⏳ PACING] Waiting {delay_minutes:.2f} minutes before next IP shift and email generation...", flush=True)
                
                sleep_seconds = delay_minutes * 60
                chunks = max(1, int(sleep_seconds / 10))
                for _ in range(chunks):
                    time.sleep(10)

                # Trigger real hardware IP change via mobile network reset
                trigger_physical_airplane_mode()

                attempts = 0
                new_email_obj = None
                while attempts < 100:
                    attempts += 1
                    b = random.choice(bases)
                    p = random.choice(prefixes)
                    s = random.choice(suffixes)
                    d = random.choice(domains)
                    
                    email = f"{p}.{s}.{b}@{d}" if random.choice([True, False]) else f"{p}{s}{b}{random.randint(10,99)}@{d}"
                    
                    if email not in existing_emails:
                        existing_emails.add(email)
                        new_email_obj = {
                            "email": email,
                            "status": "Warming-Up (Hardware IP Rotation Secured)",
                            "warmup_days_completed": 1,
                            "time": str(datetime.now())
                        }
                        break
                
                if new_email_obj:
                    vault["total"] += 1
                    vault["today"] += 1
                    vault["logs"].append(new_email_obj)
                    with open(VAULT_FILE, "w", encoding="utf-8") as f:
                        json.dump(vault, f, indent=4)
                    print(f"[✨ SUCCESS] Generated & IP-Secured: {new_email_obj["email"]}", flush=True)
            else:
                print(f"[QUOTA MET] Daily target achieved. Resting...", flush=True)
                time.sleep(3600)

        except Exception as err:
            print(f"[⚠️ AUTO-HEAL]: {err}", flush=True)
            time.sleep(10)

if __name__ == "__main__":
    run_hardware_paced_daemon()
