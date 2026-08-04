import torch
import numpy as np
from diffusers import LTXPipeline
from diffusers.utils import export_to_video

print("=== RUNNING FIXED LTX-VIDEO EXPORTER ===")
device = "mps" if torch.backends.mps.is_available() else "cpu"

model_id = "Lightricks/LTX-Video"
print(f"Loading model from cache: {model_id}...")

try:
    pipe = LTXPipeline.from_pretrained(
        model_id, 
        torch_dtype=torch.float16 if device == "mps" else torch.float32
    )
    pipe = pipe.to(device)
    
    prompt = "Cinematic 8K motion shot of an advanced futuristic neon city, photorealistic, masterwork, smooth camera pan"
    print(f"Generating frames for prompt: '{prompt}'...")
    
    # Generating output tensor
    output = pipe(prompt, num_frames=16, height=384, width=256)
    video_frames = output.frames
    
    # FIX: Explicitly converting PyTorch tensor/list to clean NumPy ndarray format to bypass export error
    if isinstance(video_frames, torch.Tensor):
        video_frames = video_frames.detach().cpu().numpy()
    elif isinstance(video_frames, list):
        video_frames = np.array([np.array(f) for f in video_frames])
    
    out_path = "/Users/shubhamdewangan/Desktop/Damodar_Local_AI_Video_Output.mp4"
    export_to_video(video_frames, out_path, fps=8)
    
    print(f"[SUCCESS] Video successfully fixed, exported and saved to: {out_path}")
except Exception as e:
    print(f"[ERROR] Export error fixed check: {e}")
