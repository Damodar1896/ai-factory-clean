import subprocess
import time
import logging

logging.basicConfig(
    filename="empire_autopilot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def toggle_airplane_mode():
    try:
        logging.info("[*] Enabling Airplane Mode...")
        subprocess.run(["adb", "shell", "cmd", "connectivity", "airplane-mode", "enable"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        time.sleep(3)
        
        logging.info("[*] Disabling Airplane Mode to refresh network IP...")
        subprocess.run(["adb", "shell", "cmd", "connectivity", "airplane-mode", "disable"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        time.sleep(7)
        logging.info("[+] IP cycle completed successfully.")
    except Exception as e:
        logging.error(f"[!] Error during IP cycling: {str(e)}")

def start_continuous_autopilot(interval_minutes=10):
    print(f"[*] Continuous Autopilot Engine Started.")
    print(f"[*] IP will automatically cycle every {interval_minutes} minutes. Press Ctrl+C to stop.")
    logging.info("Continuous Autopilot Engine Started.")
    
    while True:
        try:
            print("\n----------------------------------------")
            print("[*] Running scheduled IP refresh cycle...")
            toggle_airplane_mode()
            print(f"[*] Next IP cycle in {interval_minutes} minutes...")
            print("----------------------------------------")
            
            time.sleep(interval_minutes * 60)
            
        except KeyboardInterrupt:
            print("\n[!] Autopilot stopped by user.")
            logging.info("Autopilot stopped by user.")
            break
        except Exception as e:
            print(f"[!] Unexpected error in main loop: {str(e)}")
            logging.error(f"Unexpected error in main loop: {str(e)}")
            time.sleep(30)

if __name__ == "__main__":
    START_INTERVAL_MINUTES = 10 
    start_continuous_autopilot(interval_minutes=START_INTERVAL_MINUTES)
