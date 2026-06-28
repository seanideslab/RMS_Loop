#!/usr/bin/env python
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rmsloop.plotting import bars, line, scatter
from rmsloop.utils import read_csv


def main():
    policy = read_csv('results/generated/table7_policy_results.csv')
    scatter('figures/generated/fig6_policy_frontier.png', [float(r['overhead_pct']) for r in policy], [float(r['capture_probability']) for r in policy])
    bars('figures/generated/fig7_roc_pr_analysis.png', [1.0, 1.0, 1.0])
    pts = read_csv('results/generated/table9_pts_ablation.csv')
    bars('figures/generated/fig8_pts_distribution.png', [float(r['pts_score']) for r in pts])
    bars('figures/generated/fig9_pts_ablation.png', [float(r['pts_score']) for r in pts])
    closed = read_csv('results/generated/table13_closed_loop_metrics.csv')
    line('figures/generated/fig10_closed_loop_ttm.png', [float(r['time_to_mitigation_hours']) for r in closed])
    telemetry = read_csv('results/generated/telemetry_robustness.csv')
    bars('figures/generated/fig11_telemetry_robustness.png', [float(r['capture_rate']) for r in telemetry])


if __name__ == '__main__':
    main()
