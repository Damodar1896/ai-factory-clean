import os
import json
import time
import random
import subprocess
from datetime import datetime

class CorporateEmailEmpireEngine:
    def __init__(self, state_path="automation_core/data/generated_emails.json"):
        self.state_path = state_path
        self.log_path = "automation_core/logs/engine_execution.log"
        self._initialize_environment()

    def _initialize_environment(self):
        try:
            os.makedirs(os.path.dirname(self.state_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        except Exception as e:
            print(f"[CRITICAL ERROR] {e}")

    def log_event(self, message):
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.log_path, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {message}\n")
        except Exception:
            pass

    def toggle_mobile_airplane_mode(self):
        """Triggers Android ADB Airplane Mode ON/OFF loop to refresh residential IP per email."""
        try:
            print("[*] [ADB PROXY] Toggling Mobile Airplane Mode for Fresh IP...")
            subprocess.run(["adb", "shell", "settings", "put", "global", "airplane_mode_on", "1"], check=True)
            subprocess.run(["adb", "shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "true"], check=True)
            
            time.sleep(random.uniform(4.0, 6.0))
            
            subprocess.run(["adb", "shell", "settings", "put", "global", "airplane_mode_on", "0"], check=True)
            subprocess.run(["adb", "shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "false"], check=True)
            print("[SUCCESS] Residential IP successfully rotated via ADB.")
        except Exception as e:
            print(f"[WARNING] ADB hardware bridge skipped: {e}. Simulating IP rotation.")

    def human_mimicry_delay(self):
        """Strict non-linear human delay between individual email generation (15 to 45 mins)."""
        delay_seconds = random.randint(900, 2700) 
        minutes = delay_seconds / 60
        print(f"[*] [HUMAN-MIMICRY] Pausing for {minutes:.1f} minutes to ensure natural behavior...")
        time.sleep(delay_seconds)

    def execute_daily_quota(self):
        """Enforces a strict 50-70 email cap per 24-hour window, executing one-by-one with IP rotation and delays."""
        bases = ["damodartechcraze", "damodarventures", "techcrazeventures", "venturesdamodar", "techcrazedamodar", "damodardigital", "damodarcrazeventures", "damodarcore", "venturestechcraze", "damodarworks", "damodartechventures", "damodarempire", "venturesempire", "techcrazeempire", "teamdamodar", "damodarteam", "techcrazeteam", "venturesteam"]
        affixes = ["official", "global", "core", "hq", "group", "labs", "studio", "prime", "hub", "base", "works", "zone", "pro", "sys", "stack", "gen", "next", "apex", "elite", "cloud", "data", "ai", "net", "web", "app", "code", "port", "gate", "nexus", "axis", "nova", "orbit", "fusion", "realm", "empire", "vault", "hive", "desk", "support", "sales", "billing", "hr", "media", "press", "legal", "security", "admin", "partners", "team", "exec", "connect", "solutions", "corp"]
        
        excluded_emails = {"damodartechcraze@gmail.com", "damodarventures@gmail.com"}
        
        # Load existing state
        data = {"generated_emails": [], "last_reset_date": ""}
        if os.path.exists(self.state_path):
            try:
                with open(self.state_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                pass

        today_str = datetime.now().strftime("%Y-%m-%d")
        existing_emails = data.get("generated_emails", [])
        
        # Filter emails generated today to enforce strict 24-hour daily quota (50-70 max)
        todays_generated = [item for item in existing_emails if item.get("date") == today_str]
        
        target_daily_limit = random.randint(50, 70)
        print(f"[*] Daily Quota Status: {len(todays_generated)}/{target_daily_limit} generated today ({today_str}).")

        if len(todays_generated) >= target_daily_limit:
            print("[INFO] Daily quota reached. Pausing execution until tomorrow.")
            return

        # Generate exactly ONE email per cycle loop to apply per-action safety
        existing_set = {item["email"] for item in existing_emails}
        
        while True:
            base = random.choice(bases)
            affix = random.choice(affixes)
            pattern = random.choice(["prefix", "suffix"])
            
            candidate = f"{affix}{base}@gmail.com" if pattern == "prefix" else f"{base}{affix}@gmail.com"
            
            if candidate not in excluded_emails and candidate not in existing_set:
                # Execute individual safety protocols
                self.toggle_mobile_airplane_mode()
                
                new_entry = {
                    "email": candidate,
                    "date": today_str,
                    "timestamp": time.time()
                }
                existing_emails.append(new_entry)
                
                data["generated_emails"] = existing_emails
                with open(self.state_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)
                
                print(f"[SUCCESS] Generated & Secured Email: {candidate}")
                self.log_event(f"Generated corporate email: {candidate}")
                
                # Apply human mimicry delay after creation
                self.human_mimicry_delay()
                break

if __name__ == "__main__":
    CorporateEmailEmpireEngine().execute_daily_quota()
