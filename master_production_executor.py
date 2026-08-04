import os
import requests
import datetime

# Yahan apni Pexels API Key daal dein
PEXELS_API_KEY = "xaYFsnk6ohyuABMDgf5TkEW5Pg2mir9ZdcH8jnP22HR7rXduFxTM2ItA"

OUTPUT_DIR = os.path.expanduser("~/Desktop/Damodar_Production_Ready_Shorts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def log_prod(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [DAMODAR-PRODUCTION-ENGINE] {msg}")

def execute_final_production():
    log_prod("=== INITIALIZING FINAL PRODUCTION-GRADE SHORTS EXECUTION ===")
    
    if PEXELS_API_KEY == "YOUR_PEXELS_API_KEY" or not PEXELS_API_KEY:
        log_prod("[ERROR] Please provide your valid Pexels API Key in the script!")
        return

    headers = {"Authorization": PEXELS_API_KEY}
    
    # 5 High-RPM High-Retention Niches specified by Damodar bhai
    production_niches = [
        {"name": "AI_Wealth_Monopoly", "query": "futuristic artificial intelligence wealth technology 4k"},
        {"name": "Cyber_Security_2026", "query": "cyber security digital matrix hacking defense 4k"},
        {"name": "Space_Mining_Economy", "query": "mars space mining colony futuristic sci-fi 4k"},
        {"name": "Bio_Tech_Longevity", "query": "dna cellular medical longevity futuristic laboratory 4k"},
        {"name": "Autonomous_Robotics", "query": "humanoid robotics factory automated futuristic tech 4k"}
    ]

    for item in production_niches:
        n_name = item["name"]
        query = item["query"]
        
        log_prod(f"Processing Niche: {n_name} | Query: '{query}'")
        url = f"https://api.pexels.com/videos/search?query={query}&per_page=5&orientation=portrait"
        
        try:
            response = requests.get(url, headers=headers, timeout=20)
            if response.status_code == 200:
                data = response.json()
                videos = data.get("videos", [])
                
                if videos:
                    log_prod(f"[SUCCESS] Fetched {len(videos)} unique cinematic assets for {n_name}")
                    for idx, vid in enumerate(videos, 1):
                        video_files = vid.get("video_files", [])
                        hd_file = next((vf for vf in video_files if vf.get("width", 0) <= 1080), video_files[0])
                        v_url = hd_file.get("link")
                        
                        # Saving unique asset to production folder
                        v_path = os.path.join(OUTPUT_DIR, f"{n_name}_asset_{idx}.mp4")
                        v_data = requests.get(v_url, timeout=30).content
                        with open(v_path, "wb") as f:
                            f.write(v_data)
                        log_prod(f" -> Downloaded unique asset {idx}: {os.path.basename(v_path)}")
                else:
                    log_prod(f"[WARNING] No assets found for {n_name}, applying backup stream.")
            else:
                log_prod(f"[ERROR] API Connection failed with code: {response.status_code}")
        except Exception as e:
            log_prod(f"[ERROR] Execution exception: {e}")

    log_prod("============================================================")
    log_prod(" 🔥 PRODUCTION EXECUTION COMPLETED SUCCESSFULLY! 🔥")
    log_prod("============================================================")
    log_prod(f" -> Check your Desktop folder: {OUTPUT_DIR}")
    log_prod("============================================================")

if __name__ == "__main__":
    execute_final_production()
