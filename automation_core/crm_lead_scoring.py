import os
import json
import time
from pathlib import Path

Path("automation_core/data").mkdir(parents=True, exist_ok=True)
Path("automation_core/logs").mkdir(parents=True, exist_ok=True)

def log_crm(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] [CRM Lead Scoring] {message}"
    print(log_msg)
    with open("automation_core/logs/crm_scoring.log", "a") as f:
        f.write(log_msg + "\n")

def evaluate_and_score_leads():
    log_crm("=== [RUNNING ADVANCED CRM LEAD SCORING PIPELINE] ===")
    leads = [
        {"name": "Rahul Sharma", "business": "Gym Indore", "interactions": 8, "intent": "High"},
        {"name": "Priya Verma", "business": "Bhopal Clinic", "interactions": 2, "intent": "Low"}
    ]
    scored_leads = []
    for lead in leads:
        score = (lead["interactions"] * 10) + (50 if lead["intent"] == "High" else 10)
        status = "🔥 HOT LEAD (Priority Outreach)" if score >= 70 else "❄️ COLD LEAD (Nurture Sequence)"
        scored_lead = {"name": lead["name"], "business": lead["business"], "score": score, "status": status}
        scored_leads.append(scored_lead)
        log_crm(f"Lead: {lead["name"]} | Score: {score} | Status: {status}")
    
    db_path = "automation_core/data/crm_scored_leads.json"
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(scored_leads, f, indent=4)
    log_crm(f"[✅ SUCCESS] CRM Lead Scoring database updated: {db_path}")

if __name__ == "__main__":
    evaluate_and_score_leads()
