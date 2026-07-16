# Data Dictionary

## Common fields

- `theta`: CRM/PTS admission threshold. The default threshold is θ = 0.70.
- `N`: number of candidate patches. The controlled CRM/PTS study uses N = 90 candidates.
- `pauc_5`: partial AUROC restricted to the low-FPR region, FPR ≤ 5%.
- `auroc`: full area under the ROC curve.
- `f1`: harmonic mean of precision and recall.
- `precision`: true positives divided by all admitted positives.
- `recall`: true positives divided by all actual positives.
- `specificity`: true negatives divided by all actual negatives.
- `fa_adv`: false accepts among adversarial candidate patches.
- `fa_bloat`: false accepts among bloated candidate patches.

## Fig. 9 fields

### `results/fig9_poisoning_defense.csv`
- `poison_rate`: telemetry poisoning level.
- `method`: defense condition.
- `risk_score`: decoy-module risk score.
- `error`: symmetric error-bar value.

### `results/fig9_telemetry_degradation.csv`
- `condition`: telemetry degradation condition.
- `normalized_evidence_yield`: delivered usable evidence divided by generated evidence, normalized to clean baseline = 1.0.

### `results/table13_baseline_comparison.csv`
- `method`: candidate-patch admission method or simplified baseline.
- `precision`, `recall`, `specificity`, `f1`: classification metrics used in the baseline comparison.

## Interpretation notes

Values in the artifact should be interpreted as component-level and offline simulation results under stated assumptions. They should not be interpreted as production-scale or silicon-level validation.
