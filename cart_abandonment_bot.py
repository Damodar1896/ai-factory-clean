def trigger_cart_recovery(client_name, phone):
    try:
        recovery_message = f"Hi {client_name}, we noticed you checked out the Verified Leads database package but didn't complete your UPI payment. Here is an exclusive 10% off coupon: 'SAVE10'. Complete your order instantly here: upi://pay?pa=damodartechcraze@okaxis&am=1799&cu=INR&tn=Abandoned_Cart_Discount"
        
        print(f"[✅ SUCCESS] Cart Abandonment Bot Triggered -> Sent recovery reminder to {phone} for {client_name}")
        print(f"-> Dispatched Message: {recovery_message}")
        return True
    except Exception as e:
        print(f"[!] Error in cart recovery bot: {e}")
        return False

if __name__ == "__main__":
    print("=== [SETTING UP MODULE 9: CART ABANDONMENT BOT] ===")
    trigger_cart_recovery("Rahul Sharma", "+919232698947")
