# Artifact Evaluation Guide

## Install

```bash
python -m venv .venv
source .venv/bin/activate
# Optional scientific-stack extensions only:
# pip install -r requirements.txt
```

## Run all experiments

```bash
bash scripts/run_all.sh
```

## Individual runs

```bash
python scripts/run_policy_engine.py --config configs/policy_budgets.yaml
python scripts/run_pts_evaluation.py --config configs/pts_weights.yaml
python scripts/run_telemetry_robustness.py
python scripts/run_closed_loop_simulation.py --config configs/closed_loop_defaults.yaml
python scripts/generate_tables_figures.py
```

Successful execution creates CSV files in `results/generated/` and plots in `figures/generated/`. Main numeric outputs should match the expected schema and remain within normal floating-point rounding tolerance because all inputs are deterministic.

## Troubleshooting

If imports fail, ensure the command is run from the repository root. The baseline scripts are self-contained and do not require installing `requirements.txt`.
