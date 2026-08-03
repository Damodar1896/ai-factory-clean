import os
import json
import datetime

OUTPUT_DIR = "/Users/shubhamdewangan/ai-factory/step_by_step_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def log_mod(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [MODULE-1-NICHES] {msg}")

def generate_niches_list():
    log_mod("Initializing Module 1: Compiling 20 High-RPM Niches...")
    
    niches = [
        "AI_Wealth_Monopoly", "Cyber_Security_2026", "Autonomous_Robotics", 
        "Luxury_Future_Tech", "Space_Mining_Economy", "Quantum_Computing", 
        "Neural_Interfaces", "Synthetic_Media_Empires", "Decentralized_AI_Agents", "Bio_Tech_Longevity",
        "Passive_Income_Automations", "Cloud_Infrastructure", "Deepfake_Defense", "Nano_Tech_Medicine",
        "Smart_City_Grid", "Metaverse_Real_Estate", "Algorithmic_Trading", "Bio_Hacking_Elite", "Autonomous_Drones", "Zero_Day_Exploits"
    ]
    
    niches_data = {
        "total_niches": len(niches),
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "niches": niches
    }
    
    file_path = os.path.join(OUTPUT_DIR, "module_1_niches.json")
    with open(file_path, "w") as f:
        json.dump(niches_data, f, indent=4)
        
    log_mod(f"[SUCCESS] Module 1 Completed! 20 Niches locked at {file_path}")
    for i, n in enumerate(niches, 1):
        print(f" -> [{i:02d}] {n}")

if __name__ == "__main__":
    generate_niches_list()
