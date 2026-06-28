from rmsloop.pts import score_candidates
from rmsloop.crm_gates import apply_crm_gates
from rmsloop.utils import read_csv


def test_pts_scores_and_gates():
    weights = {'exploitability_reduction': .35, 'test_evidence': .25, 'static_confidence': .2, 'regression_risk': -.15, 'complexity_penalty': -.05}
    gated = apply_crm_gates(score_candidates(read_csv('data/juliet_patch_candidates/instances.csv'), weights), threshold=.62)
    assert 'pts_score' in gated[0]
    assert all(0 <= r['pts_score'] <= 1 for r in gated)
