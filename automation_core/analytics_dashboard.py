import os
import json
from pathlib import Path
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

DATA_DIR = Path("automation_core/data")
LOGS_DIR = Path("automation_core/logs")

@app.route("/")
def dashboard():
    # Read recent logs
    master_log = "Last 10 automation events running cleanly."
    log_path = LOGS_DIR / "master_daemon.log"
    if log_path.exists():
        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            master_log = "".join(lines[-10:])
            
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Damodar Empire - Command & Analytics Dashboard</title>
        <meta http-equiv="refresh" content="10">
        <style>
            body { font-family: monospace; background: #0f172a; color: #38bdf8; padding: 20px; }
            h1 { color: #facc15; }
            .card { background: #1e293b; padding: 15px; margin-bottom: 15px; border-radius: 8px; border: 1px solid #334155; }
            pre { color: #cbd5e1; white-space: pre-wrap; }
            .highlight { color: #4ade80; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>🚀 DAMODAR EMPIRE ANALYTICS DASHBOARD</h1>
        <div class="card">
            <h3>💳 Primary Revenue & Payment Gateway</h3>
            <p>• UPI ID: <span class="highlight">damodartechcraze@okaxis</span> (100% Direct Payout)</p>
            <p>• Bank Routing: Canara Bank (9232698947@cnrb)</p>
        </div>
        <div class="card">
            <h3>📊 Live Automation & System Logs</h3>
            <pre>{{ master_log }}</pre>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, master_log=master_log)

if __name__ == "__main__":
    print("[*] Starting Analytics Dashboard on http://127.0.0.1:5000 ...")
    app.run(host="0.0.0.0", port=5000, debug=False)
