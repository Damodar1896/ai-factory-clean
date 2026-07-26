import os

class LandingPageGenerator:
    @staticmethod
    def build_dynamic_landing_page(topic, affiliate_link):
        os.makedirs("automation_core/public_landing", exist_ok=True)
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{topic} | Autonomous Resource Center</title>
    <style>
        body {{ background-color: #0f172a; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
        .card {{ background: #1e293b; padding: 40px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); text-align: center; max-width: 500px; border: 1px solid #334155; }}
        h1 {{ font-size: 24px; margin-bottom: 15px; color: #38bdf8; }}
        p {{ color: #94a3b8; font-size: 15px; line-height: 1.6; margin-bottom: 25px; }}
        .btn {{ display: inline-block; background: #2563eb; color: #ffffff; padding: 14px 28px; border-radius: 8px; text-decoration: none; font-weight: bold; transition: background 0.3s; }}
        .btn:hover {{ background: #1d4ed8; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{topic}</h1>
        <p>You have accessed the exclusive framework. Discover how the top 1% leverage autonomous systems to scale their income stream securely in 2026.</p>
        <a href="{affiliate_link}" class="btn">Access System Blueprint Now &rarr;</a>
    </div>
</body>
</html>"""
        
        file_path = "automation_core/public_landing/index.html"
        with open(file_path, "w") as f:
            f.write(html_content)
            
        print(f"[+] Autonomous Landing Page Generated Successfully at: {file_path}")

if __name__ == "__main__":
    LandingPageGenerator.build_dynamic_landing_page("The 2026 Shift in Automated Wealth", "https://hop.clickbank.net/?aff=autonomous_wealth_2026")
