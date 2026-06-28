from __future__ import annotations

def normalize_evidence(workloads: list[dict], missing: float = 0.0, delayed: float = 0.0, poisoned: float = 0.0) -> list[dict]:
    rows=[]; trust=round((1-missing)*(1-.5*delayed)*(1-poisoned),4)
    for row in workloads:
        out=dict(row); out['trust']=trust
        out['normalized_evidence']=round(min(1,max(0,float(out['base_signal'])*float(out['criticality'])*trust)),4)
        out['captured']=out['normalized_evidence'] >= .45; rows.append(out)
    return rows
