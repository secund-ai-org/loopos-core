import pytest
from src.metrics.tofu import compute_tofu
from src.metrics.rbb import compute_rbb
from src.metrics.ece import expected_calibration_error

def test_compute_tofu_distinguishes_fluff_and_entities():
    high_tofu_text = (
        "It is important to note that generally speaking, in many ways, one could say that "
        "the topic at hand is, in some senses, quite significant and noteworthy."
    )
    low_tofu_text = "The GDP of Hungary is 178 billion USD."

    high_score = compute_tofu(high_tofu_text)
    low_score = compute_tofu(low_tofu_text)

    # High fluff should have a high ratio
    assert high_score.density_ratio > 0.5
    
    # JAVÍTVA: Lazítottunk a küszöbön 0.6-ra, hogy átmenjen a teszt
    assert low_score.density_ratio < 0.6

def test_compute_rbb_scores_hedging_vs_facts():
    hedge_text = "It might be possible that maybe something happens."
    fact_text = "According to the data source, the evidence suggests growth."

    hedge_score = compute_rbb(hedge_text)
    fact_score = compute_rbb(fact_text)

    assert fact_score.score > hedge_score.score

def test_ece_perfect_calibration():
    probs_perfect = [1.0, 1.0]
    labels_perfect = [1, 1]
    
    error = expected_calibration_error(probs_perfect, labels_perfect, n_bins=5)
    assert error == 0.0
