import os

with open("app.py", "r", encoding="utf-8") as f:
    code = f.read()

if "app = FastAPI()" not in code:
    # Prepend fastap import and app initialization
    fixed_code = "from fastapi import FastAPI\nfrom fastapi.responses import HTMLResponse\n\napp = FastAPI()\n\n" + code
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(fixed_code)
    print("[Success] FastAPI app initialization added to app.py!")
else:
    print("[Info] FastAPI app initialization already exists.")
