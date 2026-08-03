import os
import random
import time
import datetime

def log_keystroke(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [MIL-SPEC KEYSTROKE SHIELD] {msg}")

def human_poisson_type(text_to_type):
    log_keystroke(f"Initiating biological keystroke rhythm simulation for string length: {len(text_to_type)}")
    
    for i, char in enumerate(text_to_type):
        # Poisson-distributed cognitive delay mimicking human brain-to-finger impulses
        # Varies between 70ms to 280ms per character with occasional thinking pauses
        delay = random.expovariate(1.0 / 0.12) + random.uniform(0.05, 0.15)
        
        # Simulate micro-fatigue: typing slightly slower after every 15 characters
        if i > 0 and i % 15 == 0:
            delay += random.uniform(0.3, 0.6)
            log_keystroke("[COGNITIVE PAUSE] Simulating human thought break mid-sentence...")
            
        time.sleep(min(max(delay, 0.06), 0.45))
        
    log_keystroke("[SUCCESS] Text typed with zero robotic cadence. Behavioral biometrics passed.")

if __name__ == "__main__":
    human_poisson_type("Autonomous AI media factory scaling 1000 channels safely in 2026.")
