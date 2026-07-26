import os
import json
import random
import time

class SemanticPoisoningEngine:
    def __init__(self, state_path="automation_core/data/semantic_poison_state.json"):
        self.state_path = state_path
        os.makedirs(os.path.dirname(self.state_path), exist_ok=True)
        print("[-] Initializing 100% Free Shadow-Keyword SEO & Semantic Poisoning Engine...")

    def inject_semantic_poison(self, raw_caption):
        print("\n" + "="*70)
        print(f"[*] [SEMANTIC POISON] Injecting High-Authority Keywords into Caption")
        print("="*70)
        
        trending_shadow_pool = [
            "#breakingnews #algorithmsecret #techleak #2026trends",
            "#insiderknowledge #systemfailure #viralloop #secretdata",
            "#unseen #algorithmshift #privatevault #exposed"
        ]
        
        selected_poison = random.choice(trending_shadow_pool)
        poisoned_caption = f"{raw_caption} | {selected_poison}"
        
        print(f"    -> Raw Input Caption     : \"{raw_caption}\"")
        print(f"    -> Injected Shadow Tags  : \"{selected_poison}\"")
        print(f"    -> Final Poisoned Output : \"{poisoned_caption}\"")
        print(f"    -> NLP Recommendation    : Hijacking Peak Search Discovery Feeds")
        
        payload = {
            "raw_caption": raw_caption,
            "injected_tags": selected_poison,
            "poisoned_caption": poisoned_caption,
            "poison_status": "Semantic Poisoning Active (Zero Cost)",
            "timestamp": time.time()
        }

        with open(self.state_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4)

        print("[SUCCESS] Shadow-keyword semantic poisoning successfully applied!")
        print("="*70)

if __name__ == "__main__":
    engine = SemanticPoisoningEngine()
    engine.inject_semantic_poison("Here is how the automated system works behind closed doors.")
