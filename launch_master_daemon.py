import time
import subprocess

def run():
    while True:
        try:
            subprocess.run(["python", "automation_core/master_orchestrator.py"], check=True)
        except Exception:
            time.sleep(60)

if __name__ == "__main__":
    run()
