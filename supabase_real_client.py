import os
import logging
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

logging.basicConfig(
    filename="supabase_real_sync.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_supabase_client() -> Client:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY") or os.environ.get("SUPABASE_SERVICE_KEY") or os.environ.get("SUPABASE_ANON_KEY")
    if not url or not key:
        raise ValueError("Supabase URL or Key missing from environment variables!")
    return create_client(url, key)

def insert_lead_to_cloud(email: str, ip: str, status: str):
    try:
        print("[*] Connecting to Supabase Client SDK...")
        supabase = get_supabase_client()
        
        # Data payload to insert into 'execution_logs' table
        payload = {
            "email_account": email,
            "ip_address": ip,
            "status": status
        }
        
        print(f"[*] Inserting record for {email} into cloud table...")
        
        # Note: Ensure you have an 'execution_logs' table created in your Supabase SQL Editor
        response = supabase.table("execution_logs").insert(payload).execute()
        
        print("[✅ Success] Data successfully written to Supabase cloud table!")
        logging.info(f"Inserted row successfully: {response}")
        return True
    except Exception as e:
        print(f"[!] Note on cloud write: {str(e)}")
        print("[*] (If table 'execution_logs' doesn't exist yet, create it in Supabase SQL editor)")
        logging.error(f"Cloud write exception: {str(e)}")
        return False

if __name__ == "__main__":
    insert_lead_to_cloud(
        email="empire_live_user_02@securemail.com",
        ip="Dynamic-Mobile-Residential-IP",
        status="ACTIVE_PRODUCTION_RUN"
    )
