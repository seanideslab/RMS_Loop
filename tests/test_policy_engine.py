from rmsloop.policy_engine import evaluate_policies, select_policy
from rmsloop.utils import read_csv


def test_select_policy_respects_budget():
    evaluated = evaluate_policies(read_csv('data/overhead_models/hardware_policy_costs.csv'), budget=5.0)
    selected = select_policy(evaluated)
    assert selected['overhead_pct'] <= 5.0
    assert selected['feasible']
