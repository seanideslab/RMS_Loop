# RMS-Loop Artifact

**Manuscript:** *RMS-Loop: A Deployment-Aware Architecture and Evaluation Blueprint for Closed-Loop Memory-Safety Operations in Legacy C/C++ Systems*

This repository supports the component-level studies and offline control-flow simulation reported in the JISA resubmission of RMS-Loop. The artifact is intended to reproduce the reported tables and figures for the adaptive policy-engine study, CRM/PTS candidate-patch admission study, noisy closed-loop replay, telemetry degradation analysis, and baseline comparison.

RMS-Loop is not provided here as a production deployment or as an AI/ML repair model. Externally generated candidate patches are treated only as inputs to the CRM/PTS governance pipeline. The manuscript contribution is a deployment-aware memory-safety control-plane architecture and evaluation blueprint.

## Artifact scope

This artifact provides:
- final result CSV files aligned with the JISA-safe manuscript;
- plotting scripts for manuscript figures, especially the updated Fig. 9;
- reproducibility metadata, including table/figure mapping, field definitions, and seed documentation;
- configuration placeholders for component-level and offline replay studies.

This artifact does **not** claim to provide production-scale validation, live telemetry, silicon-level hardware validation, or a repository-scale APR benchmark.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/plot_fig9.py
```

To regenerate currently included lightweight figures:

```bash
python scripts/reproduce_all.py
```

Generated figures are written to `figures/`.

## Repository structure

```text
configs/        Configuration files and placeholders for simulation runs
data/           Raw or source input data, when available
figures/        Generated manuscript figures
results/        Final CSV result tables used by the manuscript
rmsloop/        RMS-Loop package placeholder / implementation modules
scripts/        Plotting and reproduction scripts
tests/          Lightweight validation tests
```

## Main manuscript alignment

The current result files are aligned with the JISA resubmission version using the following main text numbering:
- Tables 6–13
- Figures 6–9
- Graphical abstract

See `MANIFEST.md` for exact file-to-table/figure mapping.
