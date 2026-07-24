import json
import os

class OmnichannelAIBrain:
    def __init__(self):
        self.business_name = "Damodar Tech Craze Automation"
        self.payment_link = "https://damodartechcraze.com/pay-now"
        
    def process_incoming_message(self, user_id, channel, user_message):
        print(f"\n[AI Brain] Incoming Message from {channel} (User: {user_id})")
        print(f" -> User Message: {user_message}")
        
        # Simulated AI Intent & Objection Handling Logic
        msg_lower = user_message.lower()
        
        if "price" in msg_lower or "cost" in msg_lower or "kitna" in msg_lower or "charge" in msg_lower:
            reply = f"Hey! Our AI Automation setup starts at just $150. It includes 24/7 auto-chat, lead gen, and instant closing. Would you like to get started today?"
        elif "buy" in msg_lower or "pay" in msg_lower or "payment" in msg_lower or "ha" in msg_lower or "yes" in msg_lower:
            reply = f"Awesome! You can complete your setup securely using this instant link: {self.payment_link} - Once done, our automated engine will go live instantly! 🚀"
        elif "doubt" in msg_lower or "how" in msg_lower or "kaise" in msg_lower:
            reply = f"Our AI Chatbot connects directly to WhatsApp, Instagram, Telegram & Email. It handles chatting, answers doubts 24/7, and automatically closes sales for your business."
        else:
            reply = f"Hello! Welcome to {self.business_name}. We help businesses automate 100% of their customer chats & sales. How can I help you scale today?"
            
        print(f" -> Generated AI Response: {reply}")
        return reply

if __name__ == "__main__":
    ai_engine = OmnichannelAIBrain()
    # Test simulation
    ai_engine.process_incoming_message("user_101", "Instagram DM", "What is the price of your automation?")
    ai_engine.process_incoming_message("user_101", "WhatsApp", "I want to buy this service, send payment link")
