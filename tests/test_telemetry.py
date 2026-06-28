from rmsloop.telemetry import normalize_evidence
from rmsloop.utils import read_csv


def test_telemetry_degrades_with_missing_data():
    df = read_csv('data/synthetic_workloads/spatial_cases.csv')
    nominal = normalize_evidence(df)
    missing = normalize_evidence(df, missing=.5)
    assert sum(r['normalized_evidence'] for r in missing) < sum(r['normalized_evidence'] for r in nominal)
