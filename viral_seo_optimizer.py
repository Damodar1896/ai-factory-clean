import os, json
from datetime import datetime

def generate_viral_metadata(niche="AI Automation"):
    print(f"=== [VIRAL SEO OPTIMIZER] Generating High-CTR Titles for: {niche} ===")
    
    # Psychological High-CTR Hook Templates
    titles = [
        f"Stop Doing This in 2026! 🛑 (Biggest {niche} Mistake)",
        f"What OpenAI is Hiding About {niche} 🤫",
        f"Is Your Career Safe From {niche}? ⚠️",
        f"The Forbidden {niche} Strategy Nobody Tells You 🚀"
    ]
    
    description = f"""
🔥 Get the complete free code and setup guide below!
👉 Direct Payment / UPI Support: damodar.business@okhdfcbank
👉 Access the 2026 Automation Stack instantly.

In this video, we reveal the truth about {niche} and how top creators are scaling their digital empire without spending a single rupee on manual labor.

#shorts #trending #viral #{niche.replace(" ", "")} #automation
"""

    payload = {
        "niche": niche,
        "recommended_titles": titles,
        "description": description.strip(),
        "timestamp": str(datetime.now())
    }
    
    with open("viral_seo_payload.json", "w") as f:
        json.dump(payload, f, indent=4)
        
    print("[SUCCESS] Viral SEO payload generated successfully!")

if __name__ == "__main__":
    generate_viral_metadata("AI Tech Stack")
