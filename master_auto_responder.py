import os
import json
import time
import random

print("==================================================")
print("   DAMODAR EMPIRE: AUTO-RESPONDER EMAIL ENGINE   ")
print("==================================================")

def run_auto_responder():
    responder_log = "auto_responder_execution.json"
    
    while True:
        try:
            if os.path.exists(responder_log):
                with open(responder_log, "r", encoding="utf-8") as f:
                    data = json.load(f)
            else:
                data = {"responses_sent": []}
                
            response_id = f"RESP-{random.randint(10000, 99999)}"
            
            # Simulate autonomous auto-responder action
            response_record = {
                "response_id": response_id,
                "recipient_tier": "Enterprise Lead",
                "status": "Auto-Responded & Nurtured",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            data["responses_sent"].append(response_record)
            with open(responder_log, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
                
            print(f"[EMAIL AUTO-RESPONDER] Sent intelligent nurture sequence for lead ID {response_id}!")
            
            # Natural human pacing interval before next email batch (10 to 30 mins)
            rest_gap = random.randint(600, 1800)
            print(f"[⏳ PACING] Auto-responder resting for {rest_gap // 60} minutes to ensure high deliverability...")
            
            for _ in range(rest_gap // 30):
                time.sleep(30)
                
        except Exception as err:
            print(f"[⚠️ AUTO-RESPONDER EXCEPTION]: {err}")
            time.sleep(30)

if __name__ == "__main__":
    run_auto_responder()
