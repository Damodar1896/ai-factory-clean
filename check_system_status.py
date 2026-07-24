import os
import json

def check_system():
    print("============================================================")
    print("      🔍 DAMODAR TECH EMPIRE - DIAGNOSTIC CHECKER 🔍       ")
    print("============================================================")
    
    # 1. Check Database / JSON Lead Files
    db_path = "saas_database.db"
    if os.path.exists(db_path):
        print(f" [OK] Main Database found: '{db_path}' (Leads storage active)")
    else:
        print(f" [Warning] Database '{db_path}' not found yet. Submit a lead on the dashboard first.")
        
    # 2. Check Warmup Logs
    log_path = "warmup_metrics.log"
    if os.path.exists(log_path):
        print(f" [OK] Warmup log file found: '{log_path}'")
        with open(log_path, "r") as f:
            lines = f.readlines()
            print(f" -> Total recorded warmup transactions: {len(lines)}")
    else:
        print(f" [Notice] 'warmup_metrics.log' is not created yet (Using default rotation)")
        
    print("-" * 60)
    print("[Success] System diagnostic scan complete!")
    print("============================================================")

if __name__ == "__main__":
    check_system()
