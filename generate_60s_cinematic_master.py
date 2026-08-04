import os
import cv2
import numpy as np
import datetime

OUTPUT_DIR = os.path.expanduser("~/Desktop/Damodar_60s_Cinematic_Master")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def log_master(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [60S-CINEMATIC-MASTER] {msg}")

def generate_60s_videos():
    log_master("=== INITIALIZING 60-SECOND MULTI-NICHE CINEMATIC GENERATOR ===")
    
    width, height = 1080, 1920
    fps = 30
    duration_seconds = 60  # Exactly 60 seconds per video
    total_frames = fps * duration_seconds
    
    niches = [
        {"id": 1, "name": "AI_Wealth_Monopoly", "color": (0, 255, 120), "hook": "The $10B Autonomous Economy Blueprint"},
        {"id": 2, "name": "Cyber_Security_2026", "color": (255, 80, 50), "hook": "Military-Grade Zero Trust Defense Grid"},
        {"id": 3, "name": "Space_Mining_Economy", "color": (180, 50, 255), "hook": "Deep Core Asteroid Extraction Live"},
        {"id": 4, "name": "Bio_Tech_Longevity", "color": (50, 220, 255), "hook": "Cellular Rejuvenation & Immortality"},
        {"id": 5, "name": "Autonomous_Robotics", "color": (0, 165, 255), "hook": "Neural Swarm Smart Manufacturing"}
    ]

    for item in niches:
        n_id = item["id"]
        n_name = item["name"]
        base_color = item["color"]
        file_path = os.path.join(OUTPUT_DIR, f"60s_Master_{n_id:02d}_{n_name}_916.mp4")
        
        log_master(f"Rendering 60-Second Master [{n_id}/5]: {n_name} (1800 Frames) -> {file_path}")
        
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(file_path, fourcc, fps, (width, height))
        
        for f_idx in range(total_frames):
            progress = f_idx / total_frames
            
            # Safe gradient background calculation (0 to 255 uint8 safe)
            bg = np.zeros((height, width, 3), dtype=np.uint8)
            for y in range(height):
                factor = y / height
                r = int(np.clip(base_color[0] * (1.0 - factor) + 40 * np.sin(progress * np.pi + factor * 2), 0, 255))
                g = int(np.clip(base_color[1] * factor + 30 * np.cos(progress * np.pi), 0, 255))
                b = int(np.clip(base_color[2] * 0.6 + 50 * np.sin(progress * np.pi * 3), 0, 255))
                bg[y, :, :] = [b, g, r]
                
            frame = bg.copy()
            
            # Dynamic Cyber Grid Animation
            grid_size = 140
            offset = int((f_idx * 4) % grid_size)
            for x in range(0, width, grid_size):
                cv2.line(frame, (x + offset, 0), (x + offset, height), (80, 80, 80), 1, cv2.LINE_AA)
            for y_line in range(0, height, grid_size):
                cv2.line(frame, (0, y_line + offset), (width, y_line + offset), (80, 80, 80), 1, cv2.LINE_AA)
                
            # Animated Central Core Pulse
            cx, cy = width // 2, height // 2 - 150
            radius = int(280 + 50 * np.sin(progress * np.pi * 10))
            cv2.circle(frame, (cx, cy), radius, (base_color[0], base_color[1], base_color[2]), 4, cv2.LINE_AA)
            cv2.circle(frame, (cx, cy), radius - 40, (255, 255, 255), 2, cv2.LINE_AA)
            
            # Timeline & Progress Bar at bottom
            bar_width = int(width * progress)
            cv2.rectangle(frame, (0, height - 30), (bar_width, height), (0, 255, 255), -1)
            
            # Dynamic Text & Overlays
            cv2.putText(frame, f"NICHE: {n_name.upper()}", (70, 1250), cv2.FONT_HERSHEY_DUPLEX, 1.3, (255, 255, 255), 3, cv2.LINE_AA)
            cv2.putText(frame, item["hook"], (70, 1350), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (base_color[0], base_color[1], base_color[2]), 2, cv2.LINE_AA)
            cv2.putText(frame, f"DURATION: {f_idx // 30}s / 60s (9:16 Short)", (70, 1470), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (200, 200, 200), 2, cv2.LINE_AA)
            cv2.putText(frame, "STATUS: FREE AUTOMATION PIPELINE ACTIVE", (70, 1550), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (150, 255, 150), 2, cv2.LINE_AA)
            
            out.write(frame)
            
        out.release()
        log_master(f"[SUCCESS] 60-Second video generated: {os.path.basename(file_path)} ({os.path.getsize(file_path)} bytes)")

    log_master("============================================================")
    log_master(" 🔥 ALL 5 DIFFERENT 60-SECOND CINEMATIC VIDEOS READY! 🔥")
    log_master("============================================================")
    log_master(f" -> Check folder: {OUTPUT_DIR}")
    log_master("============================================================")

if __name__ == "__main__":
    generate_60s_videos()
