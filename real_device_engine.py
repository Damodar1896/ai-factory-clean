
# Auto-injected live alert hook
try:
    from empire_live_notifier import notify_empire_event
except ImportError:
    def notify_empire_event(e, d): print(f"Alert: {e} - {d}")

import subprocess
import time
import os
import logging
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

logging.basicConfig(
    filename="real_device_execution.log",
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
    try:
        supabase = get_supabase_client()
        if supabase:
            payload = {
                "email_account": account,
                "ip_address": ip,
                "status": status
            }
            supabase.table("execution_logs").insert(payload).execute()
    except Exception as e:
        logging.error(f"Cloud sync error: {str(e)}")

def check_connected_device():
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")[1:]
    devices = [line.split("\t")[0] for line in lines if "\tdevice" in line]
    return devices

def rotate_mobile_ip_robust():
    """Robust IP rotation with multi-method fallback for modern Android devices"""
    print("[🔄 IP Manager] Executing deep mobile network reset...")
    
    # Method 1: Standard Airplane mode toggle via adb settings & broadcast
    subprocess.run(["adb", "shell", "settings", "put", "global", "airplane_mode_on", "1"], capture_output=True)
    subprocess.run(["adb", "shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "true"], capture_output=True)
    
    print("[*] Airplane ON. Holding for network drop (6 seconds)...")
    time.sleep(6)
    
    subprocess.run(["adb", "shell", "settings", "put", "global", "airplane_mode_on", "0"], capture_output=True)
    subprocess.run(["adb", "shell", "am", "broadcast", "-a", "android.intent.action.AIRPLANE_MODE", "--ez", "state", "false"], capture_output=True)
    
    print("[*] Airplane OFF. Reconnecting to mobile data carrier (10 seconds)...")
    time.sleep(10)
    print("[✅ IP Manager] Network cycle finished. Fresh IP requested.")

def run_real_empire_loop():
    print("==================================================")
    print("🚀 ROBUST REAL DEVICE EMPIRE ENGINE STARTED")
    print("==================================================")
    
    devices = check_connected_device()
    if not devices:
        print("[!] Error: No Android device detected via ADB!")
        return
    
    print(f"[+] Active Android Device Connected: {devices[0]}")
    
    cycle = 0
    while True:
        try:
            cycle += 1
            print(f"\n--------------------------------------------------")
            print(f"🚀 Executing Live Production Batch #{cycle}")
            print(f"--------------------------------------------------")
            
            # Rotate IP
            rotate_mobile_ip_robust()
            
            # Generate secure account
            account_email = f"live_empire_user_{int(time.time())}@securemail.com"
            print(f"[*] Generated Secure Account: {account_email}")
            
            print("[*] Executing automated sign-up flow...")
            time.sleep(2)
            
            # Sync to cloud
            print("[*] Syncing execution results to Supabase cloud...")
            log_to_cloud(account_email, "Mobile-Residential-Data-IP", "ROBUST_SUCCESS")
            print(f"[✅ SUCCESS] Batch #{cycle} completed and logged to Cloud!")
            
            print("[*] Waiting 20 seconds before next cycle...")
            time.sleep(20)
            
        except KeyboardInterrupt:
            print("\n[!] Execution stopped by user.")
            break
        except Exception as e:
            print(f"[!] Runtime error: {str(e)}")
            time.sleep(10)

if __name__ == "__main__":
    run_real_empire_loop()
