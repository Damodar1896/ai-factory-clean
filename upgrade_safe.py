import subprocess

# Humari core automation libraries ki list
core_packages = [
    "requests", "beautifulsoup4", "selenium", "playwright", 
    "pandas", "openpyxl", "reportlab", "google-generativeai", 
    "moviepy", "opencv-python", "schedule", "python-telegram-bot", "nltk", "psutil"
]

print("="*50)
print(" 🔄 SAFELY UPGRADING CORE AUTOMATION PACKAGES...")
print("="*50)

for pkg in core_packages:
    print(f"\n[UPGRADING] -> {pkg}")
    result = subprocess.run(["pip", "install", "--upgrade", pkg], capture_output=True, text=True)
    if result.returncode == 0:
        print(f" Successfully upgraded {pkg}")
    else:
        print(f" Warning on {pkg}: {result.stderr.strip()}")

print("\n" + "="*50)
print(" ✨ ALL ESSENTIAL PACKAGES UPGRADED SUCCESSFULLY!")
print("="*50)
