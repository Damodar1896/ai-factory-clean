def get_payment_option(country_code):
    try:
        code = country_code.upper()
        if code == "IN":
            payment_info = {
                "country": "India",
                "currency": "INR",
                "amount": "₹1,999",
                "gateway": "1-Click UPI Intent (Zero Deduction)",
                "upi_id": "damodartechcraze@okaxis",
                "link": "upi://pay?pa=damodartechcraze@okaxis&pn=DAMODAR_TECHCRAZE&am=1999&cu=INR"
            }
        else:
            payment_info = {
                "country": "International",
                "currency": "USD",
                "amount": "$50",
                "gateway": "PayPal / Trust Wallet Crypto",
                "link": "https://paypal.me/damodartechcraze/50"
            }
            
        print(f"[✅ SUCCESS] Gateway Switcher Active for [{code}] -> Selected: {payment_info['gateway']} ({payment_info['amount']})")
        return payment_info
    except Exception as e:
        print(f"[!] Error in payment switcher: {e}")
        return None

if __name__ == "__main__":
    print("=== [SETTING UP MODULE 4: MULTI-CURRENCY PAYMENT SWITCHER] ===")
    get_payment_option("IN")
    get_payment_option("US")
