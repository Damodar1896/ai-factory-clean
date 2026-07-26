import subprocess
import os

modules = [
    "automation_core/module_safety_01_proxy.py",
    "automation_core/module_safety_02_jitter.py",
    "automation_core/module_safety_03_fingerprint.py",
    "automation_core/module_safety_04_circuit.py",
    "automation_core/module_safety_05_warmup.py",
    "automation_core/module_safety_06_drift.py",
    "automation_core/module_safety_07_mutation.py",
    "automation_core/module_safety_08_killswitch.py",
    "automation_core/module_safety_09_throttle.py",
    "automation_core/module_safety_10_backup.py"
]

print("="*70)
print("[*] [MASTER SAFETY RUNNER] Executing All 10 Anti-Ban Safety Modules...")
print("="*70)

for mod in modules:
    print(f"\n[RUNNING] -> {mod}")
    subprocess.run(["python", mod], check=True)

print("\n" + "="*70)
print("[SUCCESS] All 10 personal safety modules successfully executed and logged!")
print("="*70)
