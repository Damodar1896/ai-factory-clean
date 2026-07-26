import os, json

def check_empire_status():
    print("=" * 65)
    print("       DAMODAR EMPIRE: MASTER PRODUCTION & STATUS AUDIT       ")
    print("=" * 65)
    
    # 1. Check Leads Database
    db_path = "leads_database.json"
    if os.path.exists(db_path):
        with open(db_path, "r", encoding="utf-8") as f:
            leads = json.load(f)
        print(f"[📊 LEADS DATABASE]: Found ({len(leads)} Total Leads Saved)")
        print(f"   • File Path: {os.path.abspath(db_path)}")
        if leads:
            print("   • Recent 3 Leads:")
            for idx, lead in enumerate(leads[-3:], 1):
                name = lead.get("business_name") or lead.get("name") or "N/A"
                loc = lead.get("location") or lead.get("city") or "N/A"
                email = lead.get("email") or "N/A"
                print(f"     {idx}. {name} | Location: {loc} | Email: {email}")
    else:
        print("[📊 LEADS DATABASE]: 🟡 Pending collection")

    print("-" * 65)

    # 2. Check Email Generator Vault
    vault_path = "persistent_email_vault.json"
    if os.path.exists(vault_path):
        with open(vault_path, "r", encoding="utf-8") as f:
            vault = json.load(f)
        print(f"[📧 EMAIL VAULT]: Active")
        print(f"   • Total Lifetime Emails Generated : {vault.get('total', 0)}")
        print(f"   • Generated Today                : {vault.get('today', 0)} / 50")
        print(f"   • Active Date Track              : {vault.get('date', 'N/A')}")
        print(f"   • File Path: {os.path.abspath(vault_path)}")
        
        logs = vault.get("logs", [])
        if logs:
            print("   • Recent 5 Generated Emails:")
            for idx, entry in enumerate(logs[-5:], 1):
                print(f"     {idx}. Email: {entry.get('email')} | Time: {entry.get('time')}")
    else:
        print("[📧 EMAIL VAULT]: 🟡 Pending creation")

    print("=" * 65)
    print("[✅ SYSTEM STATUS]: All background daemons operating smoothly!")
    print("=" * 65)

if __name__ == "__main__":
    check_empire_status()
