from __future__ import annotations

def score_candidates(candidates: list[dict], weights: dict[str, float]) -> list[dict]:
    rows=[]
    for row in candidates:
        out=dict(row); score=sum(float(out[k])*float(w) for k,w in weights.items())
        out['pts_score']=round(min(1,max(0,score)),4); rows.append(out)
    return rows
