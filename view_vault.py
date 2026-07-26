import json, os

def view_email_vault():
    vault_file = "persistent_email_vault.json"
    if os.path.exists(vault_file):
        with open(vault_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        print("=" * 50)
        print("         DAMODAR EMPIRE: EMAIL VAULT STATUS       ")
        print("=" * 50)
        print(f"Total Emails in Vault : {data.get("total", 0)}")
        print(f"Generated Today       : {data.get("today", 0)}")
        print(f"Vault File Path       : {os.path.abspath(vault_file)}")
        print("-" * 50)
        print("Generated Corporate Emails List:")
        logs = data.get("logs", [])
        for idx, entry in enumerate(logs, 1):
            print(f"  {idx}. {entry.get("email")}  [{entry.get("status")}]")
        print("=" * 50)
    else:
        print("[INFO] persistent_email_vault.json not found yet.")

if __name__ == "__main__":
    view_email_vault()
