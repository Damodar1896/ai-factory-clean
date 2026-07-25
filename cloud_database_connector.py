import os
import logging
import json

logging.basicConfig(
    filename="cloud_sync_production.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_env_file():
    env_path = ".env"
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            for line in f:
                if "=" in line and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value

def initialize_supabase_connection():
    print("[*] Initializing Cloud Database Connector...")
    load_env_file()
    
    supabase_url = os.environ.get("SUPABASE_URL")
    supabase_key = os.environ.get("SUPABASE_KEY")
    
    if not supabase_url or "your-project-id" in supabase_url:
        print("[!] Notice: Please update your actual Supabase credentials in the .env file.")
        return False
        
    if supabase_url and supabase_key:
        print(f"[+] Success! Cloud Database URL loaded: {supabase_url[:20]}...")
        logging.info("Supabase credentials loaded successfully.")
        return True
    else:
        print("[!] Error: Cloud Database keys missing.")
        return False

if __name__ == "__main__":
    initialize_supabase_connection()
