import os
import json
import random

print("=== [ACTIVATING PER-CHANNEL PERSISTENCE & DEVICE LOCKING ENGINE] ===")

class PerChannelSecurityManager:
    def __init__(self):
        self.vault_file = "channel_security_vault.json"
        self.load_vault()

    def load_vault(self):
        """Loads existing channel security profiles or initializes an empty vault."""
        if os.path.exists(self.vault_file):
            with open(self.vault_file, "r") as f:
                self.vault = json.load(f)
        else:
            self.vault = {}

    def save_vault(self):
        """Saves the locked channel profiles to ensure permanent persistence."""
        with open(self.vault_file, "w") as f:
            json.dump(self.vault, f, indent=4)

    def get_or_create_channel_profile(self, channel_name):
        """Ensures a brand channel ALWAYS uses its own permanent, locked hardware & MAC fingerprint."""
        if channel_name in self.vault:
            profile = self.vault[channel_name]
            print(f"\n[🔒 PERSISTENCE LOCKED] Recognized existing channel: [{channel_name}]")
            print(f"   • Locked MAC Address: {profile['mac_address']}")
            print(f"   • Locked GPU Profile: {profile['gpu_renderer']}")
            print(f"   • Locked CPU Cores:   {profile['cpu_cores']} Cores")
            print(f"[✅ SAFE] Using exact same hardware signature to prevent platform suspicion.")
            return profile
        else:
            print(f"\n[🆕 NEW CHANNEL DETECTED] Provisioning isolated hardware profile for: [{channel_name}]...")
            
            # Generate a brand new, unique hardware identity for this specific channel
            new_profile = {
                "channel_name": channel_name,
                "mac_address": f"02:42:{random.randint(10,99)}:{random.randint(10,99)}:{random.randint(10,99)}:02",
                "gpu_renderer": random.choice([
                    "Apple M3 Max Integrated Graphics",
                    "NVIDIA GeForce RTX 4090 Laptop GPU",
                    "Intel Iris Xe Graphics Family",
                    "AMD Radeon Pro 5600M"
                ]),
                "cpu_cores": random.choice([8, 12, 16]),
                "status": "Permanent Hardware Lock Active"
            }
            
            self.vault[channel_name] = new_profile
            self.save_vault()
            
            print(f"[✨ SUCCESS] New hardware fingerprint permanently bound to [{channel_name}]!")
            print(f"   • Assigned MAC: {new_profile['mac_address']}")
            print(f"   • Assigned GPU: {new_profile['gpu_renderer']}")
            return new_profile

if __name__ == "__main__":
    manager = PerChannelSecurityManager()
    
    # Testing Per-Channel Persistence across multiple channels
    channels = ["Damodar_AI_Tech", "Dubai_Luxury_RealEstate", "Crypto_Wealth_2026"]
    
    for ch in channels:
        # First call creates the permanent profile
        manager.get_or_create_channel_profile(ch)
        # Second call proves that it reuses the EXACT same profile (Persistence Check)
        manager.get_or_create_channel_profile(ch)

    print("\n=== [PER-CHANNEL DEVICE LOCKING ENGINE FULLY LOCKED] ===")
