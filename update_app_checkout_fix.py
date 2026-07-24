import os

with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()

fixed_checkout_code = """
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
            <p class="text-gray-400 text-sm mb-6">Select your payment mode, enter amount, and scan to pay instantly.</p>
            
            <!-- Gateway Selector Tabs -->
            <div class="grid grid-cols-3 gap-2 mb-6">
                <button onclick="switchGateway('gpay', 'damodartechcraze@okaxis', 'Damodar Techcraze Ventures')" id="btn-gpay" class="py-2 px-3 bg-indigo-600 text-xs font-semibold rounded-lg transition">Google Pay</button>
                <button onclick="switchGateway('phonepe', '9232698947@ybl', 'Damodar Techcraze Ventures')" id="btn-phonepe" class="py-2 px-3 bg-gray-800 text-xs font-semibold rounded-lg transition">PhonePe</button>
                <button onclick="switchGateway('canara', '9232698947@cnrb', 'Damodar Techcraze Ventures')" id="btn-canara" class="py-2 px-3 bg-gray-800 text-xs font-semibold rounded-lg transition">Canara Bank</button>
            </div>

            <!-- Unified Dynamic Payment Box -->
            <div class="bg-white text-gray-900 p-6 rounded-xl text-center mb-6">
                <h3 id="gatewayTitle" class="font-bold text-indigo-700 mb-2 text-base">Google Pay (GPay)</h3>
                <div class="mb-4">
                    <label class="block text-xs font-semibold text-gray-700 mb-1">Enter Amount (INR)</label>
                    <input type="number" id="payAmount" value="499" oninput="generateQR()" class="w-32 mx-auto px-3 py-1 border border-gray-300 rounded text-center text-sm font-bold text-black" placeholder="499">
                </div>
                
                <div id="qrcode" class="flex justify-center mb-3"></div>
                
                <p id="upiIdDisplay" class="text-xs font-mono font-bold text-gray-800">UPI ID: damodartechcraze@okaxis</p>
                <p id="merchantName" class="text-xs font-bold text-indigo-900 mt-1">DAMODAR TECHCRAZE VENTURES</p>
            </div>

            <a href="/" class="block text-center bg-gray-800 hover:bg-gray-700 text-white font-semibold py-2 rounded-lg transition text-sm">
                Return to Dashboard
            </a>
        </div>

        <script>
            let currentUPI = "damodartechcraze@okaxis";
            let currentName = "Damodar Techcraze Ventures";

            function switchGateway(gateway, upi, name) {
                currentUPI = upi;
                currentName = name;
                
                document.querySelectorAll('.grid button').forEach(el => {
                    el.classList.remove('bg-indigo-600');
                    el.classList.add('bg-gray-800');
                });
                document.getElementById('btn-' + gateway).classList.remove('bg-gray-800');
                document.getElementById('btn-' + gateway).classList.add('bg-indigo-600');

                let title = "Google Pay (GPay)";
                if(gateway === 'phonepe') title = "PhonePe UPI";
                if(gateway === 'canara') title = "Canara Bank Dynamic QR";
                
                document.getElementById('gatewayTitle').innerText = title;
                document.getElementById('upiIdDisplay').innerText = "UPI ID: " + upi;
                document.getElementById('merchantName').innerText = name.toUpperCase();

                generateQR();
            }

            function generateQR() {
                const amt = document.getElementById('payAmount').value;
                const container = document.getElementById('qrcode');
                container.innerHTML = "";
                const upiString = "upi://pay?pa=" + currentUPI + "&pn=" + encodeURIComponent(currentName) + "&am=" + amt + "&cu=INR";
                new QRCode(container, {
                    text: upiString,
                    width: 150,
                    height: 150
                });
            }

            window.onload = function() { generateQR(); }
        </script>
    </body>
    </html>
    \"\"\"
    from fastapi.responses import HTMLResponse
    return HTMLResponse(content=html_content)
"""

if "@app.get(\"/checkout\")" in content:
    parts = content.split('@app.get("/checkout")')
    new_content = parts[0] + fixed_checkout_code
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("[Success] Checkout page successfully fixed with dynamic QR & proper name!")
else:
    with open("app.py", "a", encoding="utf-8") as f:
        f.write(fixed_checkout_code)
    print("[Success] Checkout page appended successfully!")
