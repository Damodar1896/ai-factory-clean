import os
import sys

try:
    from gtts import gTTS
except ImportError:
    print("[*] Installing gTTS library...")
    os.system(f"{sys.executable} -m pip install gTTS")
    from gtts import gTTS

def generate_ai_voice_pitch(client_name, niche):
    try:
        text = f"Hello {client_name}, we noticed your {niche} business has massive growth potential. Let's scale up."
        tts = gTTS(text=text, lang='en', slow=False)
        filename = f"voice_pitch_{client_name.lower().replace(' ', '_')}.mp3"
        tts.save(filename)
        print(f"[✅ SUCCESS] AI Voice Agent generated free voice pitch audio: {filename}")
        return True
    except Exception as e:
        print(f"[!] Error generating voice pitch: {e}")
        return False

if __name__ == "__main__":
    print("=== [SETTING UP MODULE 1: AI VOICE AGENT] ===")
    generate_ai_voice_pitch("Rahul Sharma", "Real Estate")
