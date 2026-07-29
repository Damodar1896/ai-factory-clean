import shutil
import os

print(">>> SYNCING MASTER LUXURY UI TO PRODUCTION ROOT <<<")

# Copy the exact master UI file to root index.html
if os.path.exists("damodar_website/index.html"):
    shutil.copy("damodar_website/index.html", "index.html")
    shutil.copy("damodar_website/index.html", "public_deployment_dist/index.html")
    print("[SUCCESS] Master UI copied successfully to root and dist!")
else:
    print("[ERROR] damodar_website/index.html not found!")
