import os
import shutil
import json
from datetime import datetime

BACKUP_DIR = os.path.expanduser("~/ai-factory/affiliate_bot/encrypted_backups")
SOURCE_FILES = [
    os.path.expanduser("~/ai-factory/affiliate_bot/secure_emails.json"),
    os.path.expanduser("~/ai-factory/affiliate_bot/conversion_tracking.json")
]
SOURCE_DIRS = [
    os.path.expanduser("~/ai-factory/content_engine/generated_pages")
]

def run_backup():
    print("--- Initializing Automated Backup & Disaster Recovery System ---")
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
        
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    target_folder = os.path.join(BACKUP_DIR, f"backup_{timestamp}")
    os.makedirs(target_folder)
    
    backed_up_count = 0
    
    # Backup individual JSON database files
    for file_path in SOURCE_FILES:
        if os.path.exists(file_path):
            shutil.copy(file_path, target_folder)
            backed_up_count += 1
            print(f" -> [Backed Up File]: {os.path.basename(file_path)}")
            
    # Backup generated content directories
    for dir_path in SOURCE_DIRS:
        if os.path.exists(dir_path):
            dest_dir = os.path.join(target_folder, os.path.basename(dir_path))
            shutil.copytree(dir_path, dest_dir)
            backed_up_count += 1
            print(f" -> [Backed Up Directory]: {os.path.basename(dir_path)}")
            
    print(f"[Success] Backup completed successfully! Securely stored at: {target_folder}")
    return target_folder

if __name__ == "__main__":
    run_backup()
