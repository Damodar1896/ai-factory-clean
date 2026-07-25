from datetime import datetime

def check_customer_churn(last_active_date_str):
    try:
        last_date = datetime.strptime(last_active_date_str, "%Y-%m-%d")
        days_inactive = (datetime.now() - last_date).days
        
        if days_inactive > 30:
            action = f"⚠️ Churn Risk Detected ({days_inactive} days inactive). Triggering Win-Back 40% Discount Offer!"
        else:
            action = "Active Customer. Engagement healthy."
            
        print(f"[✅ SUCCESS] Churn Predictor Checked -> Last Active: {last_active_date_str} | Status: {action}")
        return days_inactive > 30
    except Exception as e:
        print(f"[!] Error in churn predictor: {e}")
        return False

if __name__ == "__main__":
    print("=== [SETTING UP MODULE 7: CHURN PREDICTOR] ===")
    check_customer_churn("2026-06-01")
