import time
import subprocess
import os
import datetime

# डायरेक्टरीज का पाथ
AFFILIATE_DIR = "/Users/shubhamdewangan/ai-factory/affiliate_bot"
ROOT_DIR = "/Users/shubhamdewangan/ai-factory"

def log_message(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [EMPIRE BRAIN] {msg}")
    with open(os.path.join(ROOT_DIR, "empire_autonomous_system.log"), "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

def run_task(script_name, folder):
    script_path = os.path.join(folder, script_name)
    if os.path.exists(script_path):
        log_message(f"Starting Task: {script_name}")
        try:
            subprocess.run(f"cd {folder} && python3 {script_name}", shell=True, check=True)
            log_message(f"Successfully Completed: {script_name}")
        except Exception as e:
            log_message(f"Error executing {script_name}: {e}")
    else:
            log_message(f"Warning: Script {script_name} not found at {script_path}")

def autonomous_loop():
    log_message("=== DAMODAR EMPIRE AUTONOMOUS BRAIN INITIALIZED (24/7 ZERO-MANUAL MODE) ===")
    
    while True:
        current_hour = datetime.datetime.now().hour
        
        # 1. ईमेल ऑटोमेशन और लीड हार्वेस्टिंग (दिन के समय हाई प्रायोरिटी)
        log_message("Triggering Email & Lead Generation Engine...")
        run_task("master_autopilot.py", AFFILIATE_DIR)
        run_task("immortal_email_autopilot.py", AFFILIATE_DIR)
        
        # 2. pSEO पेज जनरेशन (जब जरूरत हो या सेफ लिमिट में)
        log_message("Checking pSEO Pages & Smart Drip Generators...")
        run_task("smart_drip_generator.py", AFFILIATE_DIR)
        
        # 3. ऑटो गिटहब सिंक (ताकि हर नया डेटा और लॉग सेफली ऑनलाइन बैकअप हो जाए)
        log_message("Performing Autonomous GitHub Sync...")
        try:
            os.chdir(ROOT_DIR)
            subprocess.run("git add -A", shell=True)
            subprocess.run('git commit -m "Auto-Autonomous Empire Sync 2026"', shell=True)
            subprocess.run("git push origin main", shell=True)
            log_message("GitHub Sync Successful.")
        except Exception as e:
            log_message(f"GitHub Sync Error: {e}")
            
        # 4. स्मार्ट रेस्ट पीरियड (सिस्टम को ओवरहीट या बैन से बचाने के लिए 2 घंटे का सेफ गैप)
        log_message("All core cycles completed. Entering smart stealth rest for 2 hours...")
        time.sleep(7200)

if __name__ == "__main__":
    autonomous_loop()
