import os
import getpass

current_user = getpass.getuser()
working_dir = os.getcwd()
python_path = os.path.join(working_dir, "venv", "bin", "python")
script_path = os.path.join(working_dir, "permanent_empire_daemon.py")

plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.empire.automation.daemon</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_path}</string>
        <string>{script_path}</string>
    </array>
    <key>WorkingDirectory</key>
    <string>{working_dir}</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>{working_dir}/daemon_stdout.log</string>
    <key>StandardErrorPath</key>
    <string>{working_dir}/daemon_stderr.log</string>
</dict>
</plist>
"""

plist_dir = os.path.expanduser("~/Library/LaunchAgents")
os.makedirs(plist_dir, exist_ok=True)
plist_path = os.path.join(plist_dir, "com.empire.automation.daemon.plist")

with open(plist_path, "w") as f:
    f.write(plist_content)

print(f"[+] LaunchAgent created successfully at: {plist_path}")
print("[*] Loading service into macOS background manager...")
os.system(f"launchctl unload {plist_path} >/dev/null 2>&1")
os.system(f"launchctl load {plist_path}")
print("[✅ SUCCESS] 24x7 Permanent Empire Daemon is now registered as a native macOS Service!")
