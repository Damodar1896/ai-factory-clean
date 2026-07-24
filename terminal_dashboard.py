import os
import json

def show_dashboard():
    print("=" * 60)
    print("      🔥 DAMODAR TECH CRAZE - LIVE ANALYTICS DASHBOARD 🔥")
    print("=" * 60)
    
    # 1. Emails Status
    email_db = os.path.expanduser("~/ai-factory/affiliate_bot/secure_emails.json")
    total_emails = 0
    if os.path.exists(email_db):
        try:
            with open(email_db, "r") as f:
                emails = json.load(f)
                total_emails = len(emails)
        except Exception:
            pass
    print(f"📧 Total Active Secure Emails : {total_emails} (Running 15/day rotation)")
    
    # 2. Tracking / Clicks Status
    track_db = os.path.expanduser("~/ai-factory/affiliate_bot/conversion_tracking.json")
    total_clicks = 0
    conversions = []
    if os.path.exists(track_db):
        try:
            with open(track_db, "r") as f:
                data = json.load(f)
                total_clicks = data.get("total_clicks", 0)
                conversions = data.get("conversions", [])
        except Exception:
            pass
            
    print(f"🔗 Total Affiliate Clicks     : {total_clicks}")
    print(f"💰 Total Recorded Conversions : {len(conversions)}")
    print("-" * 60)
    print("Recent Network Activity Logs:")
    for item in conversions[-5:]:
        print(f" -> [{item.get('timestamp')}] {item.get('network')} via {item.get('assigned_email')}")
    print("=" * 60)

if __name__ == "__main__":
    show_dashboard()
