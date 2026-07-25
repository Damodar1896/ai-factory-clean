import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

print(f"[*] Checking Supabase Configuration...")
print(f"    - URL: {url}")

try:
    supabase = create_client(url, key)
    # Test insertion to verify table and connection
    payload = {
        "email_account": "test_connection_user@securemail.com",
        "ip_address": "127.0.0.1",
        "status": "TABLE_VERIFICATION_RUN"
    }
    response = supabase.table("execution_logs").insert(payload).execute()
    print("[✅ Success] Table 'execution_logs' exists and data inserted successfully!")
except Exception as e:
    print(f"[!] Error or Missing Table: {str(e)}")
    print("[*] Please ensure you ran the SQL query in Supabase SQL Editor as shown in Method 1.")
