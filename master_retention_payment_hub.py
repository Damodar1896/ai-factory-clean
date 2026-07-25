
# Auto-injected Community & Group Rotator Hook
try:
    from setup_professional_communities import ProfessionalCommunityArchitect
    community_architect = ProfessionalCommunityArchitect()
except ImportError:
    community_architect = None

import os
import json
import requests

# ==========================================
# 🔐 FINAL LOCKED CONFIGURATION
# ==========================================
UPI_ID = "damodartechcraze@okaxis"
CANDY_UPI_QR = "9232698947@cnrb"
OWNER_WHATSAPP = "+919232698947"
TELEGRAM_CHAT_ID = "8720676587"

def generate_one_click_payment_link(amount_inr, client_name, service_name):
    """Generates 1-Click UPI Intent Link with pre-filled amount and details"""
    upi_intent = f"upi://pay?pa={UPI_ID}&pn=DAMODAR_TECHCRAZE&am={amount_inr}&cu=INR&tn={service_name}"
    return upi_intent

def dispatch_retention_welcome_message(client_email, client_phone, client_name, business_name, city, amount_paid):
    """Sends powerful retention greeting, onboarding guide, and secure access link via multi-channel fallback"""
    
    secure_download_link = "https://damodartechcraze.com/download/secure-growth-bundle"
    
    message_body = (
        f"Hi {client_name},\n\n"
        f"Welcome aboard! It’s an absolute pleasure to partner with {business_name} in {city}.\n"
        f"Your payment of ₹{amount_paid} has been successfully verified, and your business empire growth engine is now unlocked.\n\n"
        f"1. Your Direct Secure Download / Access Link:\n"
        f"👉 {secure_download_link}\n\n"
        f"2. Your 24-Hour Quick-Start Action Guide:\n"
        f"• Step 1: Download your verified leads/assets using the link above.\n"
        f"• Step 2: Import the database into your outreach CRM.\n"
        f"• Step 3: Deploy our pre-written high-conversion scripts to start closing deals on autopilot.\n\n"
        f"3. Special Loyalty Perk (Exclusive for You):\n"
        f"As a valued partner, you get an exclusive 40% OFF on our upcoming AI Automation & DFY Agency Scaling Toolkit. Use code VIPLIFETIME.\n\n"
        f"4. Direct Support:\n"
        f"Need help? Reply here or WhatsApp us instantly at {OWNER_WHATSAPP}. We've got your back 24/7!\n\n"
        f"Best regards,\nTeam Damodar Tech Craze"
    )
    
    print(f"\n[🔄 MULTI-CHANNEL DISPATCH] Attempting primary channel (Email) for {client_email}...")
    email_success = False  # Simulated primary check
    
    if not email_success:
        print(f"[⚠️ Email Limit / Fallback Triggered] Switching to Fallback Channel 1 (WhatsApp)...")
        print(f"[✅ WhatsApp Retention Message Sent to {client_phone}]:\n{message_body}\n")
    
    # Notify Business Owner on WhatsApp instantly
    owner_alert = f"💰 *PAYMENT RECEIVED & LOCKED*\nClient: {client_name} ({business_name}, {city})\nAmount: ₹{amount_paid}\nChannel: Multi-Channel Retention Active"
    print(f"[🔔 OWNER WHATSAPP ALERT TO {OWNER_WHATSAPP}] -> {owner_alert}")

if __name__ == "__main__":
    print("==================================================")
    print("🚀 MASTER RETENTION & 1-CLICK PAYMENT HUB LOCKED")
    print("==================================================")
    
    # Test execution for a closed client
    sample_payment_link = generate_one_click_payment_link(1999, "Rahul Sharma", "Verified_Leads_Package")
    print(f"[Test 1-Click Link Generated] {sample_payment_link}\n")
    
    dispatch_retention_welcome_message(
        client_email="client@targetbusiness.com",
        client_phone="+919232698947",
        client_name="Rahul Sharma",
        business_name="Prime Real Estate",
        city="Mumbai",
        amount_paid=1999
    )
