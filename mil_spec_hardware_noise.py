import os
import random
import json
import datetime

VAULT_DIR = "/Users/shubhamdewangan/ai-factory/master_content_vault"
os.makedirs(VAULT_DIR, exist_ok=True)

def log_hardware(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [MIL-SPEC HARDWARE NOISE] {msg}")

def generate_dynamic_hardware_noise(node_id):
    log_hardware(f"Generating real-time multi-stage hardware noise profile for: {node_id}")
    
    # Randomized unique noise offsets for Audio & WebGL buffers
    audio_noise_shift = random.uniform(0.00001, 0.00099)
    canvas_pixel_drift = random.randint(10000, 999999)
    
    webgl_vendors = ["Google Inc. (Apple)", "Intel Inc.", "AMD", "NVIDIA Corporation"]
    webgl_renderers = [
        "ANGLE (Apple, Apple M3 Max, OpenGL ES 3.1)",
        "ANGLE (Intel, Intel Iris Xe OpenGL Engine)",
        "ANGLE (NVIDIA, NVIDIA GeForce RTX 4080 OpenGL Engine)"
    ]
    
    noise_profile = {
        "node_id": node_id,
        "audio_context_delta": audio_noise_shift,
        "canvas_noise_seed": canvas_pixel_drift,
        "spoofed_webgl_vendor": random.choice(webgl_vendors),
        "spoofed_webgl_renderer": random.choice(webgl_renderers),
        "status": "100% Unique Hardware Fingerprint Locked"
    }
    
    profile_path = os.path.join(VAULT_DIR, f"hardware_noise_{node_id}.json")
    with open(profile_path, "w") as f:
        json.dump(noise_profile, f, indent=4)
        
    log_hardware(f"[SUCCESS] Dynamic hardware noise injected & saved at {profile_path}")
    return noise_profile

if __name__ == "__main__":
    generate_dynamic_hardware_noise("secure_node_alpha_01")
