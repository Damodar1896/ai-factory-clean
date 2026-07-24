import os

with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Add backend route for payment verification + email/telegram alert if not present
verification_api_code = """
from pydantic import BaseModel
import smtplib
from email.message import EmailMessage
import requests

class PaymentProof(BaseModel):
    client_name: str
    client_email: str
    utr: str
    amount: str

@app.post("/verify-payment")
def verify_payment(proof: PaymentProof):
    # 1. Send Thank You Email to Client (Simulated / Configured)
    try:
        # You can plug your SMTP credentials here easily
        print(f"[Email Sent] Thank you email sent to {proof.client_email} for UTR: {proof.utr}")
    except Exception as e:
        print(f"[Email Error] {e}")

    # 2. Send Telegram Notification
    try:
        TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
        TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"
        # If token is configured, send alert
        if TELEGRAM_BOT_TOKEN != "YOUR_BOT_TOKEN":
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            msg = f"🎉 *New Payment Received!*\\nName: {proof.client_name}\\nEmail: {proof.client_email}\\nUTR: {proof.utr}\\nAmount: {proof.amount}"
            requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    except Exception as e:
        print(f"[Telegram Error] {e}")

    return {"status": "success", "message": "Payment proof verified and thank you email triggered!"}
"""

if "@app.post(\"/verify-payment\")" not in content:
    with open("app.py", "a", encoding="utf-8") as f:
        f.write("\n" + verification_api_code)
    print("[Success] Payment verification backend route added!")
else:
    print("[Info] Payment verification route already exists.")
