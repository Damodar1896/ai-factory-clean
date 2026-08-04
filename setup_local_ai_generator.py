import os
import subprocess
import datetime

def log_setup(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [LOCAL-AI-SETUP] {msg}")

def install_and_verify_local_ai():
    log_setup("=== INITIALIZING LOCAL AI DIFFUSION PIPELINE SETUP FOR MAC (M2/M3) ===")
    
    # 1. Installing Hugging Face Diffusers, Transformers, and Accelerate for Apple Silicon MPS
    log_setup("Installing PyTorch, Diffusers, and Transformers packages...")
    subprocess.run([
        "pip", "install", "--quiet", 
        "torch", "torchvision", "torchaudio", 
        "diffusers", "transformers", "accelerate", "safetensors", "imageio"
    ], check=True)
    
    log_setup("[SUCCESS] All required AI diffusion libraries installed successfully!")
    
    # 2. Creating local model execution directory
    model_dir = os.path.expanduser("~/ai-factory/local_models")
    os.makedirs(model_dir, exist_ok=True)
    
    # 3. Writing the local execution runner script
    runner_code = """import torch
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
"""
    
    runner_path = os.path.expanduser("~/ai-factory/run_local_ai.py")
    with open(runner_path, "w") as f:
        f.write(runner_code)
        
    log_setup(f"[SUCCESS] Local AI execution runner locked at: {runner_path}")
    log_setup("=== SETUP COMPLETED! READY TO EXECUTE LOCALLY ===")

if __name__ == "__main__":
    install_and_verify_local_ai()
