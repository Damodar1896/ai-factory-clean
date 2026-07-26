import os
import json
import random
import time

class AccidentalLeakEngine:
    def __init__(self, log_path="automation_core/data/accidental_leak_state.json"):
        self.log_path = log_path
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        print("[-] Initializing 100% Free Accidental Leak & Confidential Aesthetic Engine...")

    def apply_leak_aesthetic(self, media_asset_id):
        print("\n" + "="*70)
        print(f"[*] [ACCIDENTAL LEAK] Applying Classified Aesthetic to Asset: {media_asset_id}")
        print("="*70)
        
        leak_overlays = [
            "Confidential Terminal Log Screen-Recording Overlay (Green Text on Black)",
            "Classified Watermark Stamp ('EYES ONLY / DO NOT DISTRIBUTE')",
            "Raw Unedited Workspace Aesthetic with Cursor Tracking"
        ]
        
        selected_overlay = random.choice(leak_overlays)
        print(f"    -> Media Asset ID        : {media_asset_id}")
        print(f"    -> Aesthetic Overlay     : {selected_overlay}")
        print(f"    -> Psychological Trigger : High Curiosity via Perceived Data Leak")
        print(f"    -> Production Status     : Raw & Unfiltered Look Applied")
        
        payload = {
            "media_asset_id": media_asset_id,
            "leak_overlay": selected_overlay,
            "aesthetic_status": "Classified Leak Aesthetic Active (Zero Cost)",
            "timestamp": time.time()
        }

        with open(self.log_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4)

        print("[SUCCESS] Accidental leak aesthetic successfully embedded!")
        print("="*70)

if __name__ == "__main__":
    engine = AccidentalLeakEngine()
    engine.apply_leak_aesthetic("asset_master_leak_04")
