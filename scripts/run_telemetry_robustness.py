#!/usr/bin/env python
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from rmsloop.telemetry import normalize_evidence
from rmsloop.utils import read_csv, write_csv

def main():
    workloads=[]
    for n in ['spatial','temporal','hybrid']: workloads += read_csv(f'data/synthetic_workloads/{n}_cases.csv')
    scenarios={'nominal':(0,0,0),'missing':(.25,0,0),'delayed':(0,.35,0),'poisoned':(0,0,.2),'combined':(.15,.2,.1)}; rows=[]
    for name,(m,d,p) in scenarios.items():
        out=normalize_evidence(workloads,m,d,p)
        rows.append({'scenario':name,'capture_rate':round(sum(r['captured'] for r in out)/len(out),4),'normalization_quality':round(sum(r['normalized_evidence'] for r in out)/len(out),4)})
    write_csv('results/generated/telemetry_robustness.csv', rows)
if __name__=='__main__': main()
