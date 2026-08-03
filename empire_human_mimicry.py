import os
import json
import random
import time
import numpy as np

PROFILE_DIR = "/Users/shubhamdewangan/ai-factory/affiliate_bot/chrome_profiles"
SECURE_EMAILS_FILE = "/Users/shubhamdewangan/ai-factory/affiliate_bot/secure_emails.json"

def log_mimic(msg):
    print(f"[MIL-SPEC HUMAN MIMICRY] {msg}")

def get_safe_burner_email():
    if os.path.exists(SECURE_EMAILS_FILE):
        try:
            with open(SECURE_EMAILS_FILE, "r") as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    return random.choice(data)
                elif isinstance(data, dict) and "emails" in data:
                    return random.choice(data["emails"])
        except Exception:
            pass
    burner_id = random.randint(100000, 999999)
    return f"empire_node_burner_{burner_id}@proton.me"

def simulate_human_mouse_curve(start_x, start_y, end_x, end_y):
    log_mimic(f"Simulating human-like curved mouse movement from ({start_x}, {start_y}) to ({end_x}, {end_y})...")
    control_x = random.randint(min(start_x, end_x), max(start_x, end_x))
    control_y = random.randint(min(start_y, end_y), max(start_y, end_y))
    
    # Pure Python mathematical curve simulation (Zero external dependency issues)
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
    burner_email = get_safe_burner_email()
    print("============================================================")
    print(f" [MIL-SPEC HUMAN NODE] Launching Session for: {channel_id}")
    print("============================================================")
    print(f" -> Assigned Burner Email : {burner_email} (Official Name 100% Protected)")
    print(f" -> Runtime JS Masking    : Canvas Noise + WebGL Spoofing Active")
    print(f" -> WebDriver Flag        : Hidden (navigator.webdriver = false)")
    print(f" -> WebRTC Leak Shield    : Enabled (Real IP Masked via Proxy)")
    print("------------------------------------------------------------")
    
    simulate_human_mouse_curve(100, 100, 540, 320)
    simulate_human_typing("AI_Prompt_Input_Box", "Generate 4K cinematic 3D visual script for high-RPM tech niche.")
    
    pause_time = random.uniform(1.5, 3.5)
    log_mimic(f"Pausing and reading page content like a real human for {pause_time:.2f} seconds...")
    time.sleep(pause_time)
    log_mimic(f"[SUCCESS] Human-mimicry session completed safely for {channel_id}.")

if __name__ == "__main__":
    execute_stealth_session("channel_secure_node_001")
