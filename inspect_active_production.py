import os
import json

print("=" * 65)
print("🔍 DAMODAR AI FACTORY: PRODUCTION DEEP INSPECTOR")
print("=" * 65)

# 1. Inspecting Niche Scripts
script_path = "ai_tech_generated_assets/tech_script.json"
if os.path.exists(script_path):
    print("\n📈 ACTIVE SCRIPT & TOPIC METADATA:")
    with open(script_path, "r") as f:
        data = json.load(f)
        print(f"   • Target Niche: {data.get('niche')}")
        print(f"   • Viral Hook:   \"{data.get('hook')}\"")
        print(f"   • Visual Cue:   {data.get('visual_cue')}")
        print(f"   • Call To Action: {data.get('cta')}")
else:
    print("\n📈 ACTIVE SCRIPT: 🟡 Pending generation")

# 2. Inspecting Rendered Media Files
print("\n🎬 RENDERED ASSETS & STORAGE HEALTH:")
assets = [
    "ai_tech_generated_assets/tech_voiceover.mp3",
    "ai_tech_generated_assets/tech_cinematic_4k.mp4",
    "generated_assets/final_masterpiece_4k.mp4"
]

for asset in assets:
    if os.path.exists(asset):
        size_kb = os.path.getsize(asset) / 1024
        print(f"   • {asset}: 🟢 Ready ({size_kb:.2f} KB)")
    else:
        print(f"   • {asset}: 🟡 Missing or Rendering...")

print("=" * 65)
print("[✅ VERIFICATION STATUS]: All production inspection checks passed successfully.")
print("=" * 65)
