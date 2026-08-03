import os
import shutil

print("==================================================")
print("   DAMODAR EMPIRE: NETLIFY MASTER DEPLOYMENT     ")
print("==================================================")

# Create a clean deployment folder containing ONLY the master UI
deploy_dir = "netlify_production_ready"
if os.path.exists(deploy_dir):
    shutil.rmtree(deploy_dir)
os.makedirs(deploy_dir, exist_ok=True)

# Copy the exact master luxury design
src_file = "damodar_website/index.html"
if os.path.exists(src_file):
    shutil.copy(src_file, os.path.join(deploy_dir, "index.html"))
    print("[SUCCESS] Master Luxury UI secured for Netlify edge deployment.")
else:
    print("[ERROR] Master UI file not found!")

print("[INFO] Installing Netlify CLI and deploying instantly...")
