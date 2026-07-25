import subprocess
import time

def force_connect_new_phone():
    print("[*] Restarting ADB server to establish fresh link...")
    subprocess.run(["adb", "kill-server"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["adb", "start-server"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)

    print("[*] Scanning connected hardware...")
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    output = result.stdout.strip()
    
    lines = output.splitlines()
    connected_devices = []
    
    for line in lines[1:]:
        if "\tdevice" in line:
            device_id = line.split("\t")[0]
            connected_devices.append(device_id)

    if connected_devices:
        active_id = connected_devices[0]
        print(f"[+] Success! Connected device ID: {active_id}")
        return active_id
    else:
        print("[!] No active devices detected. Please ensure:")
        print("    - USB Cable is properly plugged in")
        print("    - USB Debugging is enabled on your phone")
        print("    - Authorization prompt is accepted on screen")
        return None

if __name__ == "__main__":
    force_connect_new_phone()
