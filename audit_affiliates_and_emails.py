import os
import json

print("==================================================")
print("   DAMODAR EMPIRE: AFFILIATE & EMAIL VAULT AUDIT  ")
print("==================================================")

# 1. Check Email Vault File
vault_file = "persistent_email_vault.json"
if os.path.exists(vault_file):
    with open(vault_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        print(f"\n[📧 EMAIL VAULT STATS] (Total: {data.get('total', 0)})")
        logs = data.get("logs", [])
        # Last 5 generated corporate emails dikhane ke liye
        print("Recent 5 Generated Corporate Emails:")
        for idx, entry in enumerate(logs[-5:], 1):
            print(f"  {idx}. {entry.get('email')} | Status: {entry.get('status')} | Date: {entry.get('date', 'N/A')}")
else:
    print("\n[📧 EMAIL VAULT]: persistent_email_vault.json not found.")

# 2. Check Affiliate Swarm Execution File
affiliate_file = "affiliate_swarm_execution.json"
if os.path.exists(affiliate_file):
    with open(affiliate_file, "r", encoding="utf-8") as f:
        aff_data = json.load(f)
        partnerships = aff_data.get("partnerships", [])
        print(f"\n[💰 AFFILIATE SIGN-UPS STATS] (Total Locked: {len(partnerships)})")
        if partnerships:
            for idx, item in enumerate(partnerships, 1):
                print(f"  {idx}. Network: {item.get('network_name')}")
                print(f"     • Email Used: {item.get('corporate_email')}")
                print(f"     • Referral Link: {item.get('referral_link')}")
                print(f"     • Status: {item.get('status')}")
        else:
            print("  • Affiliate swarm execution file is present, but partnerships are currently populating or queued.")
else:
    print("\n[💰 AFFILIATE FILE]: affiliate_swarm_execution.json is initializing (Swarm engine running in background).")

print("==================================================")
