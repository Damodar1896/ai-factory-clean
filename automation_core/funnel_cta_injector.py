import os
import time
from pathlib import Path

Path("automation_core/data").mkdir(parents=True, exist_ok=True)
Path("automation_core/logs").mkdir(parents=True, exist_ok=True)

def log_funnel_event(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] [Funnel CTA Injector] {message}"
    print(log_msg)
    with open("automation_core/logs/funnel_cta.log", "a") as f:
        f.write(log_msg + "\n")

def generate_optimized_cta_description(video_title="Automate Your Business with AI"):
    log_funnel_event(f"Generating high-converting monetization CTA for: '{video_title}'")
    
    cta_text = f"""
🔥 {video_title}
--------------------------------------------------
🚀 Stop manual work and scale your business 24x7 with our Autonomous AI Empire Stack!
👉 Instant Access to Mini-App Store & Tools: Check Pinned Comment / Bio.

💳 Direct Secure Payment (Zero Commission):
• UPI ID: damodartechcraze@okaxis
• Bank Transfer: Canara Bank (9232698947@cnrb)

💬 Got questions? Ping us directly on WhatsApp: +91 9232698947
#BusinessAutomation #AI #YouTubeShorts #PassiveIncome
"""
    
    output_file = "automation_core/data/latest_video_cta.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(cta_text.strip())
        
    log_funnel_event(f"[✅ SUCCESS] Optimized description & UPI CTA locked at: {output_file}")
    return cta_text

if __name__ == "__main__":
    generate_optimized_cta_description()
