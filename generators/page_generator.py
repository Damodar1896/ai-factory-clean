import os
import json
import pandas as pd
from jinja2 import Template

def create_money_pages():
    os.makedirs("output_pages", exist_ok=True)
    
    # 1. Sample Data (Aapke 50k pages ke liye data source)
    tools_data = [
        {"tool_name": "AI Writer Pro", "category": "Content Generation", "rating": "4.9", "affiliate_link": "https://example.com/ai-writer"},
        {"tool_name": "CodeBot AI", "category": "Development", "rating": "4.8", "affiliate_link": "https://example.com/codebot"},
        {"tool_name": "SEO Ranker Max", "category": "Marketing", "rating": "4.7", "affiliate_link": "https://example.com/seo-ranker"}
    ]
    
    # 2. High-Converting HTML Template for Money Pages
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Best {{ tool.tool_name }} - Review & Pricing 2026</title>
        <meta name="description" content="Discover why {{ tool.tool_name }} is the top-rated tool for {{ tool.category }}. Read our comprehensive review and check pricing.">
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; background: #f4f4f9; color: #333; }
            .container { max-width: 800px; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
            h1 { color: #2c3e50; }
            .cta-btn { display: inline-block; background: #27ae60; color: #fff; padding: 12px 25px; text-decoration: none; border-radius: 5px; font-weight: bold; margin-top: 20px; }
            .cta-btn:hover { background: #219653; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{{ tool.tool_name }} Review (2026)</h1>
            <p><strong>Category:</strong> {{ tool.category }}</p>
            <p><strong>User Rating:</strong> ⭐ {{ tool.rating }} / 5.0</p>
            <hr>
            <h2>Detailed Analysis</h2>
            <p>{{ tool.tool_name }} is engineered to accelerate workflows in {{ tool.category }}. With cutting-edge architecture and seamless integration, it stands out as a market leader.</p>
            
            <h2>Why Choose {{ tool.tool_name }}?</h2>
            <ul>
                <li>Lightning-fast processing and zero lag.</li>
                <li>Advanced automation capabilities built-in.</li>
                <li>Trusted by thousands of professionals globally.</li>
            </ul>
            
            <a href="{{ tool.affiliate_link }}" class="cta-btn" target="_blank">Get Exclusive Deal & Discount</a>
        </div>
    </body>
    </html>
    """
    
    template = Template(html_template)
    
    # 3. Generate Pages in Bulk
    for index, tool in enumerate(tools_data):
        rendered_html = template.render(tool=tool)
        filename = f"output_pages/money_page_{index+1}.html"
        with open(filename, "w") as f:
            f.write(rendered_html)
        print(f"[Generated] Money page created: {filename}")

    print("\n[Done] Programmatic Money Pages generation test completed successfully!")

if __name__ == "__main__":
    print("--- Starting Programmatic Money Page Factory ---")
    create_money_pages()
