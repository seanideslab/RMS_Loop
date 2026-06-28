from __future__ import annotations

def evaluate_policies(costs: list[dict], budget: float, security_weight: float = 0.7, overhead_weight: float = 0.3) -> list[dict]:
    rows=[]
    for row in costs:
        out=dict(row); out['feasible']=float(out['overhead_pct']) <= budget
        penalty=float(out['overhead_pct'])/max(budget,1e-9)
        out['policy_score']=round(security_weight*float(out['capture_probability']) + 0.1*float(out['compatibility']) - overhead_weight*penalty,4)
        if not out['feasible']: out['policy_score']-=1.0
        rows.append(out)
    return sorted(rows, key=lambda r:(r['feasible'], r['policy_score']), reverse=True)

def select_policy(evaluated: list[dict]) -> dict:
    for row in evaluated:
        if row['feasible']: return row
    raise ValueError('No policy satisfies the overhead budget')
