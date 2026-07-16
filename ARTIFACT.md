# RMS-Loop Artifact Description

## Scope

This artifact reproduces the reported tables and figures for the adaptive policy-engine study, CRM/PTS candidate-patch admission study, noisy closed-loop replay, telemetry degradation analysis, and baseline comparison in the JISA resubmission of RMS-Loop.

The artifact supports the manuscript's deployment-aware architecture and evaluation-blueprint framing. It does not constitute:
- production-scale deployment validation;
- silicon-level hardware validation;
- a full repository-scale APR benchmark;
- a new AI/ML model, training procedure, or repair algorithm.

Externally generated candidate patches, including those produced by APR or LLM-assisted tools, are treated only as candidate inputs to the CRM/PTS governance pipeline.

## Reproducible items

Main manuscript tables reproduced or supported:
- Table 6: multi-granular tagging policy results
- Table 7: CRM/PTS ablation at the default admission threshold
- Table 8: CRM/PTS threshold sensitivity
- Table 9: rollback and failure summary
- Table 10: offline control-flow policy replay
- Table 11: noisy closed-loop replay ablation
- Table 12: deployment rounds and time-to-mitigation
- Table 13: baseline comparison

Main manuscript figures reproduced or supported:
- Fig. 6: policy-engine frontier and capture behavior
- Fig. 7: CRM/PTS evaluation
- Fig. 8: closed-loop deployment dynamics
- Fig. 9: robustness and baseline comparison

## Requirements

Install Python dependencies:

```bash
pip install -r requirements.txt
```

The included Fig. 9 script requires Python 3.10+, pandas, numpy, and matplotlib.

## Reproduction

Run:

```bash
python scripts/reproduce_all.py
```

This currently regenerates the manuscript-aligned Fig. 9 from CSV files. Scripts for Fig. 6–8 can be retained or added according to the local repository's existing workflow.

## Validation boundary

The artifact is designed for offline reproducibility of reported results and figure/table generation. It should be interpreted together with the manuscript's stated limitations: component-level evidence, synthetic workloads, analytic overhead assumptions, and offline control-flow simulation.
