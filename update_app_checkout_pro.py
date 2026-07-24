import os

with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace checkout route with multi-gateway & dynamic QR pro version
pro_checkout_code = """
@app.get("/checkout")
def upi_checkout():
    html_content = \"\"\"
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Pro Checkout - Damodar Tech Empire</title>
        <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    </head>
    <body class="bg-gray-950 text-white font-sans p-6">
        <div class="max-w-xl mx-auto bg-gray-900 border border-gray-800 p-8 rounded-xl shadow-2xl mt-6">
            <h1 class="text-2xl font-bold mb-1 text-indigo-400">⚡ Damodar Tech Pro Checkout</h1>
            <p class="text-gray-400 text-sm mb-6">Choose your preferred payment method or generate a dynamic amount QR.</p>
            
            <!-- Gateway Selector Tabs -->
            <div class="grid grid-cols-3 gap-2 mb-6">
                <button onclick="switchTab('gpay')" id="btn-gpay" class="py-2 px-3 bg-indigo-600 text-xs font-semibold rounded-lg transition">Google Pay</button>
                <button onclick="switchTab('phonepe')" id="btn-phonepe" class="py-2 px-3 bg-gray-800 text-xs font-semibold rounded-lg transition">PhonePe</button>
                <button onclick="switchTab('canara')" id="btn-canara" class="py-2 px-3 bg-gray-800 text-xs font-semibold rounded-lg transition">Canara Bank</button>
            </div>

            <!-- Tab 1: Google Pay -->
            <div id="tab-gpay" class="payment-tab bg-white text-gray-900 p-6 rounded-xl text-center mb-6">
                <h3 class="font-bold text-gray-800 mb-2">Google Pay (GPay)</h3>
                <div class="bg-gray-100 p-4 rounded-lg inline-block mb-3">
                    <p class="text-xs font-mono text-gray-600 mb-1">Subhash Dewangan</p>
                    <div class="w-40 h-40 bg-gray-300 mx-auto flex items-center justify-center text-xs font-bold text-gray-700 rounded">[ GPay QR Image ]</div>
                </div>
                <p class="text-xs font-mono font-bold">UPI ID: damodartechcraze@okaxis</p>
            </div>

            <!-- Tab 2: PhonePe -->
            <div id="tab-phonepe" class="payment-tab bg-gray-950 border border-gray-800 text-white p-6 rounded-xl text-center mb-6 hidden">
                <h3 class="font-bold text-purple-400 mb-2">PhonePe Accepted Here</h3>
                <div class="bg-white p-4 rounded-lg inline-block mb-3">
                    <p class="text-xs font-mono text-gray-800 mb-1">Damodar Techcraze Ve</p>
                    <div class="w-40 h-40 bg-gray-300 mx-auto flex items-center justify-center text-xs font-bold text-gray-700 rounded">[ PhonePe QR Image ]</div>
                </div>
                <p class="text-xs font-mono text-purple-300 font-bold">Scan & Pay via PhonePe App</p>
            </div>

            <!-- Tab 3: Canara Bank & Dynamic QR -->
            <div id="tab-canara" class="payment-tab bg-white text-gray-900 p-6 rounded-xl text-center mb-6 hidden">
                <h3 class="font-bold text-blue-800 mb-2">Canara Bank Dynamic QR</h3>
                <div class="mb-4">
                    <label class="block text-xs font-semibold text-gray-700 mb-1">Enter Amount (INR)</label>
                    <input type="number" id="payAmount" value="499" class="w-32 mx-auto px-3 py-1 border border-gray-300 rounded text-center text-sm" placeholder="499">
                    <button onclick="generateDynamicQR()" class="mt-2 bg-blue-600 hover:bg-blue-700 text-white text-xs px-3 py-1 rounded font-semibold">Generate QR</button>
                </div>
                <div id="dynamicqrcode" class="flex justify-center mb-2"></div>
                <p class="text-xs font-mono font-bold text-blue-900">9232698947@cnrb</p>
                <p class="text-xs font-bold text-gray-800 mt-1">DAMODAR TECHCRAZE VE</p>
            </div>

            <a href="/" class="block text-center bg-gray-800 hover:bg-gray-700 text-white font-semibold py-2 rounded-lg transition text-sm">
                Return to Dashboard
            </a>
        </div>

        <script>
            function switchTab(tab) {
                document.querySelectorAll('.payment-tab').forEach(el => el.classList.add('hidden'));
                document.querySelectorAll('.grid button').forEach(el => {
                    el.classList.remove('bg-indigo-600');
                    el.classList.add('bg-gray-800');
                });
                document.getElementById('tab-' + tab).classList.remove('hidden');
                document.getElementById('btn-' + tab).classList.remove('bg-gray-800');
                document.getElementById('btn-' + tab).classList.add('bg-indigo-600');
            }

            function generateDynamicQR() {
                const amt = document.getElementById('payAmount').value;
                const container = document.getElementById('dynamicqrcode');
                container.innerHTML = "";
                const upiString = "upi://pay?pa=9232698947@cnrb&pn=DAMODAR%20TECHCRAZE%20VE&am=" + amt + "&cu=INR";
                new QRCode(container, {
                    text: upiString,
                    width: 140,
                    height: 140
                });
            }
            // Initial QR generate
            window.onload = function() { generateDynamicQR(); }
        </script>
    </body>
    </html>
    \"\"\"
    from fastapi.responses import HTMLResponse
    return HTMLResponse(content=html_content)
"""

# If old route exists, replace or append
if "@app.get(\"/checkout\")" in content:
    # simple brute replace or rewrite
    parts = content.split('@app.get("/checkout")')
    new_content = parts[0] + pro_checkout_code
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("[Success] Pro Multi-Gateway & Dynamic QR Checkout updated in app.py!")
else:
    with open("app.py", "a", encoding="utf-8") as f:
        f.write(pro_checkout_code)
    print("[Success] Pro Multi-Gateway Checkout appended to app.py!")
