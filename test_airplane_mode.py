import subprocess
import time

def toggle_airplane_mode():
    print("[*] Enabling Airplane Mode...")
    subprocess.run(["adb", "shell", "cmd", "connectivity", "airplane-mode", "enable"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("[*] Waiting 3 seconds...")
    time.sleep(3)
    
    print("[*] Disabling Airplane Mode to refresh network...")
    subprocess.run(["adb", "shell", "cmd", "connectivity", "airplane-mode", "disable"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("[*] Waiting 7 seconds for network reconnection...")
    time.sleep(7)
    
    print("[+] IP cycle completed successfully!")

if __name__ == "__main__":
    toggle_airplane_mode()
