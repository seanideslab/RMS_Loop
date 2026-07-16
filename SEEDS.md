# Seeds and Reproducibility Notes

The final manuscript reports seeded component-level and offline replay studies.

## Reported seeded settings

- Policy-engine component study: 50 seeded runs per configuration.
- CRM/PTS candidate-patch study: 30 Juliet C/C++ vulnerability instances and 90 candidate patches.
- Offline control-flow replay: fixed synthetic replay seeds for canary, rollback, risk-surface update, and telemetry degradation analyses.

## Suggested local seed defaults

```text
policy_engine_runs: 1-50
closed_loop_replay_seeds: 1-30
telemetry_degradation_seeds: 1-30
baseline_comparison_seeds: 1-15
```

## Boundary

The seeds support reproducible offline analysis only. They do not represent production trace randomness or silicon-level hardware variability.
