import os
import subprocess
import sys

def check_and_install_packages():
    print("[*] Checking required packages...")
    try:
        import dotenv
        import supabase
        print("[+] All required packages are already installed.")
    except ImportError:
        print("[!] Missing packages detected. Installing python-dotenv and supabase...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-dotenv", "supabase", "requests"])
        print("[+] Packages installed successfully!")

def fix_and_verify_env():
    print("[*] Validating .env configuration...")
    env_path = ".env"
    
    if not os.path.exists(env_path):
        print("[!] .env file not found! Creating default template...")
        with open(env_path, "w") as f:
            f.write("SUPABASE_URL=https://fhtverdbtmwjvgxlkmkz.supabase.co\n")
            f.write("SUPABASE_KEY=your_service_role_key_here\n")
        print("[!] Please update your keys in the .env file.")
        return False

    # Read and sanitize .env
    with open(env_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    url_fixed = False
    for line in lines:
        if line.startswith("SUPABASE_URL="):
            url_val = line.strip().split("=", 1)[1]
            # Agar user ne galti se postgresql:// connection string daal di hai, toh usko fix karke HTTPS URL bana do
            if "postgresql://" in url_val or "db." in url_val:
                # Extract project ref from db.REF.supabase.co
                try:
                    if "db." in url_val:
                        ref = url_val.split("db.")[1].split(".supabase.co")[0]
                        corrected_url = f"https://{ref}.supabase.co"
                    else:
                        corrected_url = "https://fhtverdbtmwjvgxlkmkz.supabase.co"
                    new_lines.append(f"SUPABASE_URL={corrected_url}\n")
                    url_fixed = True
                    print(f"[+] Auto-corrected Supabase URL to standard format: {corrected_url}")
                except Exception:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    if url_fixed:
        with open(env_path, "w") as f:
            f.writelines(new_lines)

    return True

def test_supabase_connection():
    from dotenv import load_dotenv
    from supabase import create_client

    load_dotenv()
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY") or os.environ.get("SUPABASE_ANON_KEY")

    print(f"[*] Connecting to Supabase Cloud...")
    print(f"    - URL: {url}")

    if not url or "your_service_role_key_here" in key or not key:
        print("[!] Error: Please put your actual Supabase Service Role Key in the .env file.")
        return False

    try:
        supabase = create_client(url, key)
        # Test query / insert attempt
        payload = {
            "email_account": "master_empire_bot@securemail.com",
            "ip_address": "Dynamic-Residential-IP",
            "status": "MASTER_SETUP_SUCCESS"
        }
        response = supabase.table("execution_logs").insert(payload).execute()
        print("[✅ SUCCESS] Connected to Supabase and data written to 'execution_logs' table successfully!")
        return True
    except Exception as e:
        print(f"[!] Database Connection / Table Notice: {str(e)}")
        print("[*] Note: If the error says table 'execution_logs' does not exist, please run the SQL query in Supabase SQL Editor.")
        return False

if __name__ == "__main__":
    print("========================================")
    print("🚀 STARTING MASTER EMPIRE ENVIRONMENT SETUP")
    print("========================================")
    check_and_install_packages()
    if fix_and_verify_env():
        test_supabase_connection()
    print("========================================")
    print("✨ Setup script execution completed.")
    print("========================================")
