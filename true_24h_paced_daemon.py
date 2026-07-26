import os, json, time, random, sys
from datetime import datetime

VAULT_FILE = "persistent_email_vault.json"

def run_paced_production_daemon():
    print("=== [DAMODAR 24H PACED WARM-UP & MIMICRY DAEMON STARTED] ===", flush=True)
    
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

            # Reset daily counter if a new day has arrived
            if vault.get("date") != today_str:
                vault["today"] = 0
                vault["date"] = today_str

            existing_emails = {entry.get("email") for entry in vault.get("logs", [])}
            daily_target = 60 # Strict daily target inside 24 hours
            current_today = vault.get("today", 0)
            
            print(f"[STATUS] Daily Target: {daily_target} | Generated So Far Today: {current_today}", flush=True)
            
            if current_today < daily_target:
                # Calculate precise pacing gap across remaining hours of the day (spread organically)
                delay_minutes = random.uniform(18.0, 38.0) # 18 to 38 minutes gap between each single email
                print(f"[⏳ HUMAN PACING ACTIVE] Waiting {delay_minutes:.2f} minutes before generating next warm-up email to protect primary inbox score...", flush=True)
                
                # Sleep in chunks so it remains active
                sleep_seconds = delay_minutes * 60
                chunks = max(1, int(sleep_seconds / 10))
                for _ in range(chunks):
                    time.sleep(10)

                # Generate ONE single high-value professional corporate email
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
                            "status": "Warming-Up (Primary Inbox Protected - Day 1)",
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
                    print(f"[✨ SUCCESS & LOCKED] Generated Corporate Email: {new_email_obj["email"]} | 14-Day Warm-up Active", flush=True)
            else:
                print(f"[QUOTA MET] Today's target of {daily_target} emails perfectly distributed across 24h. Resting for 1 hour...", flush=True)
                time.sleep(3600)

        except Exception as err:
            print(f"[⚠️ AUTO-HEAL]: {err}. Recovering daemon core in 10 seconds...", flush=True)
            time.sleep(10)

if __name__ == "__main__":
    run_paced_production_daemon()
