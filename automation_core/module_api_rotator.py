import json
import random
import os

class FreeAPIPoolManager:
    def __init__(self, pool_file="config/api_pool.json"):
        self.pool_file = pool_file
        self.load_pool()

    def load_pool(self):
        if not os.path.exists(self.pool_file):
            os.makedirs(os.path.dirname(self.pool_file), exist_ok=True)
            default_pool = {
                "providers": [
                    {"name": "Gemini_Free", "key": "AIzaSy_DummyKey_1", "status": "active", "quota_left": 100},
                    {"name": "Groq_Llama3", "key": "gsk_DummyKey_2", "status": "active", "quota_left": 100},
                    {"name": "HuggingFace_Inference", "key": "hf_DummyKey_3", "status": "active", "quota_left": 100}
                ]
            }
            with open(self.pool_file, "w") as f:
                json.dump(default_pool, f, indent=4)
        
        with open(self.pool_file, "r") as f:
            self.data = json.load(f)

    def get_active_key(self):
        active_providers = [p for p in self.data["providers"] if p["status"] == "active" and p["quota_left"] > 0]
        if not active_providers:
            raise Exception("[!] CRITICAL: All API keys exhausted or inactive!")
        
        selected = random.choice(active_providers)
        print(f"[+] Rotated to API Provider: {selected['name']} (Quota: {selected['quota_left']})")
        return selected["key"]

if __name__ == "__main__":
    rotator = FreeAPIPoolManager()
    print("Active API Key retrieved:", rotator.get_active_key())
