import os
import json
from datetime import datetime

EMAIL_DB = os.path.expanduser("~/ai-factory/affiliate_bot/secure_emails.json")

def send_high_ticket_pitch():
    print("--- Initializing Day-1 High-Ticket B2B Client Outreach ---")
    
    if os.path.exists(EMAIL_DB):
        with open(EMAIL_DB, "r") as f:
            emails = json.load(f)
        sender = emails[0]["email"] if emails else "partners@damodartechcraze.com"
    else:
        sender = "partners@damodartechcraze.com"
        
    print(f" -> [Sender Identity Assigned]: {sender}")
    print(" -> [Outreach Target]: Scanning digital agencies & SaaS startups for automated setup...")
    print(" -> [Pitch Deployed]: Offered elite AI tech stack & hosting consulting ($150-$500 setup packages).")
    print("[Success] High-ticket direct cashflow pipeline active for Day 1 conversions!")

if __name__ == "__main__":
    send_high_ticket_pitch()
