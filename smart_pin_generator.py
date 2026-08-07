from PIL import Image, ImageDraw, ImageFont
import os

def generate_smart_template():
    # Pinterest Pin साइज (1000 x 1500 pixels)
    width, height = 1000, 1500
    
    # 1. एक रिच और प्रीमियम डार्क-टेक्नोलॉजी बैकग्राउंड बेस बनाएं
    image = Image.new("RGB", (width, height), color=(13, 17, 23)) # GitHub dark style
    draw = ImageDraw.Draw(image)
    
    # डेकोरेटिव एलिमेंट्स (ऊपर और नीचे मॉडर्न ग्लोइंग बॉर्डर्स या पट्टियां)
    draw.rectangle([0, 0, width, 25], fill=(56, 189, 248)) # Top Cyan Accent Bar
    
    # 2. फॉन्ट सेटिंग्स (Mac के हाई-क्वालिटी Helvetica फॉन्ट्स)
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 70)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
        card_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 38)
        cta_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 42)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        card_font = ImageFont.load_default()
        cta_font = ImageFont.load_default()

    # 3. ब्रांड नेम और टैगलाइन
    draw.text((80, 120), "DAMODAR TECHCRAZE", fill=(250, 204, 21), font=title_font) # Gold
    draw.text((80, 210), "VENTURES", fill=(255, 255, 255), font=title_font) # White
    
    draw.text((80, 310), "Next-Gen AI Software & Automation Factory", fill=(148, 163, 184), font=subtitle_font)

    # 4. शानदार कार्ड्स (Cards UI) जिन पर सर्विसेज लिखी होंगी
    services = [
        ("⚡ Custom AI App Development", "Build tailored intelligent software"),
        ("🤖 24x7 Autonomous AI Agents", "Run automated workflows seamlessly"),
        ("🐍 Advanced Python Automation", "Eliminate manual tasks completely"),
        ("🚀 Micro-SaaS Architecture", "Launch scalable revenue products")
    ]
    
    start_y = 450
    for title, desc in services:
        # कार्ड का बैकग्राउंड (Rounded Sleek Box)
        draw.rounded_rectangle([80, start_y, 920, start_y + 130], radius=18, fill=(22, 27, 34), outline=(56, 189, 248), width=2)
        
        # सर्विस का टाइटल और डिस्क्रिप्शन
        draw.text((120, start_y + 25), title, fill=(74, 222, 128), font=card_font) # Neon Green
        draw.text((120, start_y + 70), desc, fill=(203, 213, 225), font=subtitle_font)
        
        start_y += 160

    # 5. बॉटम में दमदार Call to Action (CTA) बटन
    draw.rounded_rectangle([80, 1220, 920, 1340], radius=25, fill=(37, 99, 235)) # Professional Blue Button
    draw.text((180, 1255), "Hire Experts on Upwork & Fiverr", fill=(255, 255, 255), font=cta_font)

    # 6. फाइल सेव करें
    output_path = "smart_professional_pin.png"
    image.save(output_path)
    print(f"🔥 Smart Professional Pin successfully created at: {output_path}")

if __name__ == "__main__":
    generate_smart_template()
