import os
import requests
import datetime
import subprocess

# ==========================================
# DAMODAR BHAI - FINAL PRODUCTION API KEYS
# ==========================================
PEXELS_API_KEY = "xaYFsnk6ohyuABMDgf5TkEW5Pg2mir9ZdcH8jnP22HR7rXduFxTM2ItA"
ELEVENLABS_API_KEY = "sk_f486db428470bb995c0ab7d0f7cc0da79f1fd638f20154b7"
# ==========================================

OUTPUT_DIR = os.path.expanduser("~/Desktop/Damodar_Master_Shorts_Studio")
os.makedirs(os.path.join(OUTPUT_DIR, "raw_clips"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "audio_voiceovers"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "final_shorts"), exist_ok=True)

def log_studio(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [DAMODAR-MASTER-STUDIO] {msg}")

def generate_elevenlabs_voice(text, output_audio_path):
    log_studio("Generating professional AI voiceover via ElevenLabs API...")
    if not ELEVENLABS_API_KEY or "YAHAN" in ELEVENLABS_API_KEY:
        log_studio("[ERROR] ElevenLabs API Key is missing or default! Please update it.")
        return False
        
    voice_id = "21m00Tcm4TlvDq8ikWAM" # Adam / Professional Cinematic Voice
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.6,
            "similarity_boost": 0.8
        }
    }
    
    try:
        response = requests.post(url, json=data, headers=headers, timeout=30)
        if response.status_code == 200:
            with open(output_audio_path, "wb") as f:
                f.write(response.content)
            log_studio(f"[SUCCESS] Voiceover generated successfully: {output_audio_path}")
            return True
        else:
            log_studio(f"[ERROR] ElevenLabs API error code {response.status_code}: {response.text}")
            return False
    except Exception as e:
        log_studio(f"[ERROR] Voiceover exception: {e}")
        return False

def run_production_factory():
    log_studio("=== INITIALIZING ULTIMATE 60S SHORTS AUTO-EDITING FACTORY ===")
    
    if not PEXELS_API_KEY or "YAHAN" in PEXELS_API_KEY:
        log_studio("[ERROR] Please provide your valid Pexels API Key in the script!")
        return

    headers = {"Authorization": PEXELS_API_KEY}
    
    niches = [
        {
            "name": "01_Mobile_Tech_Comparison",
            "query": "latest flagship smartphones cinematic showcase 4k",
            "script": "Top 5 futuristic smartphones of 2026 that are completely redefining mobile technology. From holographic displays to quantum processors, mobile tech has entered a whole new dimension. Which one is your absolute favorite? Let us know in the comments."
        },
        {
            "name": "02_Horror_Mystery",
            "query": "dark eerie haunted forest cinematic thriller 4k",
            "script": "Never walk alone through the whispering woods after midnight. Locals say the shadows move on their own, and ancient secrets are buried beneath the dark soil. If you hear someone calling your name in the dark... do not look back."
        },
        {
            "name": "03_Bhakti_Devotional",
            "query": "divine spiritual temple light glowing cinematic 4k",
            "script": "Experience the ultimate divine peace where faith meets eternity. In the heart of sacred shrines, the eternal flame guides souls toward inner awakening and supreme devotion. Feel the divine energy transform your entire existence."
        },
        {
            "name": "04_Mythological_Stories",
            "query": "ancient mythical gods celestial epic battle cinematic 4k",
            "script": "Witness the grand tales of celestial realms and legendary heroes who shaped the universe. Ancient scriptures whisper of epic wars fought between light and darkness, where destiny itself bowed before supreme willpower."
        },
        {
            "name": "05_Mythological_Engineering",
            "query": "ancient advanced vimana architecture futuristic temple 4k",
            "script": "Did ancient civilizations possess flying vimanas and advanced cosmic engineering? Temples built thousands of years ago hide architectural marvels that modern science still struggles to explain. Unlocking secrets of our ancestors."
        }
    ]

    for item in niches:
        n_name = item["name"]
        query = item["query"]
        script_text = item["script"]
        
        log_studio("------------------------------------------------------------")
        log_studio(f"🎬 Processing Niche: {n_name}")
        
        # 1. Generate Voiceover
        audio_path = os.path.join(OUTPUT_DIR, "audio_voiceovers", f"{n_name}.mp3")
        voice_success = generate_elevenlabs_voice(script_text, audio_path)
        
        # 2. Fetch Cinematic Stock Clips
        url = f"https://api.pexels.com/videos/search?query={query}&per_page=6&orientation=portrait"
        clip_paths = []
        
        try:
            response = requests.get(url, headers=headers, timeout=20)
            if response.status_code == 200:
                data = response.json()
                videos = data.get("videos", [])
                
                for idx, vid in enumerate(videos, 1):
                    v_files = vid.get("video_files", [])
                    hd_file = next((vf for vf in v_files if vf.get("width", 0) <= 1080), v_files[0])
                    v_url = hd_file.get("link")
                    
                    clip_file = os.path.join(OUTPUT_DIR, "raw_clips", f"{n_name}_part_{idx}.mp4")
                    clip_data = requests.get(v_url, timeout=30).content
                    with open(clip_file, "wb") as f:
                        f.write(clip_data)
                    clip_paths.append(clip_file)
                    log_studio(f" -> Downloaded asset part {idx}")
            else:
                log_studio(f"[ERROR] Pexels API failed with status: {response.status_code}")
        except Exception as e:
            log_studio(f"[ERROR] Asset harvesting exception: {e}")
            
        # 3. Final Auto-Editing & Rendering via FFmpeg
        temp_merged_video = os.path.join(OUTPUT_DIR, f"temp_{n_name}.mp4")
        final_short_path = os.path.join(OUTPUT_DIR, "final_shorts", f"Ready_Short_{n_name}.mp4")
        
        if clip_paths:
            list_txt = os.path.join(OUTPUT_DIR, f"list_{n_name}.txt")
            with open(list_txt, "w") as lt:
                for cp in clip_paths:
                    lt.write(f"file '{cp}'\n")
            
            # Merge video clips together
            concat_cmd = f"ffmpeg -y -f concat -safe 0 -i {list_txt} -c:v libx264 -pix_fmt yuv420p -preset ultrafast {temp_merged_video}"
            subprocess.run(concat_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Auto-Edit: Muxing the video with ElevenLabs Voiceover (if available)
            if voice_success and os.path.exists(audio_path):
                mux_cmd = f"ffmpeg -y -i {temp_merged_video} -i {audio_path} -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest {final_short_path}"
                subprocess.run(mux_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                log_studio(f"[SUCCESS] Fully Edited Short with Voiceover Compiled: {final_short_path}")
            else:
                # Fallback if voice failed
                os.rename(temp_merged_video, final_short_path)
                log_studio(f"[SUCCESS] Short Compiled (Visuals Only): {final_short_path}")
        else:
            log_studio(f"[WARNING] Skipping assembly for {n_name} due to missing clips.")

    log_studio("============================================================")
    log_studio(" 🔥 ALL 5 FULLY EDITED 60S YOUTUBE SHORTS READY ON DESKTOP! 🔥")
    log_studio("============================================================")
    log_studio(f" -> Check folder: {OUTPUT_DIR}/final_shorts")
    log_studio("============================================================")

if __name__ == "__main__":
    run_production_factory()
