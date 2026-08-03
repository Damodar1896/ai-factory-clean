import os
import random
import json
from fake_useragent import UserAgent

PROFILE_DIR = "/Users/shubhamdewangan/ai-factory/affiliate_bot/chrome_profiles"
os.makedirs(PROFILE_DIR, exist_ok=True)

def generate_mil_spec_fingerprint(channel_id):
    ua = UserAgent()
    
    # Randomized Screen Resolutions (High-end Mac/Windows profiles)
    resolutions = [
        {"width": 1920, "height": 1080},
        {"width": 2560, "height": 1440},
        {"width": 3840, "height": 2160}
    ]
    res = random.choice(resolutions)
    
    # WebGL Vendors & Renderers spoofing for hardware masking
    gpu_vendors = ["Google Inc. (Apple)", "Intel Inc.", "AMD", "NVIDIA Corporation"]
    gpu_renderers = [
        "ANGLE (Apple, Apple M2, OpenGL ES 3.1)",
        "ANGLE (Intel, Intel Iris OpenGL Engine)",
        "ANGLE (NVIDIA, NVIDIA GeForce RTX 4090 OpenGL Engine)"
    ]
    
    fingerprint = {
        "channel_id": channel_id,
        "user_agent": ua.random,
        "screen_width": res["width"],
        "screen_height": res["height"],
        "device_scale_factor": random.choice([1, 2]),
        "webgl_vendor": random.choice(gpu_vendors),
        "webgl_renderer": random.choice(gpu_renderers),
        "canvas_noise_seed": random.randint(1000, 99999),
        "audio_context_noise": random.uniform(0.0001, 0.0099),
        "timezone": "UTC",
        "locale": "en-US,en;q=0.9",
        "proxy": f"http://residential_proxy_node_{random.randint(100,999)}:1080"
    }
    
    profile_path = os.path.join(PROFILE_DIR, f"fingerprint_{channel_id}.json")
    with open(profile_path, "w") as f:
        json.dump(fingerprint, f, indent=4)
        
    print(f"[MIL-SPEC SECURITY] Unique Anti-Detect Fingerprint locked for Channel: {channel_id}")
    return profile_path

if __name__ == "__main__":
    # Test generation for Channel 1 & 2
    generate_mil_spec_fingerprint("channel_alpha_01")
    generate_mil_spec_fingerprint("channel_alpha_02")
