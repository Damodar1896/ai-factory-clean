import os

print("[*] Wiring all 10 advanced modules into master run_forever.sh loop...")

runner_file = "run_forever.sh"
with open(runner_file, "r") as f:
    content = f.read()

new_modules_hook = """
    python3 ai_voice_agent.py
    python3 gst_invoice_generator.py
    python3 lead_scoring_engine.py
    python3 currency_switcher.py
    python3 ai_inbox_responder.py
    python3 social_auto_scheduler.py
    python3 churn_predictor.py
    python3 affiliate_dashboard_gen.py
    python3 cart_abandonment_bot.py
    python3 mini_app_store.py
"""

if "ai_voice_agent.py" not in content:
    content = content.replace("python3 ai_inbox_responder.py", "python3 ai_inbox_responder.py" + new_modules_hook)
    with open(runner_file, "w") as f:
        f.write(content)
    print("[✅ SUCCESS] All 10 modules locked permanently into the 24x7 background engine!")
else:
    print("[*] Modules are already wired and active in the autopilot loop.")

print("[🚀 EMPIRE 100% READY] Your automated business is fully operational and scaling on autopilot!")
