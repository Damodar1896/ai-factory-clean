import os

# Scan karne ke liye folders (Aap chahein toh path badal sakte hain)
folders_to_check = [
    os.path.expanduser("~/Downloads"),
    os.path.expanduser("~/Documents"),
    os.path.expanduser("~/Desktop")
]

MIN_SIZE_MB = 50  # 50 MB se badi files ko dhoondega
min_size_bytes = MIN_SIZE_MB * 1024 * 1024

print("="*60)
print(f" 🔍 SCANNING FOR FILES LARGER THAN {MIN_SIZE_MB} MB 🔍")
print("="*60)

found_files = []

for folder in folders_to_check:
    if not os.path.exists(folder):
        continue
    print(f"\nScanning folder: {folder}...")
    for root, dirs, files in os.walk(folder):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                file_size = os.path.getsize(filepath)
                if file_size > min_size_bytes:
                    size_mb = file_size / (1024 * 1024)
                    found_files.append((size_mb, filepath))
            except (PermissionError, FileNotFoundError):
                continue

# Size ke hisab se descending order mein sort karna (Sabse badi file sabse upar)
found_files.sort(key=lambda x: x[0], reverse=True)

print("\n" + "="*60)
print(" 📦 TOP HEAVY FILES FOUND:")
print("="*60)
for size, path in found_files[:20]:  # Top 20 sabse badi files dikhayega
    print(f"  [{size:.2f} MB] -> {path}")

print("="*60)
print("Aap inme se jo files kaam ki nahi hain, unhe manually delete ya Google Drive par move kar sakte hain!")
