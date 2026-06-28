from __future__ import annotations
from .risk_surface import update_risk

def simulate_closed_loop(rounds: int, canary_threshold: float, rollback_threshold: float, base_ttm_hours: float) -> list[dict]:
    rows=[]; risk=.5; weight=1.0
    for r in range(1, rounds+1):
        evidence=min(.95,.42+.055*r); risk=update_risk(risk,evidence)
        rollback=risk>=rollback_threshold; canary_pass=risk<canary_threshold
        ttm=base_ttm_hours*(1-.055*r)*(.85 if canary_pass else 1.1); weight=round(weight+(.03 if rollback else .015),4)
        rows.append({'round':r,'risk':risk,'canary_pass':canary_pass,'rollback':rollback,'time_to_mitigation_hours':round(ttm,2),'pts_weight_multiplier':weight})
    return rows
