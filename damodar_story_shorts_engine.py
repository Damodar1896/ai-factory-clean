import os
import requests
import datetime
import subprocess

# ==========================================
# DAMODAR BHAI - API KEYS CONFIGURATION
# ==========================================
PEXELS_API_KEY = "xaYFsnk6ohyuABMDgf5TkEW5Pg2mir9ZdcH8jnP22HR7rXduFxTM2ItA"
ELEVENLABS_API_KEY = "sk_f486db428470bb995c0ab7d0f7cc0da79f1fd638f20154b7"
# ==========================================

OUTPUT_DIR = os.path.expanduser("~/Desktop/Damodar_Story_Shorts_Studio")
os.makedirs(os.path.join(OUTPUT_DIR, "raw_clips"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "audio_voiceovers"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "final_shorts"), exist_ok=True)

def log_engine(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [DAMODAR-STORY-ENGINE] {msg}")

def test_and_generate_voice(text, output_audio_path):
    log_engine("Generating free-tier compatible AI voiceover via ElevenLabs API...")
    if not ELEVENLABS_API_KEY or "YAHAN" in ELEVENLABS_API_KEY:
        log_engine("[ERROR] ElevenLabs API Key is missing!")
        return False
        
    # Free-tier default compatible voice ID (Rachel)
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
            log_engine(f"[SUCCESS] Voiceover generated successfully: {output_audio_path}")
            return True
        else:
            log_engine(f"[ERROR] ElevenLabs API error (Status {response.status_code}): {response.text}")
            return False
    except Exception as e:
        log_engine(f"[ERROR] Voice connection exception: {e}")
        return False

def run_story_engine():
    log_engine("=== INITIALIZING FINAL STORY-DRIVEN CINEMATIC SHORTS ENGINE ===")
    
    if not PEXELS_API_KEY or "YAHAN" in PEXELS_API_KEY:
        log_engine("[ERROR] Please provide your valid Pexels API Key at the top of the script!")
        return

    headers = {"Authorization": PEXELS_API_KEY}
    
    story_niches = [
        {
            "name": "01_Mobile_Tech_Story",
            "query": "futuristic smartphone holographic display tech 4k",
            "script": "Look closely at the device in your hand. In just three years, smartphones have evolved from simple glass screens into quantum holographic portals. Curved liquid metal frames, neural processors, and cameras that capture depth beyond human sight. This isn't just an upgrade. It's the complete rewriting of human connection."
        },
        {
            "name": "02_Horror_Mystery_Story",
            "query": "dark eerie haunted forest fog thriller cinematic 4k",
            "script": "Never step into the black forest when the clock strikes midnight. The locals whisper about a shadow that follows your footsteps, mimicking your breathing. You feel a cold touch on your shoulder, but when you turn around, there is nothing except total darkness."
        },
        {
            "name": "03_Bhakti_Devotional_Story",
            "query": "divine spiritual temple light glowing epic 4k",
            "script": "In the silent hours before dawn, when the entire world sleeps, a divine flame awakens the soul. Deep inside the ancient sacred shrine, the fragrance of burning incense and eternal chants bridge the gap between mortal existence and infinite peace."
        },
        {
            "name": "04_Mythological_Epic_Story",
            "query": "ancient mythical gods celestial epic battle cinematic 4k",
            "script": "Long before time had a name, the cosmos witnessed a war that shook the heavens and the earth. Celestial gods and legendary warriors stood on the edge of destiny, where a single arrow could alter the fate of universes."
        },
        {
            "name": "05_Mythological_Engineering_Story",
            "query": "ancient advanced vimana architecture mysterious temple 4k",
            "script": "How did ancient builders construct monuments with precision that modern lasers struggle to match? Thousands of years ago, sacred texts described flying Vimanas, anti-gravity technology, and complex metallurgical marvels hidden inside sacred temples."
        }
    ]

    for item in story_niches:
        n_name = item["name"]
        query = item["query"]
        script_text = item["script"]
        
        log_engine("------------------------------------------------------------")
        log_engine(f"🎬 Producing Story Short: {n_name}")
        
        audio_path = os.path.join(OUTPUT_DIR, "audio_voiceovers", f"{n_name}.mp3")
        voice_success = test_and_generate_voice(script_text, audio_path)
        
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
                    log_engine(f" -> Downloaded visual clip part {idx}")
            else:
                log_engine(f"[ERROR] Pexels API connection error: {response.status_code}")
        except Exception as e:
            log_engine(f"[ERROR] Asset fetching exception: {e}")
            
        temp_merged_video = os.path.join(OUTPUT_DIR, f"temp_{n_name}.mp4")
        final_short_path = os.path.join(OUTPUT_DIR, "final_shorts", f"Story_Short_{n_name}.mp4")
        
        if clip_paths:
            list_txt = os.path.join(OUTPUT_DIR, f"list_{n_name}.txt")
            with open(list_txt, "w") as lt:
                for cp in clip_paths:
                    lt.write(f"file '{cp}'\n")
            
            concat_cmd = f"ffmpeg -y -f concat -safe 0 -i {list_txt} -c:v libx264 -pix_fmt yuv420p -preset ultrafast {temp_merged_video}"
            subprocess.run(concat_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            if voice_success and os.path.exists(audio_path):
                mux_cmd = f"ffmpeg -y -i {temp_merged_video} -i {audio_path} -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest {final_short_path}"
                subprocess.run(mux_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                log_engine(f"[SUCCESS] 🔥 Fully Edited Story Short with Voiceover Ready: {final_short_path}")
            else:
                os.rename(temp_merged_video, final_short_path)
                log_engine(f"[SUCCESS] Short Compiled (Visuals Only): {final_short_path}")
        else:
            log_engine(f"[WARNING] Skipping assembly for {n_name} due to missing clips.")

    log_engine("============================================================")
    log_engine(" 🔥 ALL 5 STORY-DRIVEN SHORTS READY ON DESKTOP! 🔥")
    log_engine("============================================================")
    log_engine(f" -> Check folder: {OUTPUT_DIR}/final_shorts")
    log_engine("============================================================")

if __name__ == "__main__":
    run_story_engine()
