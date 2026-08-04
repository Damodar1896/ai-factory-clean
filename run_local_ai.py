import torch
from diffusers import StableDiffusionPipeline
import datetime

print("=== RUNNING LOCAL STABLE DIFFUSION ON MAC GPU (MPS) ===")
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Target Hardware Acceleration: {device.upper()}")

# Using a lightweight, high-performance open-source model checkpoint for local testing
model_id = "runwayml/stable-diffusion-v1-5"
print(f"Loading model: {model_id}...")

try:
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id, 
        torch_dtype=torch.float16 if device == "mps" else torch.float32
    )
    pipe = pipe.to(device)
    
    prompt = "Cinematic 8K shot of a futuristic neon city, photorealistic, masterwork"
    print(f"Generating image frame with prompt: '{prompt}'...")
    
    image = pipe(prompt).images[0]
    out_path = "/Users/shubhamdewangan/Desktop/Damodar_Local_AI_Output.png"
    image.save(out_path)
    print(f"[SUCCESS] Local AI asset generated and saved to: {out_path}")
except Exception as e:
    print(f"[ERROR] Local execution notice: {e}")
