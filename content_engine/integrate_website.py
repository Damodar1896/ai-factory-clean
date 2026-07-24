import os
import shutil

def integrate_all():
    print("--- Fixing Syntax & Building Flawless Apple-Grade Portal ---")
    
    web_dir = os.path.expanduser("~/ai-factory/damodar_website")
    pages_dir = os.path.expanduser("~/ai-factory/content_engine/generated_pages")
    
    if not os.path.exists(pages_dir):
        print("[Error] Generated pages directory not found!")
        return

    page_files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]
    
    def get_category(name):
        n = name.lower()
        if any(x in n for x in ['ai', 'jasper', 'copy', 'grammarly']): return 'Artificial Intelligence'
        if any(x in n for x in ['hostinger', 'bluehost', 'siteground', 'aws', 'cloud', 'envato']): return 'Cloud Infrastructure'
        if any(x in n for x in ['amazon', 'ebay', 'aliexpress', 'walmart', 'etsy', 'appsumo']): return 'Global Commerce'
        if any(x in n for x in ['vpn', 'nord', 'express', 'surfshark']): return 'Cybersecurity'
        return 'SaaS & Productivity'

    cards_html = ""
    for file in sorted(page_files):
        name = file.replace(".html", "").replace("_", " ")
        cat = get_category(name)
        cards_html += f"""
        <a href="generated_pages/{file}" target="_blank" class="apple-card" data-category="{cat}" data-name="{name.lower()}">
            <div class="card-top">
                <span class="card-category">{cat}</span>
                <span class="arrow-icon">→</span>
            </div>
            <div class="card-content">
                <h3>{name}</h3>
                <p>Designed for elite performance. Explore the 2026 definitive breakdown and partner access.</p>
            </div>
        </a>
        """

    total_count = len(page_files)
    
    # Using double brackets {{ }} for CSS to prevent f-string SyntaxError
    apple_index = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Damodar Tech Craze — Elite Intelligence & Resource Hub</title>
    <style>
        :root {{
            --bg: #000000;
            --surface: #0a0a0c;
            --surface-hover: #121216;
            --border: rgba(255, 255, 255, 0.08);
            --border-hover: rgba(255, 255, 255, 0.25);
            --text-primary: #f5f5f7;
            --text-secondary: #86868b;
            --accent: #2997ff;
        }}
        * {{ box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", Arial, sans-serif;
            background: var(--bg);
            color: var(--text-primary);
            margin: 0; padding: 0;
            -webkit-font-smoothing: antialiased;
        }}
        header {{
            position: fixed; top: 0; left: 0; right: 0;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            z-index: 1000;
            display: flex; justify-content: space-between; align-items: center;
            padding: 16px 48px;
        }}
        .logo {{ font-size: 17px; font-weight: 600; color: var(--text-primary); text-decoration: none; }}
        nav {{ display: flex; gap: 32px; }}
        nav a {{ color: var(--text-secondary); text-decoration: none; font-size: 13px; transition: color 0.2s ease; }}
        nav a:hover {{ color: var(--text-primary); }}
        .hero {{ padding: 160px 24px 80px 24px; text-align: center; max-width: 980px; margin: 0 auto; }}
        .hero h1 {{ font-size: 56px; font-weight: 600; letter-spacing: -0.015em; line-height: 1.07; margin-bottom: 16px; color: var(--text-primary); }}
        .hero p {{ font-size: 21px; font-weight: 400; color: var(--text-secondary); line-height: 1.38; max-width: 720px; margin: 0 auto 40px auto; }}
        .search-wrapper {{ max-width: 520px; margin: 0 auto 48px auto; }}
        .search-input {{ width: 100%; background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 14px 20px; color: var(--text-primary); font-size: 15px; outline: none; transition: border-color 0.2s; }}
        .search-input:focus {{ border-color: var(--accent); box-shadow: 0 0 0 4px rgba(41, 151, 255, 0.15); }}
        .filter-container {{ display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-bottom: 64px; }}
        .filter-pill {{ background: var(--surface); border: 1px solid var(--border); color: var(--text-secondary); padding: 8px 16px; border-radius: 20px; font-size: 13px; cursor: pointer; transition: all 0.2s ease; }}
        .filter-pill:hover, .filter-pill.active {{ background: var(--text-primary); color: var(--bg); border-color: var(--text-primary); }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 32px 120px 32px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 24px; }}
        .apple-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 20px; padding: 32px; text-decoration: none; color: inherit; display: flex; flex-direction: column; justify-content: space-between; min-height: 220px; transition: transform 0.3s cubic-bezier(0.25, 1, 0.5, 1), border-color 0.3s ease, background 0.3s ease; }}
        .apple-card:hover {{ transform: scale(1.02); border-color: var(--border-hover); background: var(--surface-hover); }}
        .card-top {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 32px; }}
        .card-category {{ font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.08em; color: var(--text-secondary); }}
        .arrow-icon {{ font-size: 16px; color: var(--text-secondary); transition: transform 0.2s ease, color 0.2s ease; }}
        .apple-card:hover .arrow-icon {{ transform: translateX(4px); color: var(--accent); }}
        .card-content h3 {{ font-size: 24px; font-weight: 600; margin: 0 0 10px 0; color: var(--text-primary); }}
        .card-content p {{ font-size: 14px; font-weight: 400; color: var(--text-secondary); line-height: 1.45; margin: 0; }}
        footer {{ text-align: center; padding: 48px 0; border-top: 1px solid var(--border); color: var(--text-secondary); font-size: 12px; }}
    </style>
