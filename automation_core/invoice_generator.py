import os
import time
import json
from pathlib import Path

Path("automation_core/data/invoices").mkdir(parents=True, exist_ok=True)
Path("automation_core/logs").mkdir(parents=True, exist_ok=True)

def log_invoice(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] [GST Invoice Engine] {message}"
    print(log_msg)
    with open("automation_core/logs/invoice_generator.log", "a") as f:
        f.write(log_msg + "\n")

def generate_gst_invoice(customer_name="Rahul Sharma", amount_inr=5000, item_desc="AI Automation Empire Setup"):
    log_invoice("=== [GENERATING COMPLIANT GST TAX INVOICE] ===")
    
    invoice_id = f"INV-2026-{int(time.time())}"
    cgst = amount_inr * 0.09  # 9% CGST
    sgst = amount_inr * 0.09  # 9% SGST
    total_amount = amount_inr + cgst + sgst
    
    invoice_data = {
        "invoice_id": invoice_id,
        "date": time.strftime("%Y-%m-%d"),
        "customer_name": customer_name,
        "item": item_desc,
        "base_amount_inr": amount_inr,
        "cgst_9_percent": cgst,
        "sgst_9_percent": sgst,
        "total_amount_inr": total_amount,
        "payment_gateway": "UPI Direct",
        "upi_id": "damodartechcraze@okaxis"
    }
    
    file_path = f"automation_core/data/invoices/{invoice_id}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(invoice_data, f, indent=4)
        
    log_invoice(f"[✅ SUCCESS] GST Tax Invoice generated successfully: {file_path}")
    log_invoice(f"Total Amount: ₹{total_amount:.2f} | Payout Locked to: damodartechcraze@okaxis")
    return invoice_id

if __name__ == "__main__":
    generate_gst_invoice()
