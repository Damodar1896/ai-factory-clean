def calculate_lead_score(lead_data):
    try:
        score = 0
        if lead_data.get("email_opened"): score += 20
        if lead_data.get("clicked_payment_link"): score += 50
        if lead_data.get("visited_community"): score += 30
        
        status = "Warm Lead"
        if score >= 70:
            status = "🔥 HOT LEAD (Ready to Close)"
        elif score < 30:
            status = "Cold Lead"
            
        print(f"[✅ SUCCESS] Lead Scoring Evaluated -> Name: {lead_data.get('name')} | Score: {score}/100 | Status: {status}")
        return score, status
    except Exception as e:
        print(f"[!] Error in lead scoring: {e}")
        return 0, "Error"

if __name__ == "__main__":
    print("=== [SETTING UP MODULE 3: ADVANCED LEAD SCORING SYSTEM] ===")
    calculate_lead_score({"name": "Amit Verma", "email_opened": True, "clicked_payment_link": True, "visited_community": False})
