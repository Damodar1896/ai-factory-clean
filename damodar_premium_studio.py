import os
import sys
import requests
import datetime
import subprocess

# ==========================================
# DAMODAR BHAI - PEXELS API CONFIGURATION
# ==========================================
PEXELS_API_KEY = "YAHAN_APNI_PEXELS_API_KEY_DAL_DEIN"
# ==========================================

OUTPUT_DIR = os.path.expanduser("~/Desktop/Damodar_Premium_Shorts_Studio")
os.makedirs(os.path.join(OUTPUT_DIR, "raw_clips"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "audio_voiceovers"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "final_shorts"), exist_ok=True)

def log_premium(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [DAMODAR-PREMIUM-STUDIO] {msg}")

def generate_human_voice(text, output_audio_path):
    log_premium("Generating ultra-natural human-like voiceover via Edge-TTS...")
    
    # 1. Check and install edge-tts automatically in your virtual environment
    try:
        subprocess.run(["edge-tts", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        log_premium("[INFO] edge-tts not found. Installing it now...")
        subprocess.run([sys.executable, "-m", "pip", "install", "edge-tts"], check=True, stdout=subprocess.DEVNULL)

    # 2. Generate voice (Safe execution without shell quote issues)
    try:
        # Using Microsoft's premium Aria Neural voice
        cmd = [
            "edge-tts", 
            "--voice", "en-US-AriaNeural", 
            "--rate", "+5%", 
            "--text", text, 
            "--write-media", output_audio_path
        ]
        subprocess.run(cmd, check=True)
        if os.path.exists(output_audio_path):
            log_premium(f"[SUCCESS] Natural voice generated: {output_audio_path}")
            return True
    except Exception as e:
        log_premium(f"[ERROR] Voice generation failed: {e}")
    return False

def run_premium_studio():
    log_premium("=== INITIALIZING PREMIUM 60-SECOND CINEMATIC STUDIO ===")
    
    headers = {"Authorization": PEXELS_API_KEY}
    
    # Premium Niches with Rich 60s Story Scripts
    premium_niches = [
        {
            "name": "01_Mobile_Tech_Revolution",
            "query": "futuristic holographic smartphone tech cinematic 4k drone shot",
            "script": "Look closely at the device in your hand. In just three short years, smartphones have evolved from simple glass panels into quantum holographic portals. Curved liquid metal frames, neural processors, and cameras capturing depth far beyond human sight are completely rewriting human connection. This is not just an upgrade; it is a total revolution in mobile engineering. Which futuristic feature blows your mind the most? Drop your thoughts in the comments below."
        },
        {
            "name": "02_Horror_Dark_Mystery",
            "query": "dark moody cinematic drone shot through foggy eerie pine forest 4k",
            "script": "Never step alone into the whispering woods when the clock strikes midnight. Locals whisper that shadows move on their own, mimicking your footsteps and whispering your deepest secrets. You suddenly feel an icy touch upon your shoulder, but when you turn around in panic, there is nothing except absolute darkness. And then, from deep within the trees, you hear your own voice calling for help. Do not look back."
        },
        {
            "name": "03_Bhakti_Divine_Sanctuary",
            "query": "divine glowing temple light rays spiritual sanctuary 4k",
            "script": "In the silent, sacred hours before dawn, when the entire world is fast asleep, a divine flame awakens the soul. Deep inside the ancient temple sanctuary, the soothing fragrance of burning incense and eternal chants bridge the gap between mortal existence and infinite cosmic peace. Close your eyes for just a moment, breathe in deeply, and feel this divine energy washing away every single fear, filling your heart with boundless tranquility."
        }
    ]

    for item in premium_niches:
        n_name = item["name"]
        query = item["query"]
        script_text = item["script"]
        
        log_premium("------------------------------------------------------------")
        log_premium(f"🎬 Producing Premium Short: {n_name}")
        
        # 1. Voice Generation
        audio_path = os.path.join(OUTPUT_DIR, "audio_voiceovers", f"{n_name}.mp3")
        voice_ok = generate_human_voice(script_text, audio_path)
        
        # 2. Fetch Cinematic Clips
        url = f"https://api.pexels.com/videos/search?query={query}&per_page=12&orientation=portrait"
        clip_paths = []
        
        try:
            response = requests.get(url, headers=headers, timeout=25)
            if response.status_code == 200:
                data = response.json()
                videos = data.get("videos", [])
                
                # Fetching 8 clips for better variety and 60s length
                for idx, vid in enumerate(videos[:8], 1):
                    v_files = vid.get("video_files", [])
                    hd_file = next((vf for vf in v_files if vf.get("width", 0) <= 1080), v_files[0])
                    v_url = hd_file.get("link")
                    
                    clip_file = os.path.join(OUTPUT_DIR, "raw_clips", f"{n_name}_part_{idx}.mp4")
                    clip_data = requests.get(v_url, timeout=30).content
                    with open(clip_file, "wb") as f:
                        f.write(clip_data)
                    clip_paths.append(clip_file)
                    log_premium(f" -> Downloaded cinematic visual asset {idx}")
            else:
                log_premium(f"[ERROR] Pexels API failed: {response.status_code}")
        except Exception as e:
            log_premium(f"[ERROR] Asset fetching exception: {e}")
            
        # 3. Final Assembly
        temp_merged = os.path.join(OUTPUT_DIR, f"temp_{n_name}.mp4")
        final_video = os.path.join(OUTPUT_DIR, "final_shorts", f"Premium_Short_{n_name}.mp4")
        
        if clip_paths:
            list_txt = os.path.join(OUTPUT_DIR, f"list_{n_name}.txt")
            with open(list_txt, "w") as lt:
                for cp in clip_paths:
                    lt.write(f"file '{cp}'\n")
            
            concat_cmd = f"ffmpeg -y -f concat -safe 0 -i {list_txt} -c:v libx264 -pix_fmt yuv420p -preset ultrafast {temp_merged}"
            subprocess.run(concat_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            if voice_ok and os.path.exists(audio_path):
                mux_cmd = f"ffmpeg -y -i {temp_merged} -i {audio_path} -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest {final_video}"
                subprocess.run(mux_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                log_premium(f"[SUCCESS] 🔥 Premium Cinematic Short with Natural Voice Ready: {final_video}")
            else:
                os.rename(temp_merged, final_video)
                log_premium(f"[SUCCESS] Short Compiled (Visuals Only): {final_video}")
        else:
            log_premium(f"[WARNING] Skipping assembly for {n_name} due to missing clips.")

    log_premium("============================================================")
    log_premium(" 🔥 ALL PREMIUM SHORTS READY ON DESKTOP! 🔥")
    log_premium(f" -> Check folder: {OUTPUT_DIR}/final_shorts")
    log_premium("============================================================")

if __name__ == "__main__":
    run_premium_studio()
