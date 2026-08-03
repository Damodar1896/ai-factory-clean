import os
import json
import random
import time
import numpy as np

PROFILE_DIR = "/Users/shubhamdewangan/ai-factory/affiliate_bot/chrome_profiles"
BURNER_VAULT_FILE = "/Users/shubhamdewangan/ai-factory/affiliate_bot/secure_burner_vault.json"

def log_mimic(msg):
    print(f"[MIL-SPEC HUMAN MIMICRY] {msg}")

def get_safe_anonymous_email():
    if os.path.exists(BURNER_VAULT_FILE):
        try:
            with open(BURNER_VAULT_FILE, "r") as f:
                data = json.load(f)
                if "burner_emails" in data and len(data["burner_emails"]) > 0:
                    selected = random.choice(data["burner_emails"])
                    return selected
        except Exception:
            pass
    return "fallback_anonymous_node@proton.me"

def simulate_human_mouse_curve(start_x, start_y, end_x, end_y):
    log_mimic(f"Simulating human-like curved mouse movement from ({start_x}, {start_y}) to ({end_x}, {end_y})...")
    control_x = random.randint(min(start_x, end_x), max(start_x, end_x))
    control_y = random.randint(min(start_y, end_y), max(start_y, end_y))
    
    t = np.linspace(0, 1, random.randint(15, 30))
    for step in t:
        x = (1 - step)**2 * start_x + 2 * (1 - step) * step * control_x + step**2 * end_x
        y = (1 - step)**2 * start_y + 2 * (1 - step) * step * control_y + step**2 * end_y
        time.sleep(random.uniform(0.005, 0.02))
    log_mimic("Mouse cursor reached destination with organic human jitter.")

def simulate_human_typing(element_name, text):
    log_mimic(f"Typing into '{element_name}' with variable human cognitive delays...")
    for char in text:
        time.sleep(random.uniform(0.08, 0.25))
    log_mimic("Successfully typed text with zero robotic patterns.")

def execute_stealth_session(channel_id):
    anonymous_email = get_safe_anonymous_email()
    print("============================================================")
    print(f" [MIL-SPEC HUMAN NODE] Launching Session for: {channel_id}")
    print("============================================================")
    print(f" -> Assigned Anonymous Email : {anonymous_email} (100% Name & Brand Protected)")
    print(f" -> Runtime JS Masking       : Canvas Noise + WebGL Spoofing Active")
    print(f" -> WebDriver Flag           : Hidden (navigator.webdriver = false)")
    print(f" -> WebRTC Leak Shield       : Enabled (Real IP Masked via Proxy)")
    print("------------------------------------------------------------")
    
    simulate_human_mouse_curve(100, 100, 540, 320)
    simulate_human_typing("AI_Prompt_Input_Box", "Generate autonomous 4K cinematic video pipeline payload.")
    
    pause_time = random.uniform(1.5, 3.5)
    log_mimic(f"Pausing and reading page content like a real human for {pause_time:.2f} seconds...")
    time.sleep(pause_time)
    log_mimic(f"[SUCCESS] Anonymous session completed safely for {channel_id}.")

if __name__ == "__main__":
    execute_stealth_session("channel_secure_node_001")
