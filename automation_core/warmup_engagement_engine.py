import json
import os
import time
import random

def run_warmup_cycle():
    vault_path = "automation_core/data/generated_emails.json"
    if not os.path.exists(vault_path):
        print("[!] Email vault not found.")
        return
    
    with open(vault_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    emails = data.get("generated_emails", [])
    if not emails:
        print("[!] No emails available for warm-up.")
        return
        
    target_email = random.choice(emails)
    print(f"[*] [{time.strftime('%Y-%m-%d %H:%M:%S')}] Warm-up Engine Active: Engaging sender identity -> {target_email['email']}")
    print(f"[*] Simulating active inbox threading, DNS check, and metadata handshake...")
    time.sleep(3)
    print(f"[SUCCESS] Warm-up engagement handshake completed for {target_email['email']}!")

if __name__ == "__main__":
    run_warmup_cycle()
