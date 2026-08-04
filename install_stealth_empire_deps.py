import os
import datetime

def log_installer(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] [STEALTH-INSTALLER] {msg}")

def install_all_stealth_dependencies():
    log_installer("=== INSTALLING PLAYWRIGHT STEALTH & AUTOMATION DEPENDENCIES ===")
    
    # 1. Installing required Python packages
    os.system("pip install --quiet playwright playwright-stealth requests")
    
    # 2. Installing Playwright Chromium browser binaries for headless/headful stealth execution
    log_installer("Downloading and installing Playwright browser binaries...")
    os.system("playwright install chromium")
    
    log_installer("[SUCCESS] All stealth automation packages and browser binaries installed successfully!")

if __name__ == "__main__":
    install_all_stealth_dependencies()
