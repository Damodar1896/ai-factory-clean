import json
import os
from flask import Flask, render_template_string

app = Flask(__name__)
DATABASE_FILE = "business_empire_master_db.json"
LOG_FILE = "system_activity.log"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Damodar Tech Craze - Live Empire Command Center</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: Arial, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }
        .container { max-width: 1200px; margin: auto; }
        h1 { color: #38bdf8; text-align: center; }
        .stats { display: flex; justify-content: space-between; margin-bottom: 20px; }
        .card { background: #1e293b; padding: 20px; border-radius: 8px; text-align: center; width: 22%; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
        .card h3 { margin: 0; color: #94a3b8; font-size: 14px; }
        .card p { font-size: 24px; font-weight: bold; color: #34d399; margin: 10px 0 0 0; }
        .section-box { background: #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
        .section-box h2 { color: #38bdf8; margin-top: 0; font-size: 18px; }
        table { width: 100%; border-collapse: collapse; background: #1e293b; border-radius: 8px; overflow: hidden; }
        th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #334155; }
        th { background: #334155; color: #f1f5f9; }
        tr:hover { background: #273548; }
        .badge { padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; background: #0284c7; color: #e0f2fe; }
        .log-stream { background: #090d16; color: #34d399; padding: 15px; border-radius: 6px; font-family: monospace; height: 120px; overflow-y: auto; font-size: 13px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Damodar Tech Craze Live Empire Command Center</h1>
        <div class="stats">
            <div class="card"><h3>Total Leads</h3><p>{{ total }}</p></div>
            <div class="card"><h3>Pitched Leads</h3><p>{{ pitched }}</p></div>
            <div class="card"><h3>Payment Sent</h3><p>{{ payment_sent }}</p></div>
            <div class="card"><h3>Replies / Samples</h3><p>{{ replies }}</p></div>
        </div>

        <div class="section-box">
            <h2>🔴 Live System Activity & Error Stream (Auto-Refreshing)</h2>
            <div class="log-stream">
                {% for log in logs %}
                <div>> [{{ log.get('event', 'INFO') }}] {{ log.get('message', '') }} (Target: {{ log.get('target', 'System') }})</div>
                {% endfor %}
            </div>
        </div>

        <div class="section-box">
            <h2>📊 Live Business Leads Pipeline</h2>
            <table>
                <tr>
                    <th>Business Name</th>
                    <th>Niche</th>
                    <th>City</th>
                    <th>Email</th>
                    <th>Status</th>
                </tr>
                {% for lead in leads[:15] %}
                <tr>
                    <td>{{ lead.get('business_name', 'N/A') }}</td>
                    <td>{{ lead.get('niche', 'N/A') }}</td>
                    <td>{{ lead.get('city', 'N/A') }}</td>
                    <td>{{ lead.get('email', 'N/A') }}</td>
                    <td><span class="badge">{{ lead.get('status', 'Fresh') }}</span></td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    leads = json.load(open(DATABASE_FILE)) if os.path.exists(DATABASE_FILE) else []
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            for line in f:
                try:
                    logs.append(json.loads(line.strip()))
                except:
                    pass
    
    total = len(leads)
    pitched = sum(1 for l in leads if l.get("status") == "Pro_Email_Sent")
    payment_sent = sum(1 for l in leads if l.get("status") == "Payment_Instructions_Sent")
    replies = sum(1 for l in leads if l.get("reply_status") == "Sample_Sent")
    
    return render_template_string(HTML_TEMPLATE, leads=leads[::-1], total=total, pitched=pitched, payment_sent=payment_sent, replies=replies, logs=logs[::-1])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
