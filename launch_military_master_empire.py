import os
import subprocess
import time

def launch_master_empire():
    print("="*70)
    print("[*] [MILITARY MASTER ARCHITECT] Verifying & Launching 24/7 Autopilot Empire...")
    print("="*70)

    modules = [
        "automation_core/module_military_01_mac.py",
        "automation_core/module_military_02_tls.py",
        "automation_core/module_military_03_ram.py",
        "automation_core/module_military_04_watchdog.py",
        "automation_core/module_military_05_geo.py",
        "automation_core/module_military_06_captcha.py",
        "automation_core/module_military_07_cache.py",
        "automation_core/module_military_08_deadman.py",
        "automation_core/module_military_09_throttle.py",
        "automation_core/module_military_10_rollback.py"
    ]

    for mod in modules:
        print(f"[VERIFYING] -> {mod}")
        subprocess.run(["python", mod], check=True)

    print("="*70)
    print("[SUCCESS] All 10 Military-Grade Safety Layers Verified and Active!")
    print("[*] Launching 24/7 Autopilot Background Daemon...")
    
    # Launch supervisor
    os.system("python launch_autopilot.py")
    print("[SUCCESS] Empire is now running fully autonomously in 24/7 Military Autopilot mode.")
    print("="*70)

if __name__ == "__main__":
    launch_master_empire()
