#!/usr/bin/env python3
"""Reproduce lightweight manuscript-aligned figures included in this artifact."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
scripts = [ROOT / "scripts" / "plot_fig9.py"]

for script in scripts:
    print(f"Running {script.relative_to(ROOT)}")
    subprocess.check_call([sys.executable, str(script)])

print("Reproduction complete.")
