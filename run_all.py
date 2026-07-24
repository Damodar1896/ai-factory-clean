import subprocess
import time
import os
from datetime import datetime

def log_master(msg):
    print(f"[Master Hub] [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def run_pipeline():
    log_master("=== Starting Autonomous Business Empire & Sales Pipeline ===")
    
    while True:
        # Step 1: Run Master Scraper to fetch fresh high-scale leads
        log_master("Running Lead Generation & IP Rotation Batch...")
        subprocess.run(["python3", "business_empire_master.py"])
        
        # Step 2: Run Outreach Dispatcher to pitch fresh leads
        log_master("Running Automated Cold Email Outreach & Pitch Dispatcher...")
        subprocess.run(["python3", "outreach_dispatcher.py"])
        
        log_master("=== Pipeline Cycle Completed. Resting for 2 hours before next batch ===")
        time.sleep(7200) # 2 hours rest

if __name__ == "__main__":
    run_pipeline()
