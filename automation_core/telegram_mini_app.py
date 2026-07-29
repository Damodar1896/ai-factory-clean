import os
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def mini_app_store():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Damodar Tech Craze - Mini-App Store</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        :root { --bg-color: #18222d; --card-bg: #212e3e; --text-color: #ffffff; --accent-color: #2ea6ff; --secondary-text: #8a9ba8; }
        body { background-color: var(--bg-color); color: var(--text-color); font-family: sans-serif; margin: 0; padding: 15px; }
        .header { text-align: center; margin-bottom: 20px; }
        .header h1 { font-size: 22px; margin: 5px 0; color: #facc15; }
        .product-card { background-color: var(--card-bg); border-radius: 12px; padding: 15px; margin-bottom: 12px; border: 1px solid #2f3e53; }
        .product-title { font-size: 16px; font-weight: bold; margin-bottom: 5px; }
        .price { font-size: 15px; font-weight: bold; color: var(--accent-color); }
        .buy-btn { background-color: var(--accent-color); color: white; border: none; padding: 8px 16px; border-radius: 8px; font-weight: bold; cursor: pointer; }
        .upi-box { background: #111827; border: 1px dashed #facc15; padding: 10px; border-radius: 8px; text-align: center; margin-top: 20px; font-size: 12px; color: #facc15; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 Damodar Tech Craze Empire</h1>
        <p>Automated AI Tools & B2B Growth Stack</p>
    </div>
    <div class="product-card">
        <div class="product-title">⚡ Autonomous AI Video Bot</div>
        <div class="price">₹1,999</div>
        <button class="buy-btn" onclick="alert("UPI Pay to: damodartechcraze@okaxis")">Instant Buy</button>
    </div>
    <div class="upi-box">💳 Direct UPI Payment: <b>damodartechcraze@okaxis</b></div>
</body>
</html>"""
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
