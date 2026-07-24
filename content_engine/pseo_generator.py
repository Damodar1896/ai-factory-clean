import os
import json

PSEO_DIR = os.path.expanduser("~/ai-factory/content_engine/generated_pseo_pages")

def generate_pseo_pages():
    print("--- Initializing Programmatic SEO (pSEO) Micro-Niche Explosion ---")
    
    niche_combinations = [
        {"tool": "AI Writer", "location": "New York", "keyword": "Best AI tool for Real Estate in New York"},
        {"tool": "Cloud Hosting", "location": "London", "keyword": "Fastest cloud hosting for gaming blog in London"},
        {"tool": "Chatbot Automation", "location": "Sydney", "keyword": "Automated WhatsApp chatbot for local gym Sydney"}
    ]
    
    os.makedirs(PSEO_DIR, exist_ok=True)
    generated_count = 0
    
    for combo in niche_combinations:
        filename = f"{combo['tool'].lower().replace(' ', '_')}_{combo['location'].lower()}.html"
        filepath = os.path.join(PSEO_DIR, filename)
        
        page_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{combo['keyword']} | Damodar Tech Craze</title>
    <style>
        body {{ background: #000; color: #fff; font-family: -apple-system, sans-serif; padding: 40px; }}
        .container {{ max-width: 800px; margin: auto; background: #111; padding: 30px; border-radius: 12px; border: 1px solid #333; }}
        h1 {{ color: #0071e3; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{combo['keyword']}</h1>
        <p>Looking for the ultimate solution? Damodar Tech Craze provides automated elite tech stacks and high-converting resources tailored for {combo['location']}.</p>
        <a href="https://damodartechcraze.com" style="color: #2997ff;">Explore Master Hub &rarr;</a>
    </div>
</body>
</html>
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(page_content)
            
        print(f" -> [pSEO Page Generated]: {combo['keyword']}")
        generated_count += 1
        
    print(f"[Success] Generated {generated_count} hyper-targeted pSEO pages for organic Google traffic flood!")

if __name__ == "__main__":
    generate_pseo_pages()
