import os
import json

TARGETS_FILE = os.path.expanduser("~/ai-factory/affiliate_bot/affiliate_targets.json")

def generate_social_posts():
    print("--- Initializing Automated Social Media Syndicator ---")
    
    if os.path.exists(TARGETS_FILE):
        with open(TARGETS_FILE, "r") as f:
            data = json.load(f)
        networks = data.get("networks", [])
    else:
        networks = [{"name": "ClickBank", "category": "Digital Products"}]
        
    posts_generated = 0
    for net in networks[:10]: # Top 10 networks ka sample post
        name = net.get("name")
        category = net.get("category")
        
        post_content = f"🔥 Looking for the best {category} platform? Check out our honest review and breakdown of {name} on Damodar Tech Craze! Maximize your workflow today. 🚀\n\n👉 Explore here: https://damodartechcraze.com\n#AffiliateMarketing #Tech #SaaS #{name.replace(' ', '')}"
        
        print(f"\n[Generated Post for {name}]:\n{post_content}")
        posts_generated += 1
        
    print(f"\n[Success] Generated {posts_generated} ready-to-publish social media posts for syndication!")

if __name__ == "__main__":
    generate_social_posts()
