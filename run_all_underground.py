import os
import subprocess

modules = [
    "automation_core/module_underground_01_correction.py",
    "automation_core/module_underground_02_nostalgia.py",
    "automation_core/module_underground_03_paradox.py",
    "automation_core/module_underground_04_cadence.py",
    "automation_core/module_underground_05_spy.py",
    "automation_core/module_underground_06_cascade.py",
    "automation_core/module_underground_07_raw.py",
    "automation_core/module_underground_08_silo.py",
    "automation_core/module_underground_09_fomo.py",
    "automation_core/module_underground_10_loop.py"
]

print("="*70)
print("[*] [MASTER RUNNER] Executing All 10 Personal Underground Retention Modules...")
print("="*70)

for mod in modules:
    print(f"\n[RUNNING] -> {mod}")
    subprocess.run(["python", mod], check=True)

print("\n" + "="*70)
print("[SUCCESS] All 10 individual underground retention modules successfully executed and logged!")
print("="*70)
