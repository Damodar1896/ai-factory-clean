import os
import json

ROOT_DIR = "/Users/shubhamdewangan/ai-factory"

def audit_empire():
    print("============================================================")
    print("       DAMODAR EMPIRE - DEEP SYSTEM AUDIT & FILE DISCOVERY   ")
    print("============================================================")
    
    python_files = []
    json_files = []
    log_files = []
    other_files = []
    
    total_size = 0
    
    for root, dirs, files in os.walk(ROOT_DIR):
        # venv aur .git ko skip kar dete hain taaki unnecessary clutter na aaye
        if "venv" in root or ".git" in root or "__pycache__" in root:
            continue
            
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, ROOT_DIR)
            try:
                file_size = os.path.getsize(file_path)
                total_size += file_size
            except:
                file_size = 0
                
            if file.endswith(".py"):
                python_files.append((rel_path, file_size))
            elif file.endswith(".json") or file.endswith(".db"):
                json_files.append((rel_path, file_size))
            elif file.endswith(".log"):
                log_files.append((rel_path, file_size))
            else:
                other_files.append((rel_path, file_size))

    print(f"\n[+] Total Python Execution Scripts Found: {len(python_files)}")
    print("------------------------------------------------------------")
    for f, size in sorted(python_files):
        print(f"  (Py) -> {f} ({size // 1024} KB)")

    print(f"\n[+] Total Databases & Config Vaults Found: {len(json_files)}")
    print("------------------------------------------------------------")
    for f, size in sorted(json_files):
        print(f"  (Data) -> {f} ({size // 1024} KB)")

    print(f"\n[+] Total Asset & Other Files Found: {len(other_files)}")
    print("------------------------------------------------------------")
    for f, size in sorted(other_files):
        print(f"  (Asset) -> {f} ({size // 1024} KB)")

    print("\n============================================================")
    print(f" SUMMARY: Total Empire Footprint Size: {total_size / (1024*1024):.2f} MB")
    print("============================================================")

if __name__ == "__main__":
    audit_empire()
