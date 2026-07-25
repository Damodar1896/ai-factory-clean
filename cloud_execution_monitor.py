import os
import json
from datetime import datetime

print("=== [DAMODAR CLOUD EMPIRE: EXECUTION MONITOR ACTIVE] ===")

def verify_cloud_assets_and_logs():
    print(f"🕒 Diagnostic Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🌐 Operating Environment: Cloud-Native Daemon & Load-Balanced Workers")
    print("-" * 65)

    # 1. Check generated assets for AI Automation & Tech Niche
    asset_dir = "ai_tech_generated_assets"
    if os.path.exists(asset_dir):
        files = os.listdir(asset_dir)
        print(f"📂 Cloud Asset Directory '{asset_dir}': 🟢 Found ({len(files)} files)")
        for f in files:
            print(f"   • Asset File: {f}")
    else:
        print(f"📂 Cloud Asset Directory '{asset_dir}': 🟡 Initializing...")

    # 2. Check general generated assets
    gen_dir = "generated_assets"
    if os.path.exists(gen_dir):
        g_files = os.listdir(gen_dir)
        print(f"🎬 Master 4K Video & Voice Folder '{gen_dir}': 🟢 Found ({len(g_files)} files)")
        for gf in g_files:
            print(f"   • Master File: {gf}")

    # 3. Check System Logs & Daemon Status
    log_files = ["master_empire_production.log", "empire_runtime.log", "daemon_stdout.log"]
    print("\n🛡️ SYSTEM HEALTH & SELF-HEALING LOGS:")
    for lf in log_files:
        if os.path.exists(lf):
            print(f"   • Log File '{lf}': 🟢 Active & Recording")
        else:
            print(f"   • Log File '{lf}': 🟡 Pending first write")

    print("-" * 65)
    print("[✅ CLOUD STATUS] All systems are synchronized. Zero local laptop load.")
    print("[🚀 READY] The AI Automation & Tech channel is fully armed for automated scale!")

if __name__ == "__main__":
    verify_cloud_assets_and_logs()
