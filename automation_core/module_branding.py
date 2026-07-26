import json
import os

NICHE_REGISTRY = {
    "AI_TECH": {
        "names": ["NexusAI_X", "SyntheticMind_HQ", "AITecOps"],
        "rpm_range": "$20 - $35",
        "hooks": ["They are hiding this AI capability from you...", "The end of traditional coding is here."]
    },
    "FINANCE": {
        "names": ["WealthMatrix_Live", "CapitalCode_247", "AlphaYield"],
        "rpm_range": "$25 - $50",
        "hooks": ["The hidden loophole banks don't want you to know...", "How the top 1% automate their cash flow."]
    },
    "DARK_PSYCHOLOGY": {
        "names": ["MindGuard_X", "ShadowInfluence", "CognitiveEdge"],
        "rpm_range": "$12 - $25",
        "hooks": ["3 manipulation triggers used against you daily...", "Master conversational dominance instantly."]
    }
}

def initialize_branding(niche_key):
    os.makedirs("config/branding", exist_ok=True)
    profile = NICHE_REGISTRY.get(niche_key, NICHE_REGISTRY["AI_TECH"])
    
    brand_data = {
        "selected_niche": niche_key,
        "assigned_brand": profile["names"][0],
        "estimated_rpm": profile["rpm_range"],
        "default_hooks": profile["hooks"]
    }
    
    with open("config/branding/active_brand.json", "w") as f:
        json.dump(brand_data, f, indent=4)
    print(f"[+] Branding Initialized for: {brand_data['assigned_brand']} ({niche_key})")

if __name__ == "__main__":
    initialize_branding("FINANCE")
