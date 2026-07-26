import json
import os

NICHE_REGISTRY = {
    "AI_TECH": {
        "names": ["Singularity", "The New Era", "Synthetica", "Cortex", "Aetherium"],
        "rpm_range": "$25 - $45",
        "hooks": [
            "They are hiding this intelligence architecture from public view...", 
            "The infrastructure of tomorrow is being written without you."
        ]
    },
    "FINANCE": {
        "names": ["Capital Club", "The 1%", "AssetForge", "WealthLedger", "Monopoly Mindset"],
        "rpm_range": "$30 - $60",
        "hooks": [
            "The silent asset allocation strategy of generational dynasties...", 
            "How the top 1 percent systematically engineer asymmetric returns."
        ]
    },
    "DARK_PSYCHOLOGY": {
        "names": ["Shadow Work", "The Architect", "Human Ledger", "Subtle Art", "Mentalist"],
        "rpm_range": "$15 - $30",
        "hooks": [
            "The invisible behavioral loops governing every decision you make...", 
            "Mastering the quiet art of absolute psychological compliance."
        ]
    },
    "LUXURY_LIFESTYLE": {
        "names": ["Opulence", "The Vault", "Heritage & High", "Aethelgard", "Status Quo"],
        "rpm_range": "$35 - $75",
        "hooks": [
            "Why the ultra-wealthy strictly avoid traditional status symbols...", 
            "The hidden architecture behind old money asset accumulation."
        ]
    },
    "GEOPOLITICS_MACRO": {
        "names": ["The Meridian", "Grand Strategy", "Atlas Doctrine", "Sovereign State", "New Paradigm"],
        "rpm_range": "$25 - $50",
        "hooks": [
            "The structural shifts reshaping global supply chains overnight...", 
            "What central bank balance sheets reveal about the upcoming decade."
        ]
    }
}

def initialize_branding(niche_key="FINANCE"):
    os.makedirs("config/branding", exist_ok=True)
    profile = NICHE_REGISTRY.get(niche_key, NICHE_REGISTRY["FINANCE"])
    
    brand_data = {
        "selected_niche": niche_key,
        "assigned_brand": profile["names"][0],
        "estimated_rpm": profile["rpm_range"],
        "default_hooks": profile["hooks"],
        "curated_roster": profile["names"]
    }
    
    file_path = "config/branding/active_brand.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(brand_data, f, indent=4)
        
    print(f"[+] Elite Media Branding Initialized -> Brand: '{brand_data['assigned_brand']}' | Niche: {niche_key}")
    return brand_data

if __name__ == "__main__":
    initialize_branding("FINANCE")
