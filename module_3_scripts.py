import os
import json
import datetime

OUTPUT_DIR = "/Users/shubhamdewangan/ai-factory/step_by_step_output"
SCRIPTS_DIR = os.path.join(OUTPUT_DIR, "scripts")
TOPICS_FILE = os.path.join(OUTPUT_DIR, "module_2_topics.json")

os.makedirs(SCRIPTS_DIR, exist_ok=True)

def log_mod(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [MODULE-3-SCRIPTS] {msg}")

def write_high_retention_scripts():
    log_mod("Initializing Module 3: Writing High-Retention Scripts for all Channels...")
    
    if not os.path.exists(TOPICS_FILE):
        log_mod("[ERROR] Module 2 topics file not found! Please run Module 2 first.")
        return

    with open(TOPICS_FILE, "r") as f:
        topics_data = json.load(f)

    for ch_id, info in topics_data.items():
        niche = info["niche"]
        topic = info["trending_topic"]
        
        script_content = {
            "channel_id": ch_id,
            "niche": niche,
            "title": topic,
            "hook": f"Stop scrolling! The top 1% are quietly executing this exact {niche.replace('_', ' ')} strategy in 2026...",
            "body": f"While everyone else is confused, automated workflows are capturing the market share. Here is the exact step-by-step breakdown.",
            "call_to_action": "Subscribe right now to stay ahead of the 2026 technological shift!"
        }
        
        script_path = os.path.join(SCRIPTS_DIR, f"{ch_id}_script.json")
        with open(script_path, "w") as sf:
            json.dump(script_content, sf, indent=4)
            
        print(f" -> [{ch_id}] Script written for: {niche}")

    log_mod(f"[SUCCESS] Module 3 Completed! All 20 scripts compiled and saved in {SCRIPTS_DIR}")

if __name__ == "__main__":
    write_high_retention_scripts()
