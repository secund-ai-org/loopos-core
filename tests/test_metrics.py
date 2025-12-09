import math

from src.metrics.ece import expected_calibration_error
from src.metrics.rbb import compute_rbb
from src.metrics.tofu import compute_tofu


def test_compute_tofu_distinguishes_fluff_and_entities():
    high_tofu_text = (
        "It is important to note that generally speaking, in many ways, one could say that "
        "the topic at hand is, in some senses, quite significant and noteworthy."
    )
    low_tofu_text = "The GDP of Hungary is 178 billion USD."

    high_score = compute_tofu(high_tofu_text)
    low_score = compute_tofu(low_tofu_text)

    assert high_score.density_ratio > 0.5
    assert low_score.density_ratio < 0.2


def test_compute_rbb_balances_hedges_and_anchors():
    hedged_sentence = "This might possibly be true, maybe it is accurate."
    anchored_sentence = "According to the available evidence, the study was replicated."

    hedged_score = compute_rbb(hedged_sentence)
    anchored_score = compute_rbb(anchored_sentence)

    assert anchored_score.score > hedged_score.score
    assert hedged_score.score < 0


def test_expected_calibration_error_perfect_inputs():
    error = expected_calibration_error([0.9, 0.9], [1, 1])

    assert math.isclose(error, 0.1, abs_tol=0.1)
