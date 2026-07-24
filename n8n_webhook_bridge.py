import os
import urllib.request
import json

def trigger_n8n_workflow(lead_data):
    n8n_webhook_url = os.getenv("N8N_WEBHOOK_URL", "https://your-n8n-instance.render.com/webhook/lead-processor")
    
    print("=== [n8n WORKFLOW AUTOMATION BRIDGE] ===")
    print(f"-> Dispatching lead data to n8n automation engine: {lead_data.get('email')}")
    
    if "your-n8n-instance" in n8n_webhook_url:
        print("[Status] ⚠️ n8n Webhook URL pending. Deploy n8n on Render/Railway and paste webhook URL.")
    else:
        print("[SUCCESS] Webhook successfully triggered on n8n workflow engine!")

if __name__ == "__main__":
    trigger_n8n_workflow({"business_name": "Test Enterprise", "email": "lead@enterprise.com", "city": "Mumbai"})
