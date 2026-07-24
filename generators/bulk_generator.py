import os

OUTPUT_DIR = "output_pages"

def generate_bulk_pages(total_pages=50):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\n[Info] Starting Bulk Generation of {total_pages} SEO Money Pages...")

    keywords = [
        "best AI automation tools for business 2026",
        "how to scale programmatic SEO with Python",
        "passive income affiliate marketing funnels",
        "secure proxy setup for web scraping",
        "automated email warmer tools for outreach"
    ]

    for i in range(1, total_pages + 1):
        keyword = keywords[(i - 1) % len(keywords)]
        page_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{keyword.title()} - Page {i}</title>
    <meta name="description" content="Discover top strategies for {keyword}. Scale your digital empire with Damodar Tech Craze automation.">
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; padding: 40px; max-width: 800px; margin: auto;">
    <h1>{keyword.title()} (#{i})</h1>
    <p>Welcome to Damodar Tech Craze automated high-performance resource hub. If you are looking to master <strong>{keyword}</strong>, you are in the right place.</p>
    <h2>Key Benefits</h2>
    <ul>
        <li>100% Automated Workflow & Deployment</li>
        <li>Optimized for Search Engine Indexing & Ranking</li>
        <li>Integrated with Secure Lead Capture & Affiliate Funnels</li>
    </ul>
    <hr>
    <p><a href="https://github.com/Damodar1896/ai-factory-pages" style="color: #0066cc; font-weight: bold;">Explore More Damodar Tech Craze Resources</a></p>
</body>
</html>
"""
        file_path = os.path.join(OUTPUT_DIR, f"money_page_{i}.html")
        with open(file_path, "w") as f:
            f.write(page_content)

    print(f"[Success] Successfully generated {total_pages} money pages inside '{OUTPUT_DIR}/' directory!")

if __name__ == "__main__":
    print("--- Starting AI Factory Bulk Money Pages Generator ---")
    generate_bulk_pages(50)
