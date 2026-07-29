import os
import time
from pathlib import Path
from gtts import gTTS

Path("automation_core/data/audio").mkdir(parents=True, exist_ok=True)
Path("automation_core/logs").mkdir(parents=True, exist_ok=True)

def log_voice(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] [AI Voice Agent] {message}"
    print(log_msg)
    with open("automation_core/logs/voice_agent.log", "a") as f:
        f.write(log_msg + "\n")

def generate_personalized_voice_pitch(client_name="Rahul Sharma", business_type="Gym"):
    log_voice("=== [SYNTHESIZING CUSTOM AI VOICE PITCH] ===")
    script_text = f"Hello {client_name}! I saw your business {business_type} and wanted to show you how our AI automation stack can scale your bookings 24/7 on autopilot. Send payment directly to damodartechcraze@okaxis to get started today."
    output_audio = f"automation_core/data/audio/voice_pitch_{client_name.lower().replace(" ", "_")}.mp3"
    log_voice(f"Converting text to speech for {client_name}...")
    tts = gTTS(text=script_text, lang="en", tld="co.in")
    tts.save(output_audio)
    log_voice(f"[✅ SUCCESS] Personalized Voice Pitch Generated: {output_audio}")
    return output_audio

if __name__ == "__main__":
    generate_personalized_voice_pitch()
