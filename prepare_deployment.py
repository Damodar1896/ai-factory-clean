import os

# 1. Create requirements.txt for deployment
requirements = """fastapi==0.110.0
uvicorn==0.28.0
pydantic==2.6.4
requests==2.31.0
jinja2==3.1.3
"""

with open("~/ai-factory/affiliate_bot/requirements.txt".replace("~", os.path.expanduser("~")), "w", encoding="utf-8") as f:
    f.write(requirements)

# 2. Create Procfile for cloud deployment (Render / Railway)
with open("~/ai-factory/affiliate_bot/Procfile".replace("~", os.path.expanduser("~")), "w", encoding="utf-8") as f:
    f.write("web: uvicorn app:app --host 0.0.0.0 --port $PORT\n")

print("[Success] Deployment files (requirements.txt and Procfile) generated successfully!")
