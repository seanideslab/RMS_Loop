#!/usr/bin/env bash
set -euo pipefail
python scripts/run_policy_engine.py --config configs/policy_budgets.yaml
python scripts/run_pts_evaluation.py --config configs/pts_weights.yaml
python scripts/run_telemetry_robustness.py
python scripts/run_closed_loop_simulation.py --config configs/closed_loop_defaults.yaml
python scripts/generate_tables_figures.py
