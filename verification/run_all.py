#!/usr/bin/env python3
"""Run the complete scientific verification set from any working directory."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
for name in ("check_exact.py", "check_anisotropy.py", "check_near_pure.py", "check_circuit.py",
             "check_resources.py", "check_robustness.py"):
    print(f"Running {name}", flush=True)
    subprocess.run([sys.executable, str(ROOT / "verification" / name)], cwd=ROOT, check=True)
print("PASS: exact maps, near-pure blocks, circuit, resource accounting and finite-error checks.")
