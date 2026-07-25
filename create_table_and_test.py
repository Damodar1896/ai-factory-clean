import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

print("[*] Connecting to Supabase to auto-create table and test...")
supabase = create_client(url, key)

# Table creation via PostgREST / RPC or direct insertion test hint
# Since Supabase client via REST API can't run raw DDL 'CREATE TABLE' directly without an RPC function,
# let's use Supabase REST endpoint or provide the exact SQL to execute, OR we can use psycopg2 if installed.
# But wait, let's make it bulletproof: we will use python to test inserting, 
# and if table is missing, we will use the PostgreSQL direct connection string if available, 
# or log the exact table creation step.

try:
    # Try inserting a test log
    payload = {
        "email_account": "empire_master_bot@securemail.com",
        "ip_address": "Mobile-Residential-IP",
        "status": "LIVE_PRODUCTION_VERIFIED"
    }
    response = supabase.table("execution_logs").insert(payload).execute()
    print("[✅ SUCCESS] Data successfully inserted into 'execution_logs'!")
    print(response)
except Exception as e:
    print(f"[!] Notice: {str(e)}")
    print("\n--------------------------------------------------")
    print("ACTION REQUIRED (Ek chota sa kaam karna hai):")
    print("1. Apne Supabase Dashboard par jao: https://supabase.com/dashboard")
    print("2. Apne project par click karke left menu se 'SQL Editor' kholo.")
    print("3. 'New query' par click karke niche diya hua code paste karo aur 'RUN' daba do:")
    print("--------------------------------------------------")
    print("""
create table if not exists execution_logs (
    id serial primary key,
    email_account text,
    ip_address text,
    status text,
    created_at timestamp default now()
);
    """)
    print("--------------------------------------------------")