</head>
<body>
    <header>
        <a href="#" class="logo">Damodar Tech Craze.</a>
        <nav>
            <a href="index.html">Overview</a>
            <a href="subdomains/tools.html">Calculators</a>
            <a href="subdomains/deals.html">Privileged Deals</a>
        </nav>
    </header>
    <section class="hero">
        <h1>Intelligence. Precision. Scale.</h1>
        <p>Explore {total_count}+ verified enterprise architectural hubs, side-by-side matrices, and ecosystem partnerships engineered for 2026.</p>
        <div class="search-wrapper">
            <input type="text" id="searchInput" class="search-input" placeholder="Search systems, tools, protocols..." onkeyup="filterHubs()">
        </div>
        <div class="filter-container">
            <button class="filter-pill active" onclick="filterCategory('all', this)">All Hubs</button>
            <button class="filter-pill" onclick="filterCategory('Artificial Intelligence', this)">Artificial Intelligence</button>
            <button class="filter-pill" onclick="filterCategory('Cloud Infrastructure', this)">Cloud Infrastructure</button>
            <button class="filter-pill" onclick="filterCategory('Global Commerce', this)">Global Commerce</button>
            <button class="filter-pill" onclick="filterCategory('Cybersecurity', this)">Cybersecurity</button>
            <button class="filter-pill" onclick="filterCategory('SaaS & Productivity', this)">SaaS & Productivity</button>
        </div>
    </section>
    <div class="container">
        <div class="grid" id="cardGrid">
            {cards_html}
        </div>
    </div>
    <footer>
        <p>Copyright © 2026 Damodar Tech Craze Inc. All rights reserved. Built with Absolute Precision.</p>
    </footer>
    <script>
        function filterHubs() {{
            let input = document.getElementById('searchInput').value.toLowerCase();
            let cards = document.getElementsByClassName('apple-card');
            for (let i = 0; i < cards.length; i++) {{
                let name = cards[i].getAttribute('data-name');
                if (name.includes(input)) {{
                    cards[i].style.display = "";
                }} else {{
                    cards[i].style.display = "none";
                }}
            }}
        }}
        function filterCategory(category, btn) {{
            let pills = document.getElementsByClassName('filter-pill');
            for(let p of pills) p.classList.remove('active');
            btn.classList.add('active');
            let cards = document.getElementsByClassName('apple-card');
            for (let card of cards) {{
                let cat = card.getAttribute('data-category');
                if (category === 'all' || cat === category) {{
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

    dest_pages_dir = os.path.join(web_dir, "generated_pages")
    if os.path.exists(pages_dir):
        if os.path.exists(dest_pages_dir):
            shutil.rmtree(dest_pages_dir)
        shutil.copytree(pages_dir, dest_pages_dir)
        print(f"[Success] Copied all generated pages to {dest_pages_dir}")

    index_path = os.path.join(web_dir, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(apple_index)
        
    print(f"[Success] Flawless Masterpiece built successfully at: {index_path}")

if __name__ == "__main__":
    integrate_all()
