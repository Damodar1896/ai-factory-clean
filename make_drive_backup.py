import os
import shutil

# Desktop par 'MacBook Backup 2026' folder banana
backup_folder = os.path.expanduser("~/Desktop/MacBook Backup 2026")
os.makedirs(backup_folder, exist_ok=True)

# Kahan-kahan se files uthani hain (Downloads folder)
downloads_dir = os.path.expanduser("~/Downloads")

# Move karne ke liye keywords ya extensions (Jo heavy ya backup hain)
items_to_backup = [
    "Takeout", 
    ".mp4", 
    "AI developed", 
    "Takeout 2", 
    "Takeout 3", 
    "Takeout 4"
]

print("="*50)
print(" 📦 MOVING FILES TO 'MacBook Backup 2026' FOLDER...")
print("="*50)

moved_count = 0
for item in os.listdir(downloads_dir):
    item_path = os.path.join(downloads_dir, item)
    
    # Check karna ki kya ye wahi heavy/backup files hain
    if any(keyword in item for keyword in items_to_backup):
        dest_path = os.path.join(backup_folder, item)
        try:
            if os.path.exists(dest_path):
                # Agar pehle se hai toh skip ya overwrite
                continue
            shutil.move(item_path, dest_path)
            print(f" Moved to Backup: {item}")
            moved_count += 1
        except Exception as e:
            print(f" Error moving {item}: {e}")

print("="*50)
print(f" Success! Total {moved_count} items moved to Desktop/MacBook Backup 2026")
print("="*50)
