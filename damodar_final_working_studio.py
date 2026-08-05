import os
import sys
import requests
import datetime
import subprocess

# ==========================================
# DAMODAR BHAI - PEXELS API CONFIGURATION
# ==========================================
PEXELS_API_KEY = "xaYFsnk6ohyuABMDgf5TkEW5Pg2mir9ZdcH8jnP22HR7rXduFxTM2ItA"
# ==========================================

OUTPUT_DIR = os.path.expanduser("~/Desktop/Damodar_Working_Shorts_Studio")
os.makedirs(os.path.join(OUTPUT_DIR, "raw_clips"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "audio_voiceovers"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "final_shorts"), exist_ok=True)

def log_studio(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [DAMODAR-WORKING-STUDIO] {msg}")

def generate_human_voice(text, output_audio_path):
    log_studio("Generating ultra-natural human voiceover via Edge-TTS...")
    
    # Ensure edge-tts is installed in the virtual environment
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "edge-tts"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

    try:
        cmd = [
            "edge-tts", 
            "--voice", "en-US-AriaNeural", 
            "--rate", "+5%", 
            "--text", text, 
            "--write-media", output_audio_path
        ]
        subprocess.run(cmd, check=True)
        if os.path.exists(output_audio_path):
            log_studio(f"[SUCCESS] Natural voice generated: {output_audio_path}")
            return True
    except Exception as e:
        log_studio(f"[ERROR] Voice generation failed: {e}")
    return False

def run_working_studio():
    log_studio("=== INITIALIZING WORKING 60-SECOND CINEMATIC STUDIO ===")
    
    headers = {"Authorization": PEXELS_API_KEY}
    
    cinematic_niches = [
        {
            "name": "01_Mobile_Tech_Revolution",
            "query": "futuristic holographic smartphone tech cinematic 4k drone shot",
            "script": "Look closely at the device in your hand. In just three short years, smartphones have evolved from simple glass panels into quantum holographic portals. Curved liquid metal frames, neural processors, and cameras capturing depth far beyond human sight are completely rewriting human connection. This is not just an upgrade; it is a total revolution in mobile engineering. Which futuristic feature blows your mind the most? Drop your thoughts in the comments below."
        },
        {
            "name": "02_Horror_Dark_Mystery",
            "query": "dark moody cinematic drone shot through foggy eerie pine forest 4k",
            "script": "Never step alone into the whispering woods when the clock strikes midnight. Locals whisper that shadows move on their own, mimicking your footsteps and whispering your deepest secrets. You suddenly feel an icy touch upon your shoulder, but when you turn around in panic, there is nothing except absolute darkness. And then, from deep within the trees, you hear your own voice calling for help. Do not look back."
        }
    ]

    for item in cinematic_niches:
        n_name = item["name"]
        query = item["query"]
        script_text = item["script"]
        
        log_studio("------------------------------------------------------------")
        log_studio(f"🎬 Processing Short: {n_name}")
        
        # 1. Voice Generation
        audio_path = os.path.join(OUTPUT_DIR, "audio_voiceovers", f"{n_name}.mp3")
        voice_ok = generate_human_voice(script_text, audio_path)
        
        # 2. Fetch Cinematic Clips from Pexels
        url = f"https://api.pexels.com/videos/search?query={query}&per_page=12&orientation=portrait"
        clip_paths = []
        
        try:
            response = requests.get(url, headers=headers, timeout=25)
            if response.status_code == 200:
                data = response.json()
                videos = data.get("videos", [])
                
                for idx, vid in enumerate(videos[:8], 1):
                    v_files = vid.get("video_files", [])
                    hd_file = next((vf for vf in v_files if vf.get("width", 0) <= 1080), v_files[0])
                    v_url = hd_file.get("link")
                    
                    clip_file = os.path.join(OUTPUT_DIR, "raw_clips", f"{n_name}_part_{idx}.mp4")
                    clip_data = requests.get(v_url, timeout=30).content
                    with open(clip_file, "wb") as f:
                        f.write(clip_data)
                    clip_paths.append(clip_file)
                    log_studio(f" -> Downloaded cinematic visual asset {idx}")
            else:
                log_studio(f"[ERROR] Pexels API failed with status code: {response.status_code}")
        except Exception as e:
            log_studio(f"[ERROR] Asset fetching exception: {e}")
            
        # 3. Final Assembly & Audio Muxing
        temp_merged = os.path.join(OUTPUT_DIR, f"temp_{n_name}.mp4")
        final_video = os.path.join(OUTPUT_DIR, "final_shorts", f"Working_Short_{n_name}.mp4")
        
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
                log_studio(f"[SUCCESS] 🔥 Fully Edited Short with Natural Voice Ready: {final_video}")
            else:
                os.rename(temp_merged, final_video)
                log_studio(f"[SUCCESS] Short Compiled (Visuals Only): {final_video}")
        else:
            log_studio(f"[WARNING] Skipping assembly for {n_name} due to missing clips.")

    log_studio("============================================================")
    log_studio(" 🔥 ALL WORKING SHORTS READY ON DESKTOP! 🔥")
    log_studio(f" -> Check folder: {OUTPUT_DIR}/final_shorts")
    log_studio("============================================================")

if __name__ == "__main__":
    run_working_studio()
