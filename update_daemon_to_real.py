import os

working_dir = os.getcwd()
python_path = os.path.join(working_dir, "venv", "bin", "python")
real_script_path = os.path.join(working_dir, "real_device_engine.py")

plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.empire.automation.daemon</string>
    <key>ProgramArguments</key>
    <array>
        <string>{python_path}</string>
        <string>{real_script_path}</string>
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

plist_path = os.path.expanduser("~/Library/LaunchAgents/com.empire.automation.daemon.plist")
with open(plist_path, "w") as f:
    f.write(plist_content)

os.system(f"launchctl unload {plist_path} >/dev/null 2>&1")
os.system(f"launchctl load {plist_path}")
print("[✅ SUCCESS] 24x7 Background Daemon is now permanently locked with the REAL Phone & IP Rotation Engine!")
