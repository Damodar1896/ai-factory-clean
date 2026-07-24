import subprocess
import time

def toggle_airplane_mode():
    print("[Network] -> Executing Realme 8 optimized IP rotation sequence...")
    try:
        # Method 1: Using modern connectivity command for Realme / Oppo / Android 11+
        subprocess.run(["adb", "shell", "cmd", "connectivity", "airplane-mode", "enable"], check=True)
        print("[Network] -> Airplane Mode ON. Dropping connection for 4 seconds...")
        time.sleep(4)
        
        subprocess.run(["adb", "shell", "cmd", "connectivity", "airplane-mode", "disable"], check=True)
        print("[Success] -> Airplane Mode OFF. Fresh IP assigned successfully to Realme 8!")
        return True
    except Exception as e:
        print(f"[Fallback] Cmd connectivity failed, switching to Realme Quick Settings UI toggle: {str(e)}")
        try:
            # Method 2: Realme UI swipe & tap sequence
            subprocess.run(["adb", "shell", "input", "keyevent", "26"], check=True) # Wake up screen
            time.sleep(1)
            subprocess.run(["adb", "shell", "input", "swipe", "500", "0", "500", "1200"], check=True) # Pull down status bar twice
            time.sleep(1)
            subprocess.run(["adb", "shell", "input", "swipe", "500", "0", "500", "1200"], check=True)
            time.sleep(1)
            # Tap coordinates for Airplane mode toggle (optimized for standard Realme UI 2.0/3.0 grid)
            subprocess.run(["adb", "shell", "input", "tap", "300", "550"], check=True)
            time.sleep(3)
            subprocess.run(["adb", "shell", "input", "tap", "300", "550"], check=True)
            print("[Success] -> Realme UI Airplane mode toggle sequence executed.")
            return True
        except Exception as err:
            print(f"[Error] All methods failed: {str(err)}")
            return False

if __name__ == "__main__":
    toggle_airplane_mode()
