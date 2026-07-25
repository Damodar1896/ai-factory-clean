import os, time, subprocess, sys
from datetime import datetime

GROWTH_STACK = [
    ("trick_1_viral_loop.py", 90),
    ("trick_2_retargeting.py", 60),
    ("trick_3_affiliate_swarm.py", 120),
    ("trick_4_pseo.py", 180),
    ("trick_5_onboarding.py", 40),
    ("trick_6_upsell.py", 100),
    ("trick_7_fomo.py", 50),
    ("trick_8_community.py", 110),
    ("trick_9_behavioral_triggers.py", 70),
    ("trick_10_interactive_quiz.py", 80)
]

def log(msg):
    line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line)
    try:
        with open("global_growth_stack.log", "a") as f: f.write(line + "\n")
    except: pass

log("=== [DAMODAR GLOBAL GROWTH STACK ACTIVATED 24x7] ===")
while True:
    for script, delay in GROWTH_STACK:
        if os.path.exists(script):
            try:
                res = subprocess.run(f"pgrep -f {script}", shell=True, capture_output=True, text=True)
                if not res.stdout.strip():
                    log(f"[⚙️ LOAD-BALANCED EXECUTION] Triggering {script}...")
                    subprocess.Popen(f"{sys.executable} {script}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception as e:
                log(f"[❌ ERROR on {script}]: {e}")
        time.sleep(delay)
