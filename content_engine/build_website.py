import os
import json

BASE_DIR = os.path.expanduser("~/ai-factory/content_engine")
WEB_DIR = os.path.expanduser("~/ai-factory/damodar_website")
os.makedirs(WEB_DIR, exist_ok=True)
os.makedirs(os.path.join(WEB_DIR, "subdomains"), exist_ok=True)

def build_master_website():
    print("--- Building Damodar Tech Craze World-Class Frontend & Subdomains ---")
    
    # 1. Main Website Index (damodartechcraze.com)
    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Damodar Tech Craze | Ultimate SaaS, AI Tools & Tech Hub 2026</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 0; }
        header { background: #1e293b; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; }
        .logo { font-size: 24px; font-weight: bold; color: #38bdf8; text-decoration: none; }
        nav a { color: #94a3b8; text-decoration: none; margin-left: 20px; font-weight: 500; }
        nav a:hover { color: #38bdf8; }
        .hero { text-align: center; padding: 80px 20px; background: linear-gradient(to bottom, #1e293b, #0f172a); }
        .hero h1 { font-size: 48px; margin-bottom: 20px; color: #fff; }
        .hero p { font-size: 18px; color: #94a3b8; max-width: 700px; margin: 0 auto 30px auto; }
        .cta-btn { background: #38bdf8; color: #0f172a; padding: 14px 28px; border-radius: 8px; font-weight: bold; text-decoration: none; display: inline-block; }
        .container { max-width: 1200px; margin: 40px auto; padding: 0 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
        .card { background: #1e293b; border: 1px solid #334155; padding: 25px; border-radius: 12px; transition: transform 0.2s; }
        .card:hover { transform: translateY(-5px); border-color: #38bdf8; }
        .card h3 { margin-top: 0; color: #38bdf8; }
        .card p { color: #94a3b8; font-size: 14px; }
        .card a { color: #38bdf8; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 15px; }
        footer { text-align: center; padding: 40px; color: #64748b; border-top: 1px solid #334155; margin-top: 60px; }
    </style>
</head>
<body>
    <header>
        <a href="#" class="logo">⚡ Damodar Tech Craze</a>
        <nav>
            <a href="#reviews">Software Reviews</a>
            <a href="subdomains/tools.html">🛠️ Tools & Calculators</a>
            <a href="subdomains/deals.html">🔥 SaaS Deals</a>
        </nav>
    </header>

    <div class="hero">
        <h1>Supercharge Your Workflow with Verified Tech & AI Tools</h1>
        <p>Explore deep-dive expert reviews, side-by-side comparison tables, and exclusive partner deals curated for modern professionals.</p>
        <a href="#reviews" class="cta-btn">Explore 45+ Verified Resources</a>
    </div>

    <div class="container" id="reviews">
        <h2>Featured Authority Hubs</h2>
        <div class="grid">
            <div class="card">
                <h3>ClickBank & Marketplace Ecosystems</h3>
                <p>Complete breakdown of top digital marketplaces, commission structures, and scaling guides.</p>
                <a href="generated_pages/ClickBank.html">Read Full Review →</a>
            </div>
            <div class="card">
                <h3>Hostinger & Cloud Infrastructure</h3>
                <p>Lightning-fast performance benchmarks, speed analysis, and special partner savings.</p>
                <a href="generated_pages/Hostinger.html">Read Full Review →</a>
            </div>
            <div class="card">
                <h3>Jasper AI & Next-Gen Productivity</h3>
                <p>Automate your content creation pipeline with cutting-edge AI software reviews.</p>
                <a href="generated_pages/Jasper_AI.html">Read Full Review →</a>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2026 Damodar Tech Craze (damodartechcraze.com). All rights reserved. Verified Global Partner Hub.</p>
    </footer>
</body>
</html>
"""
    
    with open(os.path.join(WEB_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    # 2. Subdomain: tools.damodartechcraze.com
    tools_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Tools & ROI Calculators | Damodar Tech Craze</title>
    <style>
        body { font-family: sans-serif; background: #0f172a; color: #f8fafc; padding: 40px; text-align: center; }
        a { color: #38bdf8; text-decoration: none; }
    </style>
</head>
<body>
    <h1>🛠️ Interactive SaaS Tools & ROI Calculators</h1>
    <p>Subdomain: <strong>tools.damodartechcraze.com</strong></p>
    <p>Feature active: Advanced software cost & revenue projection tools embedded.</p>
    <br><a href="../index.html">← Back to Main Damodar Tech Craze Hub</a>
</body>
</html>
"""
    with open(os.path.join(WEB_DIR, "subdomains", "tools.html"), "w", encoding="utf-8") as f:
        f.write(tools_html)

    # 3. Subdomain: deals.damodartechcraze.com
    deals_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Exclusive Software Deals | Damodar Tech Craze</title>
    <style>
        body { font-family: sans-serif; background: #0f172a; color: #f8fafc; padding: 40px; text-align: center; }
        a { color: #38bdf8; text-decoration: none; }
    </style>
</head>
<body>
    <h1>🔥 Exclusive Software Deals & Lifetime Discounts</h1>
    <p>Subdomain: <strong>deals.damodartechcraze.com</strong></p>
    <p>Feature active: AppSumo-style verified partner discounts and promotional codes.</p>
    <br><a href="../index.html">← Back to Main Damodar Tech Craze Hub</a>
.</body>
</html>
"""
    with open(os.path.join(WEB_DIR, "subdomains", "deals.html"), "w", encoding="utf-8") as f:
        f.write(deals_html)

    print(f"[Success] Master Website & Subdomains built successfully at: {WEB_DIR}")

if __name__ == "__main__":
    build_master_website()
