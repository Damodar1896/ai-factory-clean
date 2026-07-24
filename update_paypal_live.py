import os

with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace dummy paypal link with real paypal link
if "https://paypal.me/damodartechcraze" not in content:
    # We will replace the paypal href in the checkout page
    old_snippet = 'href="https://paypal.me/damodartechcraze"' # or similar placeholder
    # Let's do a robust replacement of the paypal-box section
    print("[Info] Updating PayPal link...")

# Let's rewrite the checkout file cleanly with the real PayPal link
update_script = """
import os

with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the paypal anchor href
if 'href="https://paypal.me/' in content:
    # Already has some paypal link, let's replace it
    import re
    content = re.sub(r'href="https://paypal\.me/[^"]*?"', 'href="https://paypal.me/damodartechcraze"', content)
else:
    pass

with open("app.py", "w", encoding="utf-8") as f:
    f.write(content)
print("[Success] Real PayPal link successfully integrated into app.py!")
"""

exec(update_script)
