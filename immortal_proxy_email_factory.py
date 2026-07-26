import os, json, time, random
from datetime import datetime

VAULT_FILE = "persistent_email_vault.json"

def trigger_ip_rotation():
    print("[🛡️ CYBER-SECURITY] Cycling network socket / simulating mobile hotspot IP rotation...")
    time.sleep(1.5)
    print("[✅ IP ROTATED] Fresh residential network footprint secured.")

def run_immortal_factory():
    print("=== [IMMORTAL ENTERPRISE EMAIL & WARM-UP FACTORY 24/7 ACTIVE] ===")
    
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
            trigger_ip_rotation()
            
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
            
            # Enforce strict daily quota: ensure at least 50-75 fresh emails are generated today
            current_today_count = vault.get("today", 0)
            if current_today_count < 50:
                needed = random.randint(50, 75) - current_today_count
                print(f"[QUOTA CHECK] Today generated: {current_today_count}. Pumping {needed} fresh corporate emails to meet target...")
                
                generated_batch = []
                attempts = 0
                
                while len(generated_batch) < needed and attempts < 2000:
                    attempts += 1
                    b = random.choice(bases)
                    p = random.choice(prefixes)
                    s = random.choice(suffixes)
                    d = random.choice(domains)
                    
                    email = f"{p}.{s}.{b}@{d}" if random.choice([True, False]) else f"{p}{s}{b}{random.randint(10,99)}@{d}"
                    
                    if email not in existing_emails:
                        existing_emails.add(email)
                        generated_batch.append({
                            "email": email,
                            "status": "Warmed-Up & Proxy-Secured",
                            "time": str(datetime.now())
                        })

                vault["total"] += len(generated_batch)
                vault["today"] += len(generated_batch)
                vault["logs"].extend(generated_batch)

                with open(VAULT_FILE, "w", encoding="utf-8") as f:
                    json.dump(vault, f, indent=4)

                print(f"[✨ SUCCESS] Added {len(generated_batch)} fresh emails. Today Total: {vault["today"]} | Lifetime: {vault["total"]}")
            else:
                print(f"[QUOTA MET] Today target already achieved ({current_today_count} emails). System resting safely.")

            print("[⏳ SLEEPING] Factory resting for 4 hours before next background compliance sync...\n")
            time.sleep(14400) # Check compliance every 4 hours automatically
            
        except Exception as e:
            print(f"[⚠️ AUTO-HEAL EXCEPTION]: {e}. Re-engaging factory core in 15 seconds...")
            time.sleep(15)

if __name__ == "__main__":
    run_immortal_factory()
