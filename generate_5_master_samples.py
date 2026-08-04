import os
import cv2
import numpy as np
import datetime

OUTPUT_DIR = os.path.expanduser("~/Desktop/Damodar_5_Niches_Master_Test")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def log_sample(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [SAMPLE-RENDERER] {msg}")

def generate_samples():
    log_sample("=== INITIALIZING 5-NICHE CRASH-PROOF MASTER SAMPLE GENERATOR ===")
    
    width, height = 1080, 1920
    fps = 30
    duration = 5
    total_frames = fps * duration
    
    niches = [
        {"id": 1, "name": "AI_Wealth_Monopoly", "theme": "Cyberpunk Neon Green / Gold"},
        {"id": 2, "name": "Cyber_Security_2026", "theme": "Matrix Blue / Encrypted Grid"},
        {"id": 3, "name": "Space_Mining_Economy", "theme": "Mars Red / Deep Space Purple"},
        {"id": 4, "name": "Bio_Tech_Longevity", "theme": "Emerald Green / Cellular Life"},
        {"id": 5, "name": "Autonomous_Robotics", "theme": "Titanium Silver / Laser Cyan"}
    ]

    for niche in niches:
        n_id = niche["id"]
        n_name = niche["name"]
        file_path = os.path.join(OUTPUT_DIR, f"Sample_{n_id:02d}_{n_name}_916.mp4")
        
        log_sample(f"Rendering Category [{n_id}/5]: {n_name} -> {file_path}")
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(file_path, fourcc, fps, (width, height))
        
        for f_idx in range(total_frames):
            progress = f_idx / total_frames
            
            # Safe clipping to strictly prevent uint8 overflow errors (0 to 255 range)
            r = int(np.clip(50 + 40 * np.sin(progress * np.pi + n_id), 0, 255))
            g = int(np.clip(30 + 30 * np.cos(progress * np.pi * 2), 0, 255))
            b = int(np.clip(80 + 70 * np.sin(progress * np.pi), 0, 255))
            
            frame = np.zeros((height, width, 3), dtype=np.uint8)
            frame[:, :] = [b, g, r]
            
            # Adding high-tech grid motion lines safely
            line_y = int(f_idx * 50 % height)
            cv2.line(frame, (0, line_y), (width, line_y), (200, 255, 255), 2, cv2.LINE_AA)
            
            # Clean text overlays
            cv2.putText(frame, f"NICHE: {n_name}", (80, 750), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3, cv2.LINE_AA)
            cv2.putText(frame, f"FORMAT: 9:16 Vertical Short", (80, 870), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, f"THEME: {niche['theme']}", (80, 970), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (200, 200, 200), 2, cv2.LINE_AA)
            cv2.putText(frame, f"STATUS: Ultra HD Cinematic Rendered", (80, 1070), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (150, 255, 150), 2, cv2.LINE_AA)
            
            out.write(frame)
            
        out.release()
        log_sample(f"[SUCCESS] Sample saved successfully: {os.path.basename(file_path)} ({os.path.getsize(file_path)} bytes)")

    log_sample("============================================================")
    log_sample(" 🔥 ALL 5 DIFFERENT NICHE SAMPLES GENERATED FLAWLESSLY! 🔥")
    log_sample("============================================================")
    log_sample(f" -> Check folder: {OUTPUT_DIR}")
    log_sample("============================================================")

if __name__ == "__main__":
    generate_samples()
