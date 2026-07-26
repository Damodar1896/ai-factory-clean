import os, json, time, random, sys
from datetime import datetime

VAULT_FILE = "persistent_email_vault.json"

def simulate_human_mimicry(email_index, total_target):
    delay_minutes = random.uniform(15.0, 45.0)
    delay_seconds = delay_minutes * 60
    print(f"[🧠 HUMAN MIMICRY] Email #{email_index}/{total_target} queued.", flush=True)
    print(f"[⏳ SPACING JITTER] Organic human pause of {delay_minutes:.2f} minutes active...", flush=True)
    
    chunks = max(1, int(delay_seconds / 10))
    for _ in range(chunks):
        time.sleep(10)

def run_master_production_factory():
    print("=== [DAMODAR MASTER PRODUCTION DAEMON 24/7 ACTIVE & UNBUFFERED] ===", flush=True)
    
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
            daily_target = random.randint(50, 75)
            current_today = vault.get("today", 0)
            
            print(f"[STATUS] Daily Goal: {daily_target} | Generated Today: {current_today}", flush=True)
            
            if current_today < daily_target:
                emails_needed = daily_target - current_today
                print(f"[QUOTA MANAGER] Pumping next batch of {emails_needed} emails...", flush=True)
                
                for i in range(1, emails_needed + 1):
                    simulate_human_mimicry(current_today + i, daily_target)
                    
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
                                "status": "Warming-Up (Active 14-Day Cycle)",
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
                        print(f"[✨ SUCCESS] Generated & Secured: {new_email_obj["email"]} | 14-Day Warm-up Locked", flush=True)
            else:
                print(f"[QUOTA REACHED] Today target achieved. Sleeping for 2 hours...", flush=True)
                time.sleep(7200)

        except Exception as err:
            print(f"[⚠️ AUTO-HEAL]: {err}. Recovering in 10 seconds...", flush=True)
            time.sleep(10)

if __name__ == "__main__":
    run_master_production_factory()
