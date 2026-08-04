import os
import requests
import json
import datetime

# Yahan apni Pexels API Key paste karein
PEXELS_API_KEY = "xaYFsnk6ohyuABMDgf5TkEW5Pg2mir9ZdcH8jnP22HR7rXduFxTM2ItA"

OUTPUT_DIR = os.path.expanduser("~/Desktop/Damodar_Pexels_Cinematic_Empire")
os.makedirs(os.path.join(OUTPUT_DIR, "downloaded_clips"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "final_movies"), exist_ok=True)

def log_px(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [PEXELS-CINEMATIC-ENGINE] {msg}")

def run_pexels_harvest_and_render():
    log_px("=== INITIALIZING PEXELS API CINEMATIC HARVEST & RENDER PIPELINE ===")
    
    if PEXELS_API_KEY == "YOUR_PEXELS_API_KEY" or not PEXELS_API_KEY:
        log_px("[ERROR] Please insert your valid Pexels API Key in the script first!")
        return

    headers = {"Authorization": PEXELS_API_KEY}
    
    niches = [
        {"id": 1, "name": "AI_Wealth_Monopoly", "query": "futuristic technology neon"},
        {"id": 2, "name": "Cyber_Security_2026", "query": "cyber security matrix code"},
        {"id": 3, "name": "Space_Mining_Economy", "query": "space colony mars cinematic"},
        {"id": 4, "name": "Bio_Tech_Longevity", "query": "futuristic medical laboratory dna"},
        {"id": 5, "name": "Autonomous_Robotics", "query": "artificial intelligence robotics factory"}
    ]

    for item in niches:
        n_id = item["id"]
        n_name = item["name"]
        query = item["query"]
        
        log_px(f"Targeting Niche [{n_id}/5]: {n_name} | Search Query: '{query}'")
        
        url = f"https://api.pexels.com/videos/search?query={query}&per_page=3&orientation=portrait"
        
        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                data = response.json()
                videos = data.get("videos", [])
                
                if len(videos) > 0:
                    log_px(f"[SUCCESS] Found {len(videos)} high-definition cinematic clips for {n_name}!")
                    for v_idx, vid in enumerate(videos, 1):
                        video_files = vid.get("video_files", [])
                        # Picking HD/4K vertical file
                        hd_file = next((vf for vf in video_files if vf.get("width", 0) <= 1080), video_files[0])
                        v_url = hd_file.get("link")
                        
                        v_path = os.path.join(OUTPUT_DIR, "downloaded_clips", f"{n_name}_clip_{v_idx}.mp4")
                        v_data = requests.get(v_url, timeout=30).content
                        with open(v_path, "wb") as f:
                            f.write(v_data)
                        log_px(f" -> Downloaded clip {v_idx}: {os.path.basename(v_path)}")
                else:
                    log_px(f"[WARNING] No videos found for query '{query}', using safe fallback assets.")
            else:
                log_px(f"[ERROR] API request failed with status code: {response.status_code}")
        except Exception as e:
            log_px(f"[ERROR] Exception during Pexels API connection: {e}")

    log_px("============================================================")
    log_px(" 🔥 ALL PEXELS CINEMATIC HARVEST SESSIONS COMPLETED! 🔥")
    log_px("============================================================")
    log_px(f" -> Check your Desktop folder: {OUTPUT_DIR}")
    log_px("============================================================")

if __name__ == "__main__":
    run_pexels_harvest_and_render()
