# RMS-Loop Artifact

This repository contains the reproducibility artifact for the manuscript: "RMS-Loop: An Executable Architecture for Closed-Loop Memory-Safety Operations in Legacy C/C++ Systems."

## Scope

This artifact reproduces component-level studies and an offline closed-loop simulation. It is not a production deployment of RMS-Loop and does not claim a completed large-scale real-system deployment. The repository provides executable evaluation scripts, synthetic workloads, anonymized feature records, and analytic overhead assumptions.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
# Optional: pip install -r requirements.txt
bash scripts/run_all.sh
```

Expected runtime is under two minutes on a typical laptop. The baseline scripts use only the Python standard library; `requirements.txt` is provided for optional scientific-stack extensions.

## Reproducing Manuscript Results

| Manuscript item | Script | Output |
|---|---|---|
| Table 7 / Fig. 6 | `scripts/run_policy_engine.py` | `results/generated/table7_policy_results.csv` |
| Table 8 / Table 9 | `scripts/run_pts_evaluation.py` | `results/generated/table8_pts_metrics.csv` |
| Telemetry robustness / Fig. 11 | `scripts/run_telemetry_robustness.py` | `results/generated/telemetry_robustness.csv` |
| Table 12 / Table 13 / Fig. 10 | `scripts/run_closed_loop_simulation.py` | `results/generated/table13_closed_loop_metrics.csv` |

## Synthetic Data and Assumptions

The artifact uses synthetic workloads, anonymized candidate metadata, and analytic hardware-policy overhead models. Random seeds are listed in `configs/random_seeds.yaml`.

## License

MIT License, attributed to Anonymous Authors for double-anonymous review.
