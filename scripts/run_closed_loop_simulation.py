#!/usr/bin/env python
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rmsloop.closed_loop import simulate_closed_loop
from rmsloop.utils import write_csv, read_simple_yaml
import argparse

def main():
    p=argparse.ArgumentParser(); p.add_argument('--config', default='configs/closed_loop_defaults.yaml'); args=p.parse_args(); cfg=read_simple_yaml(args.config)
    out=simulate_closed_loop(cfg['rounds'], cfg['canary_threshold'], cfg['rollback_threshold'], cfg['base_ttm_hours'])
    write_csv('results/generated/table13_closed_loop_metrics.csv', out)
    write_csv('results/generated/table12_closed_loop_ablation.csv', [dict(r, ablation='disabled_feedback') for r in out])
if __name__=='__main__': main()
