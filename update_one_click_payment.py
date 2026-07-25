import json

def generate_one_click_upi_link(amount_inr, client_email):
    upi_id = "damodartechcraze@okaxis"
    name = "DAMODAR_TECHCRAZE_VE"
    note = "Business_Growth_Database_Package"
    
    # Standard UPI Intent URI (Yeh link automatic amount aur app open kar dega)
    upi_intent_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount_inr}&cu=INR&tn={note}"
    
    print(f"[1-Click Payment Generated] For {client_email} -> Amount: ₹{amount_inr}")
    print(f"-> UPI Intent URL: {upi_intent_link}")
    return upi_intent_link

if __name__ == "__main__":
    print("=== [1-CLICK UPI INTENT PAYMENT GENERATOR] ===")
    # Test generation for ₹1,999 package
    generate_one_click_upi_link(1999, "client@targetbusiness.com")
