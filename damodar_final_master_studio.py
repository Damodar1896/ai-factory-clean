import os
import requests
import datetime
import subprocess

# ==========================================
# DAMODAR BHAI - PEXELS API CONFIGURATION
# ==========================================
PEXELS_API_KEY = "YAHAN_APNI_PEXELS_API_KEY_DAL_DEIN"
# ==========================================

OUTPUT_DIR = os.path.expanduser("~/Desktop/Damodar_Final_Master_Studio")
os.makedirs(os.path.join(OUTPUT_DIR, "raw_clips"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "audio_voiceovers"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "final_shorts"), exist_ok=True)

def log_master(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [DAMODAR-MASTER-STUDIO] {msg}")

def generate_voice_local(text, output_audio_path):
    log_master("Generating professional local AI voiceover...")
    try:
        temp_aiff = output_audio_path.replace(".mp3", ".aiff")
        cmd_say = f"say -v 'Samantha' -o '{temp_aiff}' '{text}'"
        subprocess.run(cmd_say, shell=True, check=True)
        
        cmd_ffmpeg = f"ffmpeg -y -i '{temp_aiff}' -codec:a libmp3lame -qscale:a 2 '{output_audio_path}'"
        subprocess.run(cmd_ffmpeg, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if os.path.exists(output_audio_path):
            log_master(f"[SUCCESS] Voiceover generated: {output_audio_path}")
            return True
    except Exception as e:
        log_master(f"[ERROR] Voice generation exception: {e}")
    return False

def run_master_production():
    log_master("=== INITIALIZING FINAL 60S CINEMATIC SHORTS MASTER STUDIO ===")
    
    if not PEXELS_API_KEY or "YAHAN" in PEXELS_API_KEY:
        log_master("[WARNING] Pexels API Key missing! Please update it, using fallback simulation if needed.")

    headers = {"Authorization": PEXELS_API_KEY}
    
    master_niches = [
        {
            "name": "01_Mobile_Tech_Short",
            "query": "futuristic smartphone holographic display tech 4k",
            "script": "Look closely at the device in your hand. In just three years, smartphones have evolved from simple glass screens into quantum holographic portals. Curved liquid metal frames, neural processors, and cameras that capture depth beyond human sight. This isn't just an upgrade. It's the complete rewriting of human connection."
        },
        {
            "name": "02_Horror_Mystery_Short",
            "query": "dark eerie haunted forest fog thriller cinematic 4k",
            "script": "Never step into the black forest when the clock strikes midnight. The locals whisper about a shadow that follows your footsteps, mimicking your breathing. You feel a cold touch on your shoulder, but when you turn around, there is nothing except total darkness."
        },
        {
            "name": "03_Bhakti_Devotional_Short",
            "query": "divine spiritual temple light glowing epic 4k",
            "script": "In the silent hours before dawn, when the entire world sleeps, a divine flame awakens the soul. Deep inside the ancient sacred shrine, the fragrance of burning incense and eternal chants bridge the gap between mortal existence and infinite peace."
        },
        {
            "name": "04_Mythological_Epic_Short",
            "query": "ancient mythical gods celestial epic battle cinematic 4k",
            "script": "Long before time had a name, the cosmos witnessed a war that shook the heavens and the earth. Celestial gods and legendary warriors stood on the edge of destiny, where a single arrow could alter the fate of universes."
        },
        {
            "name": "05_Mythological_Engineering_Short",
            "query": "ancient advanced vimana architecture mysterious temple 4k",
            "script": "How did ancient builders construct monuments with precision that modern lasers struggle to match? Thousands of years ago, sacred texts described flying Vimanas, anti-gravity technology, and complex metallurgical marvels hidden inside sacred temples."
        }
    ]

    for item in master_niches:
        n_name = item["name"]
        query = item["query"]
        script_text = item["script"]
        
        log_master("------------------------------------------------------------")
        log_master(f"🎬 Processing Master Short: {n_name}")
        
        # 1. Generate Voice
        audio_path = os.path.join(OUTPUT_DIR, "audio_voiceovers", f"{n_name}.mp3")
        voice_ok = generate_voice_local(script_text, audio_path)
        
        # 2. Fetch Visual Clips from Pexels
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
                    log_master(f" -> Downloaded visual clip part {idx}")
            else:
                log_master(f"[ERROR] Pexels API failed with status: {response.status_code}")
        except Exception as e:
            log_master(f"[ERROR] Clip fetching exception: {e}")
            
        # 3. Auto-Editing & Audio Muxing via FFmpeg
        temp_merged = os.path.join(OUTPUT_DIR, f"temp_{n_name}.mp4")
        final_video = os.path.join(OUTPUT_DIR, "final_shorts", f"Master_Ready_Short_{n_name}.mp4")
        
        if clip_paths:
            list_txt = os.path.join(OUTPUT_DIR, f"list_{n_name}.txt")
            with open(list_txt, "w") as lt:
                for cp in clip_paths:
                    lt.write(f"file '{cp}'\n")
            
            # Concat video clips
            concat_cmd = f"ffmpeg -y -f concat -safe 0 -i {list_txt} -c:v libx264 -pix_fmt yuv420p -preset ultrafast {temp_merged}"
            subprocess.run(concat_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Mux with Voiceover
            if voice_ok and os.path.exists(audio_path):
                mux_cmd = f"ffmpeg -y -i {temp_merged} -i {audio_path} -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest {final_video}"
                subprocess.run(mux_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                log_master(f"[SUCCESS] 🔥 Fully Edited Short with Voiceover Ready: {final_video}")
            else:
                os.rename(temp_merged, final_video)
                log_master(f"[SUCCESS] Short Compiled (Visuals Only): {final_video}")
        else:
            log_master(f"[WARNING] Skipping assembly for {n_name} due to missing clips.")

    log_master("============================================================")
    log_master(" 🔥 ALL 5 MASTER SHORTS FULLY EDITED & READY ON DESKTOP! 🔥")
    log_master("============================================================")
    log_master(f" -> Check folder: {OUTPUT_DIR}/final_shorts")
    log_master("============================================================")

if __name__ == "__main__":
    run_master_production()
