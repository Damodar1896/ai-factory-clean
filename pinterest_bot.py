from PIL import Image, ImageDraw, ImageFont
import os

def create_professional_ai_pin():
    # Pinterest Pin के लिए परफेक्ट वर्टिकल साइज (1000 x 1500 pixels)
    width, height = 1000, 1500
    
    # एक रिच और प्रोफेशनल डार्क टेक बैकग्राउंड (Rich Dark Slate / Charcoal)
    image = Image.new("RGB", (width, height), color=(11, 15, 25))
    draw = ImageDraw.Draw(image)
    
    # फॉन्ट लोडिंग (Mac के डिफॉल्ट हाई-क्वालिटी Helvetica फॉन्ट का उपयोग)
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 65)
        heading_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 45)
        body_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
        cta_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
    except:
        title_font = ImageFont.load_default()
        heading_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        cta_font = ImageFont.load_default()

    # 1. टॉप पर ब्रांड का नाम और टैगलाइन (Gold & Cyan Accent)
    draw.text((80, 150), "DAMODAR TECHCRAZE", fill=(250, 204, 21), font=title_font) # Gold
    draw.text((80, 230), "VENTURES", fill=(255, 255, 255), font=title_font) # White
    
    # एक पतली डेकोरेटिव लाइन (Modern Divider)
    draw.rectangle([80, 320, 300, 328], fill=(56, 189, 248)) # Cyan line

    # 2. मुख्य सर्विस हाइलाइट्स (Clear, Structured & High-Tech Look)
    start_y = 500
    services = [
        ("⚡", "Custom AI Software Development"),
        ("🤖", "24x7 Autonomous AI Agents"),
        ("🐍", "Advanced Python Automation"),
        ("🚀", "Scalable Micro-SaaS Platforms")
    ]
    
    for icon, text in services:
        # बैकग्राउंड में हल्का कार्ड बॉक्स (Card UI Style)
        draw.rounded_rectangle([80, start_y, 920, start_y + 110], radius=15, fill=(30, 41, 59))
        # आइकॉन और टेक्स्ट
        draw.text((120, start_y + 30), icon, fill=(255, 255, 255), font=heading_font)
        draw.text((200, start_y + 35), text, fill=(226, 232, 240), font=body_font)
        start_y += 150

    # 3. बॉटम में दमदार Call to Action (CTA Banner)
    draw.rounded_rectangle([80, 1200, 920, 1330], radius=20, fill=(37, 99, 235)) # Modern Blue Button
    draw.text((150, 1240), "Hire Experts on Upwork & Fiverr", fill=(255, 255, 255), font=cta_font)

    # 4. इमेज सेव करें
    output_path = "generated_pin.png"
    image.save(output_path)
    print(f"✨ Professional UI/UX Pin generated successfully at: {output_path}")

if __name__ == "__main__":
    create_professional_ai_pin()
