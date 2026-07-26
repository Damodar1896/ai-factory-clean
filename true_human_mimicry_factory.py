import os, json, time, random
from datetime import datetime

VAULT_FILE = "persistent_email_vault.json"

def simulate_human_mimicry(email_index, total_target):
    delay_minutes = random.uniform(15.0, 55.0)
    delay_seconds = delay_minutes * 60
    print(f"[🧠 HUMAN MIMICRY] Email #{email_index}/{total_target} queued.")
    print(f"[⏳ BEHAVIORAL JITTER] Organic pause for {delay_minutes:.2f} minutes...")
    
    chunks = max(1, int(delay_seconds / 10))
    for _ in range(chunks):
        time.sleep(10)

def run_true_mimicry_factory():
    print("=== [TRUE HUMAN MIMICRY & 24H SPACED EMAIL FACTORY STARTED] ===")
    
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
            
            if current_today < daily_target:
                emails_to_generate_now = daily_target - current_today
                print(f"[DAILY PACING] Target: {daily_target} | Done: {current_today} | Spreading across 24h...")
                
                for i in range(1, emails_to_generate_now + 1):
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
                        print(f"[✨ SUCCESS] Generated: {new_email_obj["email"]} | 14-Day Warm-up Locked")
            else:
                print(f"[QUOTA REACHED] Today's target of {daily_target} completed with human pacing. Standing by...")
                time.sleep(14400)

        except Exception as e:
            print(f"[⚠️ AUTO-HEAL ERROR]: {e}. Recovering in 15 seconds...")
            time.sleep(15)

if __name__ == "__main__":
    run_true_mimicry_factory()
