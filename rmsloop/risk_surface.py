from __future__ import annotations


def update_risk(previous: float, evidence: float, learning_rate: float = 0.35) -> float:
    return round((1 - learning_rate) * previous + learning_rate * evidence, 4)
