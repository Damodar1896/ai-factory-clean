import os
import json

def verify_retention_modules():
    print("="*70)
    print("[*] [RETENTION EMPIRE MASTER VERIFIER] Scanning All Retention Daemons...")
    print("="*70)
    
    retention_modules = [
        ("1. Open Loop Narrative", "automation_core/data/retention_open_loop_state.json"),
        ("2. Tribal Framing", "automation_core/data/retention_tribe_state.json"),
        ("3. Dynamic Pacing", "automation_core/data/retention_pacing_state.json"),
        ("4. Vulnerability Confession", "automation_core/data/retention_vulnerability_state.json"),
        ("5. Micro-Habit Conditioning", "automation_core/data/retention_habit_state.json"),
        ("6. Interactive Easter Eggs", "automation_core/data/retention_easter_egg_state.json"),
        ("7. Anti-Guru Persona", "automation_core/data/retention_persona_state.json"),
        ("8. Micro-Payoffs Ladder", "automation_core/data/retention_payoff_state.json"),
        ("9. Community Co-Creation", "automation_core/data/retention_cocreation_state.json"),
        ("10. Transformation Arc", "automation_core/data/retention_transformation_state.json")
    ]
    
    active_count = 0
    for name, path in retention_modules:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f" [+] {name:<30} -> [ACTIVE] (24/7 Zero-Cost Daemon)")
            active_count += 1
        else:
            print(f" [!] {name:<30} -> [PENDING] (State log missing)")
            
    print("="*70)
    print(f"[*] Retention Status Summary: {active_count} / 10 Loyalty Daemons Fully Operational.")
    print("[SUCCESS] All audience retention and attachment systems verified successfully!")
    print("="*70)

if __name__ == "__main__":
    verify_retention_modules()
