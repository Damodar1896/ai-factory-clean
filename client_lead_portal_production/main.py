
from fastapi import FastAPI, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import database

app = FastAPI(title="Damodar SaaS Engine")
database.init_db()

templates = Jinja2Templates(directory="templates")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_dashboard(request: Request, db: Session = Depends(get_db)):
    leads = db.query(database.Lead).all()
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>SaaS Control Center | Damodar Tech Craze</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-black text-white font-sans p-10">
        <div class="max-w-4xl mx-auto bg-zinc-900 border border-zinc-800 p-8 rounded-2xl shadow-2xl">
            <h1 class="text-3xl font-bold text-blue-500 mb-2">🔥 Automated Micro-SaaS Dashboard</h1>
            <p class="text-zinc-400 mb-6">Manage incoming client leads and automated AI triggers instantly.</p>
            
            <div class="bg-zinc-950 p-6 rounded-xl border border-zinc-800 mb-8">
                <h2 class="text-xl font-semibold mb-4 text-white">Capture New Lead</h2>
                <form action="/add-lead" method="POST" class="space-y-4">
                    <div>
                        <label class="block text-sm text-zinc-400 mb-1">Client Name</label>
                        <input type="text" name="name" required class="w-full bg-zinc-900 border border-zinc-700 rounded-lg p-3 text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-sm text-zinc-400 mb-1">Email Address</label>
                        <input type="email" name="email" required class="w-full bg-zinc-900 border border-zinc-700 rounded-lg p-3 text-white focus:outline-none focus:border-blue-500">
                    </div>
                    <div>
                        <label class="block text-sm text-zinc-400 mb-1">Requirement / Message</label>
                        <textarea name="message" required class="w-full bg-zinc-900 border border-zinc-700 rounded-lg p-3 text-white focus:outline-none focus:border-blue-500"></textarea>
                    </div>
                    <button type="submit" class="w-full bg-blue-600 hover:bg-blue-500 font-semibold py-3 rounded-lg transition">Deploy Auto-Responder & Save Lead</button>
                </form>
            </div>

            <div>
                <h2 class="text-xl font-semibold mb-4 text-white">Stored Leads Database (Live)</h2>
                <div class="space-y-3">
                    {% for lead in leads %}
                    <div class="bg-zinc-950 p-4 rounded-xl border border-zinc-800 flex justify-between items-center">
                        <div>
                            <p class="font-bold text-lg text-white">{{ lead.client_name }}</p>
                            <p class="text-sm text-blue-400">{{ lead.email }}</p>
                            <p class="text-sm text-zinc-400 mt-1">{{ lead.message }}</p>
                        </div>
                        <span class="bg-green-500/10 text-green-400 text-xs px-3 py-1 rounded-full border border-green-500/20">Active Auto-Pilot</span>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </body>
    </html>
    '''
    # Simple inline template rendering simulation for standalone file execution
    return HTMLResponse(content=html_content.replace("{% for lead in leads %}", "").replace("{% endfor %}", ""))

@app.post("/add-lead")
def add_lead(name: str = Form(...), email: str = Form(...), message: str = Form(...), db: Session = Depends(get_db)):
    new_lead = database.Lead(client_name=name, email=email, message=message)
    db.add(new_lead)
    db.commit()
    return RedirectResponse(url="/", status_code=303)
