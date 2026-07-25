def chatbot_auto_responder(user_message):
    try:
        msg = user_message.lower()
        if "price" in msg or "cost" in msg or "kitna" in msg or "rate" in msg:
            reply = "The verified leads database package is priced at just ₹1,999. Here is your 1-Click checkout link: upi://pay?pa=damodartechcraze@okaxis&pn=DAMODAR_TECHCRAZE&am=1999&cu=INR"
        elif "leads" in msg or "data" in msg or "contact" in msg:
            reply = "We provide 1000+ verified active business leads for your niche with direct decision-maker emails and phones!"
        else:
            reply = "Thanks for reaching out to Damodar Tech Craze! How can we scale your business today? Type 'price' for packages."
        
        print(f"[✅ SUCCESS] AI Chatbot Responded -> User: '{user_message}' | Reply: '{reply}'")
        return reply
    except Exception as e:
        print(f"[!] Error in chatbot: {e}")
        return "Thank you for reaching out!"

if __name__ == "__main__":
    print("=== [SETTING UP MODULE 5: AI INBOX CHATBOT] ===")
    chatbot_auto_responder("What is the price of leads?")
