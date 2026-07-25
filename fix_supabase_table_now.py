import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY") or os.environ.get("SUPABASE_SERVICE_KEY")

if not url or not key:
    print("[!] Error: Supabase credentials missing in .env")
else:
    print("[*] Connecting to Supabase to verify/create table...")
    try:
        supabase = create_client(url, key)
        # Test insert to check if table exists
        test_payload = {
            "email_account": "table_init_check@securemail.com",
            "ip_address": "127.0.0.1",
            "status": "TABLE_READY"
        }
        response = supabase.table("execution_logs").insert(test_payload).execute()
        print("[✅ SUCCESS] Table 'execution_logs' is fully active and working!")
    except Exception as e:
        print(f"[!] Notice: {str(e)}")
        print("[*] NOTE: If the table doesn't exist yet, please go to your Supabase Dashboard -> SQL Editor -> Run this command:")
        print("    create table if not exists execution_logs (id serial primary key, email_account text, ip_address text, status text, created_at timestamp default now());")

