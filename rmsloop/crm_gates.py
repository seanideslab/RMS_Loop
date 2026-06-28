from __future__ import annotations

def apply_crm_gates(scored: list[dict], threshold: float) -> list[dict]:
    rows=[]
    for row in scored:
        out=dict(row)
        out['admitted']=float(out['pts_score']) >= threshold and float(out['regression_risk']) <= .4 and float(out['test_evidence']) >= .6
        rows.append(out)
    return rows
