import torch
from diffusers import LTXPipeline
from diffusers.utils import export_to_video
import datetime

print("=== INITIALIZING LOCAL LTX-VIDEO GENERATION PIPELINE ON MAC (MPS) ===")
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Target Hardware Acceleration: {device.upper()}")

model_id = "Lightricks/LTX-Video"
print(f"Loading video model: {model_id}...")

try:
    pipe = LTXPipeline.from_pretrained(
        model_id, 
        torch_dtype=torch.float16 if device == "mps" else torch.float32
    )
    pipe = pipe.to(device)
    
    prompt = "Cinematic 8K motion shot of an advanced futuristic neon city, photorealistic, masterwork, smooth camera pan"
    print(f"Generating video frames with prompt: '{prompt}'...")
    
    # Generating video output tensor
    video_frames = pipe(prompt, num_frames=16, height=384, width=256).frames
    
    out_path = "/Users/shubhamdewangan/Desktop/Damodar_Local_AI_Video_Output.mp4"
    export_to_video(video_frames, out_path, fps=8)
    
    print(f"[SUCCESS] Local AI video successfully generated and saved to: {out_path}")
except Exception as e:
    print(f"[ERROR] Local video generation error: {e}")
