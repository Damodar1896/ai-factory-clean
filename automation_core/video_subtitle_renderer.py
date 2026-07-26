import os
from pathlib import Path
from gtts import gTTS
from moviepy import ColorClip, CompositeVideoClip, AudioFileClip, TextClip

Path("automation_core/data").mkdir(parents=True, exist_ok=True)
Path("automation_core/logs").mkdir(parents=True, exist_ok=True)

def generate_video_with_subtitles(script_text, output_filename="automation_core/data/output_short.mp4"):
    print("[*] Step 1: Synthesizing AI Voiceover (100% Free)...")
    audio_path = "automation_core/data/temp_voiceover.mp3"
    tts = gTTS(text=script_text, lang='en', tld='co.in')
    tts.save(audio_path)
    
    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration
    
    print(f"[*] Step 2: Rendering 9:16 Vertical Video (Duration: {duration:.2f}s)...")
    bg_clip = ColorClip(size=(1080, 1920), color=(15, 15, 15)).with_duration(duration)
    
    print("[*] Step 3: Injecting High-Retention Dynamic Subtitles...")
    txt_clip = TextClip(
        text=script_text, 
        font="Arial",
        font_size=65, 
        color='yellow', 
        size=(900, None)
    ).with_duration(duration).with_position(('center', 'center'))
    
    video = CompositeVideoClip([bg_clip, txt_clip]).with_audio(audio_clip).with_duration(duration)
    
    print("[*] Step 4: Exporting Final Video File...")
    video.write_videofile(
        output_filename, 
        fps=24, 
        codec='libx264', 
        audio_codec='aac', 
        preset='ultrafast', 
        logger=None
    )
    
    print(f"[✅ SUCCESS] High-Retention Video Rendered Successfully: {output_filename}")

if __name__ == "__main__":
    sample_hook = "Stop scrolling! Automate your business 24x7 with AI and collect direct UPI payments at damodartechcraze@okaxis instantly."
    generate_video_with_subtitles(sample_hook)
