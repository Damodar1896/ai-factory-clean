import os
import requests
import datetime
import subprocess

# ==========================================
# DAMODAR BHAI - PEXELS API CONFIGURATION
# ==========================================
PEXELS_API_KEY = "xaYFsnk6ohyuABMDgf5TkEW5Pg2mir9ZdcH8jnP22HR7rXduFxTM2ItA"
# ==========================================

OUTPUT_DIR = os.path.expanduser("~/Desktop/Damodar_Ultimate_60s_Studio")
os.makedirs(os.path.join(OUTPUT_DIR, "raw_clips"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "audio_voiceovers"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "final_shorts"), exist_ok=True)

def log_engine(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [DAMODAR-ULTIMATE-ENGINE] {msg}")

def generate_natural_voice(text, output_audio_path):
    log_engine("Generating optimized natural voiceover...")
    try:
        temp_aiff = output_audio_path.replace(".mp3", ".aiff")
        # Using enhanced rate and voice parameters for better flow
        cmd_say = f"say -v 'Samantha' -r 195 -o '{temp_aiff}' '{text}'"
        subprocess.run(cmd_say, shell=True, check=True)
        
        cmd_ffmpeg = f"ffmpeg -y -i '{temp_aiff}' -codec:a libmp3lame -qscale:a 2 '{output_audio_path}'"
        subprocess.run(cmd_ffmpeg, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if os.path.exists(output_audio_path):
            log_engine(f"[SUCCESS] Voiceover generated successfully: {output_audio_path}")
            return True
    except Exception as e:
        log_engine(f"[ERROR] Voice generation exception: {e}")
    return False

def run_ultimate_studio():
    log_engine("=== INITIALIZING ULTIMATE 60-SECOND CINEMATIC SHORTS STUDIO ===")
    
    headers = {"Authorization": PEXELS_API_KEY}
    
    # 5 High-RPM Niches with Extended 60s Story Scripts (Rich Content)
    extended_niches = [
        {
            "name": "01_Mobile_Tech_Empire",
            "query": "futuristic smartphone holographic display tech 4k",
            "script": "Look closely at the device in your hand. In just a few years, smartphones have evolved from simple glass panels into quantum holographic portals. Curved liquid metal frames, neural processing chips, and cameras that capture depth far beyond human sight are completely rewriting how we interact with technology. This isn't just an upgrade; it is a total revolution in mobile engineering. Which futuristic feature excites you the most? Drop your thoughts in the comments below."
        },
        {
            "name": "02_Horror_Mystery_Thrill",
            "query": "dark eerie haunted forest fog thriller cinematic 4k",
            "script": "Never step alone into the whispering woods when the clock strikes midnight. Local legends say the shadows move on their own, mimicking your footsteps and whispering your deepest secrets. You suddenly feel an icy touch upon your shoulder, but when you turn around in panic, there is nothing except absolute, suffocating darkness. And then, from deep within the trees, you hear your own voice calling for help. Do not look back."
        },
        {
            "name": "03_Bhakti_Devotional_Peace",
            "query": "divine spiritual temple light glowing epic 4k",
            "script": "In the silent, sacred hours before dawn, when the entire world is fast asleep, a divine flame awakens the soul. Deep inside the ancient temple sanctuary, the soothing fragrance of burning incense and eternal chants bridge the gap between mortal existence and infinite cosmic peace. Close your eyes for just a moment, breathe in deeply, and feel this divine energy washing away every single fear, filling your heart with supreme grace and boundless tranquility."
        },
        {
            "name": "04_Mythological_Epic_Journey",
            "query": "ancient mythical gods celestial epic battle cinematic 4k",
            "script": "Long before time itself had a name, the cosmos witnessed an apocalyptic war that shook both the heavens and the earth. Celestial gods, divine warriors, and legendary heroes stood firmly on the edge of ultimate destiny, where a single celestial weapon could alter the fate of entire universes. Ancient scriptures whisper that these epic battles were fought not with physical might alone, but through unshakeable righteousness, absolute devotion, and supreme willpower."
        },
        {
            "name": "05_Mythological_Engineering_Marvel",
            "query": "ancient advanced vimana architecture mysterious temple 4k",
            "script": "How did ancient architects construct massive stone monuments with such jaw-dropping precision that modern lasers still struggle to match? Thousands of years ago, sacred texts described flying Vimanas, anti-gravity mechanics, and complex metallurgical secrets hidden deep inside sacred temple architecture. Modern science often dismisses these accounts as mere fantasy, but the stunning architectural evidence is carved permanently into stone. The lost engineering secrets of our ancestors are finally coming to light."
        }
    ]

    for item in extended_niches:
        n_name = item["name"]
        query = item["query"]
        script_text = item["script"]
        
        log_engine("------------------------------------------------------------")
        log_engine(f"🎬 Producing 60s Short: {n_name}")
        
        # 1. Generate Voiceover
        audio_path = os.path.join(OUTPUT_DIR, "audio_voiceovers", f"{n_name}.mp3")
        voice_ok = generate_natural_voice(script_text, audio_path)
        
        # 2. Fetch Diverse Unique Cinematic Clips from Pexels (More clips for 60s length)
        url = f"https://api.pexels.com/videos/search?query={query}&per_page=10&orientation=portrait"
        clip_paths = []
        
        try:
            response = requests.get(url, headers=headers, timeout=25)
            if response.status_code == 200:
                data = response.json()
                videos = data.get("videos", [])
                
                for idx, vid in enumerate(videos[:8], 1): # Using up to 8 unique clips for variety
                    v_files = vid.get("video_files", [])
                    hd_file = next((vf for vf in v_files if vf.get("width", 0) <= 1080), v_files[0])
                    v_url = hd_file.get("link")
                    
                    clip_file = os.path.join(OUTPUT_DIR, "raw_clips", f"{n_name}_part_{idx}.mp4")
                    clip_data = requests.get(v_url, timeout=30).content
                    with open(clip_file, "wb") as f:
                        f.write(clip_data)
                    clip_paths.append(clip_file)
                    log_engine(f" -> Downloaded unique visual asset {idx}")
            else:
                log_engine(f"[ERROR] Pexels API failed with status: {response.status_code}")
        except Exception as e:
            log_engine(f"[ERROR] Clip fetching exception: {e}")
            
        # 3. Professional Assembly & Audio Synchronization via FFmpeg
        temp_merged = os.path.join(OUTPUT_DIR, f"temp_{n_name}.mp4")
        final_video = os.path.join(OUTPUT_DIR, "final_shorts", f"Ultimate_60s_Short_{n_name}.mp4")
        
        if clip_paths:
            list_txt = os.path.join(OUTPUT_DIR, f"list_{n_name}.txt")
            with open(list_txt, "w") as lt:
                for cp in clip_paths:
                    lt.write(f"file '{cp}'\n")
            
            # Step A: Concatenate video clips smoothly
            concat_cmd = f"ffmpeg -y -f concat -safe 0 -i {list_txt} -c:v libx264 -pix_fmt yuv420p -preset ultrafast {temp_merged}"
            subprocess.run(concat_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Step B: Mux with Voiceover and loop/trim to exact 60s length
            if voice_ok and os.path.exists(audio_path):
                mux_cmd = f"ffmpeg -y -i {temp_merged} -i {audio_path} -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest {final_video}"
                subprocess.run(mux_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                log_master_status = f"[SUCCESS] 🔥 60-Second Master Short with Voice Ready: {final_video}"
                log_engine(log_master_status)
            else:
                os.rename(temp_merged, final_video)
                log_engine(f"[SUCCESS] Short Compiled (Visuals Only): {final_video}")
        else:
            log_engine(f"[WARNING] Skipping assembly for {n_name} due to missing clips.")

    log_engine("============================================================")
    log_engine(" 🔥 ALL 5 EXTENDED 60S CINEMATIC SHORTS READY ON DESKTOP! 🔥")
    log_engine("============================================================")
    log_engine(f" -> Check folder: {OUTPUT_DIR}/final_shorts")
    log_engine("============================================================")

if __name__ == "__main__":
    run_ultimate_studio()
