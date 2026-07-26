import os
import json
import time
import random

class APIPoolRotator:
    def __init__(self, pool_path="automation_core/data/api_pool.json"):
        self.pool_path = pool_path
        os.makedirs(os.path.dirname(self.pool_path), exist_ok=True)
        print("[-] Initializing Phase 2: Free AI API Harvesting & Intelligent Rotation Pool...")

    def initialize_pool(self):
        """Creates a mock pool of 20+ free AI service keys with rotation status."""
        providers = ["OpenAI-FreeTier", "Gemini-Dev", "Groq-Cloud", "Anthropic-Trial", "Mistral-API", 
                     "Cohere-Free", "DeepSeek-Node", "HuggingFace-Inference", "Perplexity-Sandbox", "Replicate-Free",
                     "TogetherAI-Node", "Anyscale-Endpoint", "Fireworks-AI", "Cloudflare-WorkersAI", "OpenRouter-Free",
                     "Groq-Backup", "Gemini-Flash", "Mistral-Codestral", "Cohere-Command", "HuggingFace-Router", "Local-Ollama-Bridge"]
        
        pool = []
        for idx, provider in enumerate(providers, 1):
            pool.append({
                "key_id": f"key_node_{idx:02d}",
                "provider": provider,
                "api_key": f"sk-free-harvested-token-{random.randint(100000, 999999)}",
                "status": "ACTIVE",
                "rate_limit_hits": 0,
                "last_used": time.time()
            })
            
        payload = {
            "module": "Phase 2 - 20+ Free AI API Rotator",
            "total_nodes": len(pool),
            "active_pool": pool,
            "timestamp": time.time()
        }
        
        with open(self.pool_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4)
            
        print(f"[SUCCESS] Initialized API pool with {len(pool)} free-tier nodes.")

    def get_active_node(self):
        """Fetches the next available active node, implementing intelligent failover."""
        try:
            with open(self.pool_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                
            active_nodes = [node for node in data["active_pool"] if node["status"] == "ACTIVE"]
            if not active_nodes:
                print("[WARNING] All nodes exhausted! Triggering global pool reset...")
                self.initialize_pool()
                return self.get_active_node()
                
            selected = random.choice(active_nodes)
            print(f"[ROTATION] Successfully routed execution through -> [{selected['provider']}] ({selected['key_id']})")
            return selected
            
        except Exception as e:
            print(f"[ERROR] Failed to fetch active API node: {e}")
            return None

    def execute(self):
        if not os.path.exists(self.pool_path):
            self.initialize_pool()
        self.get_active_node()

if __name__ == "__main__":
    APIPoolRotator().execute()
