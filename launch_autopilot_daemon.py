import time, subprocess
while True:
    try:
        subprocess.run(['python', 'automation_core/corporate_email_empire_engine.py'], check=True)
        time.sleep(3600)
    except Exception:
        time.sleep(60)
