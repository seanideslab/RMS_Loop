from __future__ import annotations
import csv
from pathlib import Path


def read_csv(path: str):
    with open(path, newline='') as f:
        rows=list(csv.DictReader(f))
    for row in rows:
        for k,v in list(row.items()):
            try: row[k]=float(v) if '.' in v else int(v)
            except (ValueError, TypeError): pass
    return rows


def write_csv(path: str, rows):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    rows=list(rows)
    if not rows: return
    with open(path,'w',newline='') as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)


def read_simple_yaml(path: str):
    cfg={}; stack=[cfg]; indents=[0]
    for raw in open(path):
        if not raw.strip() or raw.lstrip().startswith('#'): continue
        indent=len(raw)-len(raw.lstrip()); key,val=raw.strip().split(':',1); val=val.strip()
        while indent < indents[-1]: stack.pop(); indents.pop()
        if val=='':
            node={}; stack[-1][key]=node; stack.append(node); indents.append(indent+2)
        else:
            try: val=float(val) if '.' in val else int(val)
            except ValueError: pass
            stack[-1][key]=val
    return cfg
