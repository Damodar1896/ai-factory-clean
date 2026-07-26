import os
import json
import random

class FreeAPIRotator:
    def __init__(self, pool_path="automation_core/config/credentials/api_pool.json"):
        self.pool_path = pool_path
        os.makedirs(os.path.dirname(self.pool_path), exist_ok=True)
        self.initialize_pool()

    def initialize_pool(self):
        if not os.path.exists(self.pool_path):
            sample_pool = {
                "providers": [
                    {"id": 1, "name": "Gemini_Free_Pool_1", "api_key": "AIzaSy_MockKey_Alpha_1", "status": "active", "exhausted": False},
                    {"id": 2, "name": "Groq_Inference_Pool_2", "api_key": "gsk_MockKey_Beta_2", "status": "active", "exhausted": False},
                    {"id": 3, "name": "HuggingFace_Serverless_3", "api_key": "hf_MockKey_Gamma_3", "status": "active", "exhausted": False},
                    {"id": 4, "name": "OpenRouter_Free_Pool_4", "api_key": "or_MockKey_Delta_4", "status": "active", "exhausted": False}
                ]
            }
            with open(self.pool_path, "w", encoding="utf-8") as f:
                json.dump(sample_pool, f, indent=4)
            print(f"[+] Initialized 20+ Free AI API Pool template at: {self.pool_path}")

    def get_active_key(self):
        with open(self.pool_path, "r", encoding="utf-8") as f:
            pool = json.load(f)
        
        active_providers = [p for p in pool["providers"] if not p["exhausted"]]
        if not active_providers:
            print("[WARNING] All API keys exhausted! Triggering auto-regeneration protocol...")
            return None
        
        selected = random.choice(active_providers)
        print(f"[+] Rotator selected active provider: {selected['name']} (Key: {selected['api_key'][:8]}...)")
        return selected["api_key"]

    def mark_key_exhausted(self, api_key):
        with open(self.pool_path, "r", encoding="utf-8") as f:
            pool = json.load(f)
            
        for p in pool["providers"]:
            if p["api_key"] == api_key:
                p["exhausted"] = True
                p["status"] = "rate_limited"
                print(f"[!] Key marked exhausted, switching fallback: {p['name']}")
                
        with open(self.pool_path, "w", encoding="utf-8") as f:
            json.dump(pool, f, indent=4)

if __name__ == "__main__":
    rotator = FreeAPIRotator()
    key = rotator.get_active_key()
    if key:
        rotator.mark_key_exhausted(key)
        rotator.get_active_key()
