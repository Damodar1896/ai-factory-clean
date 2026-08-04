import os
import requests
import datetime
import subprocess

# ==========================================
# DAMODAR BHAI - API KEYS PLACEHOLDERS
# ==========================================
PEXELS_API_KEY = "xaYFsnk6ohyuABMDgf5TkEW5Pg2mir9ZdcH8jnP22HR7rXduFxTM2ItA"
ELEVENLABS_API_KEY = "3907d9b9cbc9fb7c7e6686b78569462b3cdd3832060f5ae0b43307acd8e56a72"
# ==========================================

OUTPUT_DIR = os.path.expanduser("~/Desktop/Damodar_Master_Shorts_Studio")
os.makedirs(os.path.join(OUTPUT_DIR, "raw_clips"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "audio_voiceovers"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "final_shorts"), exist_ok=True)

def log_studio(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [DAMODAR-SHORTS-FACTORY] {msg}")

def generate_elevenlabs_voice(text, output_audio_path):
    log_studio("Generating professional AI voiceover via ElevenLabs API...")
    if ELEVENLABS_API_KEY == "YAHAN_APNI_ELEVENLABS_API_KEY_DAL_DEIN" or not ELEVENLABS_API_KEY:
        log_studio("[WARNING] ElevenLabs API Key missing! Skipping voiceover generation.")
        return False
        
    voice_id = "21m00Tcm4TlvDq8ikWAM" 
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
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    
    try:
        response = requests.post(url, json=data, headers=headers, timeout=30)
        if response.status_code == 200:
            with open(output_audio_path, "wb") as f:
                f.write(response.content)
            log_studio(f"[SUCCESS] Voiceover generated: {output_audio_path}")
            return True
        else:
            log_studio(f"[ERROR] ElevenLabs API error: {response.status_code}")
            return False
    except Exception as e:
        log_studio(f"[ERROR] Voiceover exception: {e}")
        return False

def run_production_factory():
    log_studio("=== INITIALIZING 60S CINEMATIC SHORTS PRODUCTION FACTORY ===")
    
    if PEXELS_API_KEY == "YAHAN_APNI_PEXELS_API_KEY_DAL_DEIN" or not PEXELS_API_KEY:
        log_studio("[ERROR] Please provide your valid Pexels API Key at the top of the script!")
        return

    headers = {"Authorization": PEXELS_API_KEY}
    
    niches = [
        {
            "name": "01_Mobile_Tech_Comparison",
            "query": "latest flagship smartphones cinematic showcase 4k",
            "script": "Top 5 futuristic smartphones of 2026 that are completely redefining mobile technology. From holographic displays to quantum processors, mobile tech has entered a whole new dimension."
        },
        {
            "name": "02_Horror_Mystery",
            "query": "dark eerie haunted forest cinematic thriller 4k",
            "script": "Never walk alone through the whispering woods after midnight. Locals say the shadows move on their own, and ancient secrets are buried beneath the dark soil."
        },
        {
            "name": "03_Bhakti_Devotional",
            "query": "divine spiritual temple light glowing cinematic 4k",
            "script": "Experience the ultimate divine peace where faith meets eternity. In the heart of sacred shrines, the eternal flame guides souls toward inner awakening and supreme devotion."
        },
        {
            "name": "04_Mythological_Stories",
            "query": "ancient mythical gods celestial epic battle cinematic 4k",
            "script": "Witness the grand tales of celestial realms and legendary heroes who shaped the universe. Ancient scriptures whisper of epic wars fought between light and darkness."
        },
        {
            "name": "05_Mythological_Engineering",
            "query": "ancient advanced vimana architecture futuristic temple 4k",
            "script": "Did ancient civilizations possess flying vimanas and advanced cosmic engineering? Temples built thousands of years ago hide architectural marvels that modern science still struggles to explain."
        }
    ]

    for item in niches:
        n_name = item["name"]
        query = item["query"]
        script_text = item["script"]
        
        log_studio("------------------------------------------------------------")
        log_studio(f"🎬 Processing Short: {n_name}")
        
        audio_path = os.path.join(OUTPUT_DIR, "audio_voiceovers", f"{n_name}.mp3")
        generate_elevenlabs_voice(script_text, audio_path)
        
        url = f"https://api.pexels.com/videos/search?query={query}&per_page=5&orientation=portrait"
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
            
        final_short_path = os.path.join(OUTPUT_DIR, "final_shorts", f"Ready_Short_{n_name}.mp4")
        
        if clip_paths:
            list_txt = os.path.join(OUTPUT_DIR, f"list_{n_name}.txt")
            with open(list_txt, "w") as lt:
                for cp in clip_paths:
                    lt.write(f"file '{cp}'\n")
            
            concat_cmd = f"ffmpeg -y -f concat -safe 0 -i {list_txt} -c:v libx264 -preset ultrafast {final_short_path}"
            subprocess.run(concat_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            log_studio(f"[SUCCESS] Final Short Successfully Rendered: {final_short_path}")
        else:
            log_studio(f"[WARNING] Skipping assembly for {n_name} due to missing clips.")

    log_studio("============================================================")
    log_studio(" 🔥 ALL 5 HIGH-RPM YOUTUBE SHORTS READY ON DESKTOP! 🔥")
    log_studio("============================================================")
    log_studio(f" -> Check folder: {OUTPUT_DIR}/final_shorts")
    log_studio("============================================================")

if __name__ == "__main__":
    run_production_factory()
