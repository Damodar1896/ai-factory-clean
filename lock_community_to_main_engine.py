import os

print("[*] Integrating Professional Community Architect with the Main System...")

# Main engine me community manager ka hook jod rahe hain
engine_file = "master_retention_payment_hub.py"
if os.path.exists(engine_file):
    with open(engine_file, "r") as f:
        content = f.read()
    
    if "ProfessionalCommunityArchitect" not in content:
        integration_snippet = """
# Auto-injected Community & Group Rotator Hook
try:
    from setup_professional_communities import ProfessionalCommunityArchitect
    community_architect = ProfessionalCommunityArchitect()
except ImportError:
    community_architect = None
"""
        with open(engine_file, "w") as f:
            f.write(integration_snippet + "\n" + content)
        print("[✅ SUCCESS] Community Architect successfully locked and wired into the payment & retention hub!")
    else:
        print("[*] Community Architect is already locked in.")

print("[🚀 LOCKED FOREVER] Group rotation, numbering, and professional community dispatch are now 100% automated!")
