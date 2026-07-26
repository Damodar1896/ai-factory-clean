import json
import os

state_path = "automation_core/data/generated_emails.json"

if os.path.exists(state_path):
    with open(state_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    emails = data.get("generated_emails", [])
    print("="*60)
    print(f"[*] Total Generated Emails in Vault: {len(emails)}")
    print("="*60)
    print("[-] Last 15 Generated Emails:")
    for idx, item in enumerate(emails[-15:], 1):
        print(f"    {idx}. {item['email']}  (Date: {item.get('date', 'N/A')})")
    print("="*60)
else:
    print("[!] Email vault file not found yet.")

if __name__ == "__main__":
    pass
