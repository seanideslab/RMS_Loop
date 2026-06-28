#!/usr/bin/env python
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rmsloop.policy_engine import evaluate_policies, select_policy
from rmsloop.utils import read_csv, write_csv, read_simple_yaml
import argparse

def main():
    p=argparse.ArgumentParser(); p.add_argument('--config', default='configs/policy_budgets.yaml'); args=p.parse_args()
    cfg=read_simple_yaml(args.config); out=evaluate_policies(read_csv('data/overhead_models/hardware_policy_costs.csv'), cfg['overhead_budget_pct'], cfg['security_weight'], cfg['overhead_weight'])
    selected=select_policy(out)['policy']
    for r in out: r['selected']=r['policy']==selected
    write_csv('results/generated/table7_policy_results.csv', out)
if __name__=='__main__': main()
