import math

from src.metrics.ece import expected_calibration_error
from src.metrics.rbb import compute_rbb
from src.metrics.tofu import compute_tofu


def test_compute_tofu_density_ratios():
    dense_fluff = "This is a very good and nice result."
    rich_entities = "Europan Union AI Act Article 13 compliance."

    fluff_score = compute_tofu(dense_fluff)
    entity_score = compute_tofu(rich_entities)

    assert fluff_score.density_ratio > entity_score.density_ratio
    assert entity_score.density_ratio <= 0.5


def test_compute_rbb_balances_anchors_and_hedges():
    hedge_text = "It might be possible that this is correct."
    anchor_text = "According to data from 2024 the report was published."

    hedge_score = compute_rbb(hedge_text)
    anchor_score = compute_rbb(anchor_text)

    assert hedge_score.score < 0
    assert anchor_score.score > hedge_score.score
    assert anchor_score.score > 0


def test_expected_calibration_error():
    perfectly_calibrated = expected_calibration_error([0.0, 1.0], [0, 1], n_bins=5)
    poorly_calibrated = expected_calibration_error([1.0, 1.0], [0, 0], n_bins=5)

    assert math.isclose(perfectly_calibrated, 0.0, abs_tol=1e-9)
    assert poorly_calibrated > 0.9
