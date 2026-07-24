import os

with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Let's check if the root route '/' exists and update its professional UI
root_route_code = """
@app.get("/")
def home():
    html_content = \"\"\"
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Damodar Techcraze Ventures - Master Dashboard</title>
        <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    </head>
    <body class="bg-gray-950 text-white font-sans p-8">
        <div class="max-w-4xl mx-auto">
            <!-- Header Section -->
            <div class="flex justify-between items-center bg-gray-900 border border-gray-800 p-6 rounded-xl shadow-xl mb-8">
                <div>
                    <h1 class="text-2xl font-bold text-indigo-400">🏢 Damodar Techcraze Ventures</h1>
                    <p class="text-gray-400 text-sm">Enterprise Automation & Global Payment Gateway Engine</p>
                </div>
                <div class="flex gap-3">
                    <a href="/checkout" class="bg-indigo-600 hover:bg-indigo-700 px-4 py-2 rounded-lg text-sm font-semibold transition">
                        ⚡ Global Checkout
                    </a>
                </div>
            </div>

            <!-- Dashboard Stats & Quick Links Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <div class="bg-gray-900 border border-gray-800 p-6 rounded-xl shadow">
                    <h3 class="text-gray-400 text-xs font-bold uppercase mb-2">Payment Gateways</h3>
                    <p class="text-xl font-bold text-green-400">Active (5 Modes)</p>
                    <p class="text-gray-500 text-xs mt-1">GPay, PhonePe, Canara, PayPal, Crypto</p>
                </div>
                <div class="bg-gray-900 border border-gray-800 p-6 rounded-xl shadow">
                    <h3 class="text-gray-400 text-xs font-bold uppercase mb-2">Automated Invoicing</h3>
                    <p class="text-xl font-bold text-indigo-400">PDF & Live UTR</p>
                    <p class="text-gray-500 text-xs mt-1">Instant Telegram & Email Alerts</p>
                </div>
                <div class="bg-gray-900 border border-gray-800 p-6 rounded-xl shadow">
                    <h3 class="text-gray-400 text-xs font-bold uppercase mb-2">Infrastructure Status</h3>
                    <p class="text-xl font-bold text-emerald-400">100% Production Ready</p>
                    <p class="text-gray-500 text-xs mt-1">Hostinger SSL & Domain Linked</p>
                </div>
            </div>

            <!-- Quick Navigation / Modules -->
            <div class="bg-gray-900 border border-gray-800 p-6 rounded-xl shadow mb-8">
                <h3 class="text-lg font-bold text-gray-200 mb-4">🚀 Core Business Modules</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                    <a href="/checkout" class="block bg-gray-800 hover:bg-gray-700 p-4 rounded-lg border border-gray-700 transition">
                        <span class="font-bold text-indigo-300">🔗 Multi-Gateway Checkout Page</span>
                        <p class="text-gray-400 text-xs mt-1">Global & Local client payment processing.</p>
                    </a>
                    <div class="bg-gray-800 p-4 rounded-lg border border-gray-700">
                        <span class="font-bold text-emerald-300">📊 Programmatic SEO & Affiliate Bot</span>
                        <p class="text-gray-400 text-xs mt-1">Automated traffic and lead generation engine.</p>
                    </div>
                </div>
            </div>

            <!-- Footer -->
            <div class="text-center text-gray-500 text-xs">
                &copy; 2026 Damodar Techcraze Ventures. All rights reserved. Secured by 256-Bit SSL.
            </div>
        </div>
    </body>
    </html>
    \"\"\"
    from fastapi.responses import HTMLResponse
    return HTMLResponse(content=html_content)
"""

if "@app.get(\"/\")" in content:
    # Replace existing root route
    parts = content.split('@app.get("/")')
    # Find next route or end
    rest = parts[1].split('@app.get(') # rough split
    new_content = parts[0] + root_route_code + ('@app.get(' + rest[1] if len(rest) > 1 else "")
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("[Success] Master Dashboard UI updated successfully!")
else:
    with open("app.py", "a", encoding="utf-8") as f:
        f.write(root_route_code)
    print("[Success] Master Dashboard UI appended!")
