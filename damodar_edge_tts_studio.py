import os
import asyncio
import datetime
import subprocess
import requests

# ==========================================
# DAMODAR BHAI - PEXELS API CONFIGURATION
# ==========================================
PEXELS_API_KEY = "xaYFsnk6ohyuABMDgf5TkEW5Pg2mir9ZdcH8jnP22HR7rXduFxTM2ItA"
# ==========================================

OUTPUT_DIR = os.path.expanduser("~/Desktop/Damodar_Edge_TTS_Studio")
os.makedirs(os.path.join(OUTPUT_DIR, "raw_clips"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "audio_voiceovers"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "final_shorts"), exist_ok=True)

def log_studio(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [DAMODAR-EDGE-STUDIO] {msg}")

async def generate_edge_tts_voice(text, output_audio_path):
    log_studio("Generating ultra-natural voiceover via Edge-TTS...")
    try:
        import edge_tts
        # Using Microsoft's natural English/Hindi neural voice (Swara for Hindi/En or Aria/en-US)
        voice = "en-US-AriaNeural" # Extremely professional and human-like
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_audio_path)
        if os.path.exists(output_audio_path):
            log_studio(f"[SUCCESS] Natural voice generated: {output_audio_path}")
            return True
    except ImportError:
        log_studio("[WARNING] edge-tts package not found. Installing it automatically...")
        subprocess.run("pip install edge-tts", shell=True, check=True)
        return await generate_edge_tts_voice(text, output_audio_path)
    except Exception as e:
        log_studio(f"[ERROR] Edge-TTS exception: {e}")
    return False

def run_edge_studio():
    log_studio("=== INITIALIZING EDGE-TTS & CINEMATIC VISUALS STUDIO ===")
    
    headers = {"Authorization": PEXELS_API_KEY}
    
    # High-RPM Niches with Cinematic Queries & Rich 60s Story Scripts
    cinematic_niches = [
        {
            "name": "01_Mobile_Tech_Future",
            "query": "futuristic holographic smartphone tech cinematic 4k drone shot",
            "script": "Look closely at the device in your hand. In just three short years, smartphones have evolved from simple glass panels into quantum holographic portals. Curved liquid metal frames, neural processors, and cameras capturing depth far beyond human sight are rewriting human connection. This isn't just an upgrade; it's a total revolution. Which futuristic feature blows your mind?"
        },
        {
            "name": "02_Horror_Dark_Woods",
            "query": "dark moody cinematic drone shot through foggy eerie pine forest 4k",
            "script": "Never step alone into the whispering woods when the clock strikes midnight. Locals whisper that shadows move on their own, mimicking your footsteps and whispering secrets. You feel an icy touch upon your shoulder, but when you turn around in panic, there is nothing except absolute darkness. And then, from deep within the trees, you hear your own voice calling for help. Do not look back."
        },
        {
            "name": "03_Bhakti_Divine_Peace",
            "query": "divine glowing temple light rays spiritual sanctuary 4k",
            "script": "In the silent, sacred hours before dawn, when the entire world sleeps, a divine flame awakens the soul. Deep inside the ancient temple sanctuary, the soothing fragrance of burning incense and eternal chants bridge the gap between mortal existence and infinite peace. Close your eyes, breathe in deeply, and feel this divine energy washing away every single fear."
        }
    ]

    for item in cinematic_niches:
        n_name = item["name"]
        query = item["query"]
        script_text = item["script"]
        
        log_studio("------------------------------------------------------------")
        log_studio(f"🎬 Processing Cinematic Short: {n_name}")
        
        # 1. Generate Natural Voice via Edge-TTS (run inside synchronous loop)
        audio_path = os.path.join(OUTPUT_DIR, "audio_voiceovers", f"{n_name}.mp3")
        voice_ok = asyncio.run(generate_edge_tts_voice(script_text, audio_path))
        
        # 2. Fetch High-End Cinematic 4K/HD Clips from Pexels
        url = f"https://api.pexels.com/videos/search?query={query}&per_page=8&orientation=portrait"
        clip_paths = []
        
        try:
            response = requests.get(url, headers=headers, timeout=25)
            if response.status_code == 200:
                data = response.json()
                videos = data.get("videos", [])
                
                for idx, vid in enumerate(videos[:6], 1):
                    v_files = vid.get("video_files", [])
                    hd_file = next((vf for vf in v_files if vf.get("width", 0) <= 1080), v_files[0])
                    v_url = hd_file.get("link")
                    
                    clip_file = os.path.join(OUTPUT_DIR, "raw_clips", f"{n_name}_part_{idx}.mp4")
                    clip_data = requests.get(v_url, timeout=30).content
                    with open(clip_file, "wb") as f:
                        f.write(clip_data)
                    clip_paths.append(clip_file)
                    log_studio(f" -> Downloaded cinematic clip part {idx}")
            else:
                log_studio(f"[ERROR] Pexels API failed with code: {response.status_code}")
        except Exception as e:
            log_studio(f"[ERROR] Visual asset fetching exception: {e}")
            
        # 3. Final Assembly & Synchronization via FFmpeg
        temp_merged = os.path.join(OUTPUT_DIR, f"temp_{n_name}.mp4")
        final_video = os.path.join(OUTPUT_DIR, "final_shorts", f"Cinematic_Short_{n_name}.mp4")
        
        if clip_paths:
            list_txt = os.path.join(OUTPUT_DIR, f"list_{n_name}.txt")
            with open(list_txt, "w") as lt:
                for cp in clip_paths:
                    lt.write(f"file '{cp}'\n")
            
            # Concat video clips with ultrafast preset
            concat_cmd = f"ffmpeg -y -f concat -safe 0 -i {list_txt} -c:v libx264 -pix_fmt yuv420p -preset ultrafast {temp_merged}"
            subprocess.run(concat_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Mux with Natural Voiceover
            if voice_ok and os.path.exists(audio_path):
                mux_cmd = f"ffmpeg -y -i {temp_merged} -i {audio_path} -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest {final_video}"
                subprocess.run(mux_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                log_studio(f"[SUCCESS] 🔥 Cinematic Short with Natural Voice Ready: {final_video}")
            else:
                os.rename(temp_merged, final_video)
                log_studio(f"[SUCCESS] Short Compiled (Visuals Only): {final_video}")
        else:
            log_studio(f"[WARNING] Skipping assembly for {n_name} due to missing clips.")

    log_studio("============================================================")
    log_studio(" 🔥 ALL CINEMATIC SHORTS WITH NATURAL VOICE READY ON DESKTOP! 🔥")
    log_studio("============================================================")
    log_studio(f" -> Check folder: {OUTPUT_DIR}/final_shorts")
    log_studio("============================================================")

if __name__ == "__main__":
    run_edge_studio()
