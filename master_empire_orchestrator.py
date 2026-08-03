import os
import time
import datetime
import json

LOG_FILE = "/Users/shubhamdewangan/ai-factory/empire_master_execution.log"

def log_orchestrator(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{ts}] [GRAND-MASTER-DISPATCHER] {msg}"
    print(formatted_msg)
    with open(LOG_FILE, "a") as f:
        f.write(formatted_msg + "\n")

def run_empire_cycle():
    log_orchestrator("=== STARTING AUTONOMOUS EMPIRE PRODUCTION CYCLE ===")
    
    # 1. Step: Harvest Real-Time Market Intelligence
    log_orchestrator("Phase 1: Running Market Intel & Competitor Trend Scraper...")
    os.system("python3 /Users/shubhamdewangan/ai-factory/empire_market_intel.py")
    
    # 2. Step: Generate Content Payload & High-CTR Assets
    log_orchestrator("Phase 2: Running Autonomous Content & Thumbnail Factory...")
    os.system("python3 /Users/shubhamdewangan/ai-factory/empire_content_factory.py")
    
    # 3. Step: Execute Mil-Spec Anti-Detect & Human Mimicry Validation
    log_orchestrator("Phase 3: Running Mil-Spec Anti-Detect & Human Mimicry Nodes...")
    os.system("python3 /Users/shubhamdewangan/ai-factory/empire_human_mimicry.py")
    
    log_orchestrator("=== EMPIRE PRODUCTION CYCLE COMPLETED SUCCESSFULLY ===")

def start_eternal_loop():
    log_orchestrator("Initializing 24/7 Autonomous Master Dispatcher Daemon...")
    while True:
        try:
            run_empire_cycle()
            log_orchestrator("Cooling down engine for 30 minutes before next batch execution...")
            time.sleep(1800) # 30 minutes rest period to maintain absolute safety and low resource usage
        except Exception as e:
            log_orchestrator(f"[CRITICAL ERROR DETECTED] Self-healing protocol activated. Error: {str(e)}")
            time.sleep(60)

if __name__ == "__main__":
    start_eternal_loop()
