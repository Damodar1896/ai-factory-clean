import os
import json

def build_hub():
    print("--- Building Ultra-Refined Apple/Stripe Grade Master Hub ---")
    web_dir = os.path.expanduser("~/ai-factory/damodar_website")
    os.makedirs(web_dir, exist_ok=True)
    
    targets_path = os.path.expanduser("~/ai-factory/affiliate_bot/affiliate_targets.json")
    if os.path.exists(targets_path):
        with open(targets_path, "r") as f:
            data = json.load(f)
        networks = data.get("networks", [])
    else:
        networks = [
            {"name": "ClickBank", "category": "Digital Products", "url": "https://www.clickbank.com"},
            {"name": "Hostinger", "category": "Cloud Hosting", "url": "https://www.hostinger.com"},
            {"name": "Jasper AI", "category": "Artificial Intelligence", "url": "https://www.jasper.ai"}
        ]

    cards_html = ""
    for net in networks:
        name = net.get('name', 'Tool')
        category = net.get('category', 'SaaS Platform')
        url = net.get('url', 'https://damodartechcraze.com')
        file_slug = name.replace(" ", "_").replace(".", "") + ".html"
        cards_html += f"""
        <a href="generated_pages/{file_slug}" target="_blank" class="elite-card" data-name="{name.lower()}" data-category="{category.lower()}">
            <div class="card-header">
                <span class="card-tag">{category}</span>
                <span class="verified-badge">Verified Hub</span>
            </div>
            <h3>{name}</h3>
            <p>Explore the definitive 2026 architecture analysis, benchmark metrics, and secure partner access.</p>
            <div class="card-footer-link">Explore Hub →</div>
        </a>
        """

    master_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Damodar Tech Craze — Elite Intelligence & Resource Hub</title>
    <style>
        :root {{
            --bg: #030305;
            --surface: rgba(18, 18, 24, 0.7);
            --surface-hover: rgba(28, 28, 38, 0.9);
            --border: rgba(255, 255, 255, 0.08);
            --border-hover: rgba(41, 151, 255, 0.4);
            --text-primary: #f5f5f7;
            --text-secondary: #86868b;
            --accent: #2997ff;
        }}
        * {{ box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", Arial, sans-serif;
            background: var(--bg);
            background-image: radial-gradient(circle at 50% 0%, #111827 0%, var(--bg) 60%);
            color: var(--text-primary);
            margin: 0; padding: 0;
            -webkit-font-smoothing: antialiased;
            min-height: 100vh;
        }}
        .navbar {{
            background: rgba(3, 3, 5, 0.8);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            position: sticky; top: 0; z-index: 1000;
            display: flex; justify-content: space-between; align-items: center;
            padding: 20px 48px;
        }}
        .logo {{ font-size: 18px; font-weight: 600; color: var(--text-primary); text-decoration: none; letter-spacing: -0.01em; }}
        .nav-links {{ display: flex; gap: 32px; }}
        .nav-links a {{ color: var(--text-secondary); text-decoration: none; font-size: 13px; font-weight: 400; transition: color 0.2s; }}
        .nav-links a:hover {{ color: var(--text-primary); }}

        .hero-section {{
            padding: 120px 24px 60px 24px;
            text-align: center;
            max-width: 900px;
            margin: 0 auto;
        }}
        .hero-section h1 {{
            font-size: 56px;
            font-weight: 600;
            letter-spacing: -0.02em;
            line-height: 1.08;
            margin-bottom: 20px;
            color: var(--text-primary);
        }}
        .hero-section p {{
            font-size: 20px;
            color: var(--text-secondary);
            line-height: 1.4;
            max-width: 680px;
            margin: 0 auto 40px auto;
        }}

        .search-bar {{
            max-width: 520px;
            margin: 0 auto 40px auto;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 8px;
            display: flex;
            backdrop-filter: blur(10px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
            transition: border-color 0.2s;
        }}
        .search-bar:focus-within {{ border-color: var(--accent); }}
        .search-bar input {{
            flex: 1; background: transparent; border: none; outline: none;
            color: var(--text-primary); padding: 12px 16px; font-size: 16px;
        }}

        .grid-container {{
            max-width: 1300px;
            margin: 0 auto;
            padding: 0 32px 120px 32px;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
            gap: 24px;
        }}
        .elite-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 36px;
            text-decoration: none;
            color: inherit;
            display: flex; flex-direction: column; justify-content: space-between;
            backdrop-filter: blur(10px);
            transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
        }}
        .elite-card:hover {{
            transform: translateY(-6px);
            border-color: var(--border-hover);
            background: var(--surface-hover);
            box-shadow: 0 20px 40px rgba(41, 151, 255, 0.08);
        }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }}
        .card-tag {{ font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--accent); font-weight: 500; }}
        .verified-badge {{ font-size: 11px; color: #34c759; background: rgba(52, 199, 89, 0.1); padding: 4px 10px; border-radius: 12px; font-weight: 500; }}
        
        .elite-card h3 {{ font-size: 24px; font-weight: 600; margin: 0 0 12px 0; color: var(--text-primary); letter-spacing: -0.01em; }}
        .elite-card p {{ font-size: 14px; color: var(--text-secondary); line-height: 1.5; margin: 0 0 28px 0; }}
        
        .card-footer-link {{
            color: var(--accent);
            font-size: 14px;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: gap 0.2s ease;
        }}
        .elite-card:hover .card-footer-link {{ gap: 10px; }}

        footer {{
            text-align: center;
            padding: 60px;
            border-top: 1px solid var(--border);
            color: var(--text-secondary);
            font-size: 13px;
        }}
    </style>
</head>
<body>
    <div class="navbar">
        <a href="#" class="logo">Damodar Tech Craze.</a>
        <div class="nav-links">
            <a href="#">Ecosystem Hub</a>
            <a href="#">Privileged Deals</a>
            <a href="#">Security Protocols</a>
        </div>
    </div>

    <div class="hero-section">
        <h1>Intelligence. Precision. Scale.</h1>
        <p>Access {len(networks)}+ verified enterprise platforms, optimized protocols, and exclusive partner infrastructure curated for elite execution.</p>
        
        <div class="search-bar">
            <input type="text" id="liveSearch" placeholder="Search platforms, tools, networks..." onkeyup="searchHubs()">
        </div>
    </div>

    <div class="grid-container" id="hubGrid">
        {cards_html}
    </div>

    <footer>
        <p>© 2026 Damodar Tech Craze Inc. All rights reserved. Built with Absolute Precision.</p>
    </footer>

    <script>
        function searchHubs() {{
            let query = document.getElementById('liveSearch').value.toLowerCase();
            let cards = document.getElementsByClassName('elite-card');
            for (let card of cards) {{
                let name = card.getAttribute('data-name');
                let cat = card.getAttribute('data-category');
                if (name.includes(query) || cat.includes(query)) {{
                    card.style.display = "";
                }} else {{
                    card.style.display = "none";
                }}
            }}
        }}
    </script>
</body>
</html>
"""

    index_path = os.path.join(web_dir, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(master_page)
        
    print(f"[Success] Ultimate Refined Apple-Grade Hub built at: {index_path}")

if __name__ == "__main__":
    build_hub()
