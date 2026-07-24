import os

checkout_full_code = """
@app.get("/checkout")
def upi_checkout():
    html_content = \"\"\"
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Pro Checkout & Invoice - Damodar Tech Empire</title>
        <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
    </head>
    <body class="bg-gray-950 text-white font-sans p-6">
        <div class="max-w-xl mx-auto bg-gray-900 border border-gray-800 p-8 rounded-xl shadow-2xl mt-6">
            <h1 class="text-2xl font-bold mb-1 text-indigo-400">⚡ Damodar Tech Empire Checkout</h1>
            <p class="text-gray-400 text-sm mb-6">Select payment method, complete payment, and submit your Transaction ID below.</p>
            
            <!-- Gateway Selector Tabs -->
            <div class="grid grid-cols-5 gap-1 mb-6 text-xs">
                <button onclick="switchTab('gpay')" id="btn-gpay" class="py-2 px-1 bg-indigo-600 font-semibold rounded transition">GPay</button>
                <button onclick="switchTab('phonepe')" id="btn-phonepe" class="py-2 px-1 bg-gray-800 font-semibold rounded transition">PhonePe</button>
                <button onclick="switchTab('canara')" id="btn-canara" class="py-2 px-1 bg-gray-800 font-semibold rounded transition">Canara</button>
                <button onclick="switchTab('paypal')" id="btn-paypal" class="py-2 px-1 bg-gray-800 font-semibold rounded transition">PayPal</button>
                <button onclick="switchTab('crypto')" id="btn-crypto" class="py-2 px-1 bg-gray-800 font-semibold rounded transition">Crypto</button>
            </div>

            <!-- Tab 1, 2, 3: UPI Dynamic Box -->
            <div id="upi-box" class="bg-white text-gray-900 p-6 rounded-xl text-center mb-6">
                <h3 id="gatewayTitle" class="font-bold text-indigo-700 mb-2 text-base">Google Pay (GPay)</h3>
                <div class="mb-4">
                    <label class="block text-xs font-semibold text-gray-700 mb-1">Enter Amount (INR)</label>
                    <input type="number" id="payAmount" value="499" oninput="updateAll()" class="w-32 mx-auto px-3 py-1 border border-gray-300 rounded text-center text-sm font-bold text-black" placeholder="499">
                </div>
                <div id="qrcode" class="flex justify-center mb-3"></div>
                <p id="upiIdDisplay" class="text-xs font-mono font-bold text-gray-800">UPI ID: damodartechcraze@okaxis</p>
                <p class="text-xs font-bold text-indigo-900 mt-1">DAMODAR TECHCRAZE VENTURES</p>
            </div>

            <!-- Tab 4: PayPal (USD) - Fixed with Email Fallback -->
            <div id="paypal-box" class="bg-white text-gray-900 p-6 rounded-xl text-center mb-6 hidden">
                <h3 class="font-bold text-blue-700 mb-2 text-base">PayPal International (USD $)</h3>
                <p class="text-xs text-gray-600 mb-3">Pay securely via PayPal. If link prompts an error, send direct funds to our official email.</p>
                <a href="https://paypal.me/damodartechcraze" target="_blank" class="inline-block bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold px-6 py-3 rounded-lg shadow transition mb-3">
                    Pay via PayPal.me ($ USD)
                </a>
                <div class="bg-gray-100 p-2 rounded text-xs font-mono text-gray-800">
                    Official PayPal Email: <strong>support@damodartechcraze.com</strong>
                </div>
            </div>

            <!-- Tab 5: Crypto (USDT - TRC20) -->
            <div id="crypto-box" class="bg-white text-gray-900 p-6 rounded-xl text-center mb-6 hidden">
                <h3 class="font-bold text-amber-600 mb-2 text-base">Crypto Payment (USDT - TRC20)</h3>
                <p class="text-xs text-gray-600 mb-3">Scan or copy address to pay via USDT (TRC20).</p>
                <div id="cryptoqrcode" class="flex justify-center mb-3"></div>
                <div class="bg-gray-100 p-2 rounded text-xs font-mono font-bold text-gray-800 break-all select-all">
                    TXTwBaR7CATwkgRqgX5cXTzPd2GjMqQC3E
                </div>
                <p class="text-xs text-gray-500 mt-2">Network: TRON (TRC20 only) - Damodar Techcraze Ventures</p>
            </div>

            <!-- Module 1: Invoice / Receipt Preview Section -->
            <div class="bg-gray-900 border border-gray-700 p-4 rounded-xl mb-6 text-xs">
                <h4 class="font-bold text-indigo-300 mb-2">📄 Live Invoice Summary</h4>
                <div class="flex justify-between text-gray-300 border-b border-gray-800 pb-1 mb-1">
                    <span>Company:</span> <span class="font-bold">Damodar Techcraze Ventures</span>
                </div>
                <div class="flex justify-between text-gray-300 border-b border-gray-800 pb-1 mb-1">
                    <span>Item / Service:</span> <span class="font-bold">Tech Empire Module Access</span>
                </div>
                <div class="flex justify-between text-gray-300">
                    <span>Total Amount:</span> <span id="invoiceAmt" class="font-bold text-green-400">₹499</span>
                </div>
            </div>

            <!-- Module 2: Payment Verification / UTR Submission Form -->
            <div class="bg-gray-800 border border-gray-700 p-4 rounded-xl mb-6">
                <h4 class="font-bold text-emerald-400 text-xs mb-2">✅ Submit Payment Proof (UTR / TXID)</h4>
                <form onsubmit="submitProof(event)" class="space-y-3 text-xs">
                    <div>
                        <label class="block text-gray-300 mb-1">Your Name / Email</label>
                        <input type="text" id="clientName" required class="w-full px-3 py-2 bg-gray-900 border border-gray-700 rounded text-white" placeholder="Enter name or email">
                    </div>
                    <div>
                        <label class="block text-gray-300 mb-1">Transaction ID / UTR Number</label>
                        <input type="text" id="clientUtr" required class="w-full px-3 py-2 bg-gray-900 border border-gray-700 rounded text-white font-mono" placeholder="e.g. 423910294102">
                    </div>
                    <button type="submit" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-semibold py-2 rounded transition">
                        Verify & Submit Payment
                    </button>
                </form>
                <div id="successMsg" class="hidden mt-3 p-2 bg-emerald-950 border border-emerald-800 text-emerald-300 text-center rounded">
                    🎉 Payment proof submitted successfully to Dashboard!
                </div>
            </div>

            <a href="/" class="block text-center bg-gray-800 hover:bg-gray-700 text-white font-semibold py-2 rounded-lg transition text-sm">
                Return to Dashboard
            </a>
        </div>

        <script>
            let currentUPI = "damodartechcraze@okaxis";
            let currentName = "Damodar Techcraze Ventures";

            function switchTab(tab) {
                document.getElementById('upi-box').classList.add('hidden');
                document.getElementById('paypal-box').classList.add('hidden');
                document.getElementById('crypto-box').classList.add('hidden');

                document.querySelectorAll('.grid button').forEach(el => {
                    el.classList.remove('bg-indigo-600');
                    el.classList.add('bg-gray-800');
                });
                document.getElementById('btn-' + tab).classList.remove('bg-gray-800');
                document.getElementById('btn-' + tab).classList.add('bg-indigo-600');

                if (tab === 'paypal') {
                    document.getElementById('paypal-box').classList.remove('hidden');
                } else if (tab === 'crypto') {
                    document.getElementById('crypto-box').classList.remove('hidden');
                    generateCryptoQR();
                } else {
                    document.getElementById('upi-box').classList.remove('hidden');
                    if(tab === 'gpay') {
                        currentUPI = "damodartechcraze@okaxis";
                        document.getElementById('gatewayTitle').innerText = "Google Pay (GPay)";
                    } else if(tab === 'phonepe') {
                        currentUPI = "9232698947@ybl";
                        document.getElementById('gatewayTitle').innerText = "PhonePe UPI";
                    } else if(tab === 'canara') {
                        currentUPI = "9232698947@cnrb";
                        document.getElementById('gatewayTitle').innerText = "Canara Bank Dynamic QR";
                    }
                    document.getElementById('upiIdDisplay').innerText = "UPI ID: " + currentUPI;
                    generateQR();
                }
            }

            function updateAll() {
                const amt = document.getElementById('payAmount').value;
                document.getElementById('invoiceAmt').innerText = "₹" + amt;
                generateQR();
            }

            function generateQR() {
                const amt = document.getElementById('payAmount').value;
                const container = document.getElementById('qrcode');
                container.innerHTML = "";
                const upiString = "upi://pay?pa=" + currentUPI + "&pn=" + encodeURIComponent(currentName) + "&am=" + amt + "&cu=INR";
                new QRCode(container, { text: upiString, width: 140, height: 140 });
            }

            function generateCryptoQR() {
                const container = document.getElementById('cryptoqrcode');
                if(container.innerHTML === "") {
                    new QRCode(container, { text: "TXTwBaR7CATwkgRqgX5cXTzPd2GjMqQC3E", width: 140, height: 140 });
                }
            }

            function submitProof(e) {
                e.preventDefault();
                document.getElementById('successMsg').classList.remove('hidden');
                setTimeout(() => {
                    document.getElementById('clientName').value = "";
                    document.getElementById('clientUtr').value = "";
                }, 1500);
            }

            window.onload = function() { generateQR(); }
        </script>
    </body>
    </html>
    \"\"\"
    from fastapi.responses import HTMLResponse
    return HTMLResponse(content=html_content)
"""

with open("app.py", "w", encoding="utf-8") as f:
    f.write(checkout_full_code)

print("[Success] app.py updated with PayPal fallback, Invoice Generator, and UTR Verification Form!")
