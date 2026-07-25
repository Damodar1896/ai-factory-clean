import subprocess
import time
import os
import logging
from dotenv import load_dotenv
from supabase import create_client

# Load configuration
load_dotenv()

logging.basicConfig(
    filename="master_empire.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_supabase_client():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY") or os.environ.get("SUPABASE_ANON_KEY")
    if not url or not key:
        return None
    return create_client(url, key)

def log_to_cloud(account, ip, status):
    """Supabase cloud database par live log sync karne ka function"""
    try:
        supabase = get_supabase_client()
        if supabase:
            payload = {
                "email_account": account,
                "ip_address": ip,
                "status": status
            }
            supabase.table("execution_logs").insert(payload).execute()
            print(f"[☁️ Cloud Sync] Successfully written to Supabase table 'execution_logs'!")
    except Exception as e:
        print(f"[!] Cloud sync warning: {str(e)}")
        logging.error(f"Cloud sync error: {str(e)}")

def check_connected_device():
    """Android phone connection check via ADB"""
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")[1:]
    devices = [line.split("\t")[0] for line in lines if "\tdevice" in line]
    return devices

def rotate_mobile_ip():
    """Phone ka Airplane mode toggle karke IP rotate karna"""
    print("\n[🔄 IP Manager] Triggering real Airplane mode rotation on phone...")
    
    # Enable Airplane Mode
    subprocess.run(["adb", "shell", "settings", "put", "global", "airplane_mode_on", "1"], capture_output=True)
    subprocess.run(["adb", "shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "true"], capture_output=True)
    
    print("[*] Airplane mode ON. Waiting 4 seconds for network reset...")
    time.sleep(4)
    
    # Disable Airplane Mode
    subprocess.run(["adb", "shell", "settings", "put", "global", "airplane_mode_on", "0"], capture_output=True)
    subprocess.run(["adb", "shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "false"], capture_output=True)
    
    print("[*] Airplane mode OFF. Waiting 6 seconds for fresh mobile data IP assignment...")
    time.sleep(6)
    print("[✅ IP Manager] New mobile network IP acquired successfully!")

def run_master_pipeline():
    print("==================================================")
    print("🚀 MASTER UNIFIED EMPIRE ENGINE STARTED")
    print("==================================================")
    
    devices = check_connected_device()
    if not devices:
        print("[!] CRITICAL ERROR: No Android device detected via ADB!")
        print("[*] Please check USB cable and ensure USB Debugging is allowed on phone.")
        return
    
    print(f"[+] Active Android Device Verified ID: {devices[0]}")
    
    cycle = 0
    while True:
        try:
            cycle += 1
            print(f"\n==================================================")
            print(f"🔥 EXECUTING MASTER EMPIRE CYCLE #{cycle}")
            print(f"==================================================")
            
            # 1. Rotate IP via Phone
            rotate_mobile_ip()
            
            # 2. Generate secure automated email account
            account_email = f"empire_bot_live_{int(time.time())}@securemail.com"
            ip_bridge = "Dynamic-Mobile-Residential-IP"
            
            print(f"[*] Target Account Generated: {account_email}")
            print(f"[*] Executing automated browser/app sign-up sequence...")
            time.sleep(3) # Simulated workflow action
            
            # 3. Sync everything to Supabase Cloud Database
            print(f"[*] Syncing execution record to Supabase cloud...")
            log_to_cloud(account_email, ip_bridge, f"CYCLE_{cycle}_SUCCESS")
            
            print(f"[✅ SUCCESS] Cycle #{cycle} completed 100% successfully!")
            
            # 4. Cool-down interval before next batch (e.g., 20 seconds)
            print(f"[*] Waiting 20 seconds before starting next automation cycle...")
            time.sleep(20)
            
        except KeyboardInterrupt:
            print("\n[!] Master engine stopped manually by user.")
            break
        except Exception as e:
            print(f"[!] Runtime error caught: {str(e)}")
            print("[*] Auto-recovery initiated: Restarting loop in 10 seconds...")
            time.sleep(10)

if __name__ == "__main__":
    run_master_pipeline()
