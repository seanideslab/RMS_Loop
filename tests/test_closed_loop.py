from rmsloop.closed_loop import simulate_closed_loop


def test_closed_loop_round_count():
    out = simulate_closed_loop(8, .65, .78, 72)
    assert len(out) == 8
    assert all(r['time_to_mitigation_hours'] > 0 for r in out)
