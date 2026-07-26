import subprocess
import time

def fast_rotate_ip():
    try:
        print(f"[*] [{time.strftime('%H:%M:%S')}] Fast IP Rotation: Turning Airplane Mode ON...")
        subprocess.run(["adb", "shell", "cmd", "connectivity", "airplane-mode", "enable"], check=True)
        
        # 3 second ka fast pause taaki network drop ho
        time.sleep(3)
        
        print(f"[*] [{time.strftime('%H:%M:%S')}] Fast IP Rotation: Turning Airplane Mode OFF...")
        subprocess.run(["adb", "shell", "cmd", "connectivity", "airplane-mode", "disable"], check=True)
        
        print(f"[SUCCESS] [{time.strftime('%H:%M:%S')}] IP Rotated Successfully!")
    except Exception as e:
        print(f"[ERROR] IP Rotation failed: {e}")

if __name__ == "__main__":
    print("=== [ADB AIRPLANE MODE CONTINUOUS ROTATOR ACTIVE] ===")
    while True:
        fast_rotate_ip()
        # Har 5 minutes (300 seconds) mein automatic IP rotation cycle chalega
        print("[*] Waiting 5 minutes for next IP rotation cycle...")
        time.sleep(300)
