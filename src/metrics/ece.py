"""Expected Calibration Error metric implementation."""
from __future__ import annotations

from typing import Iterable, Sequence

import numpy as np
from pydantic import BaseModel, Field, root_validator, validator


class CalibrationInput(BaseModel):
    """Validation schema for calibration data."""

    probabilities: Sequence[float]
    labels: Sequence[int]
    n_bins: int = Field(default=10, ge=1, description="Number of bins for calibration.")

    @validator("probabilities")
    def validate_probabilities(cls, values: Sequence[float]) -> Sequence[float]:
        if not values:
            raise ValueError("At least one probability is required.")
        for probability in values:
            if not 0.0 <= probability <= 1.0:
                raise ValueError("Probabilities must be between 0 and 1.")
        return values

    @validator("labels")
    def validate_labels(cls, values: Sequence[int]) -> Sequence[int]:
        if not values:
            raise ValueError("At least one label is required.")
        for label in values:
            if label not in (0, 1):
                raise ValueError("Labels must be 0 or 1 for ECE computation.")
        return values

    @root_validator
    def validate_lengths(cls, values: dict) -> dict:
        probabilities = values.get("probabilities")
        labels = values.get("labels")
        if probabilities is not None and labels is not None and len(probabilities) != len(labels):
            raise ValueError("Probabilities and labels must have the same length.")
        return values


def expected_calibration_error(
    probabilities: Sequence[float], labels: Sequence[int], n_bins: int = 10
) -> float:
    """Compute Expected Calibration Error (ECE).

    The metric partitions predictions into ``n_bins`` bins and compares the average
    confidence with the empirical accuracy in each bin. Empty bins are ignored.
    
    Args:
        probabilities: Model confidence scores between 0 and 1.
        labels: Ground-truth binary labels (0 or 1).
        n_bins: Number of equal-width bins to use.

    Returns:
        Weighted average of the absolute accuracy-confidence gap across bins.
    """

    data = CalibrationInput(probabilities=probabilities, labels=labels, n_bins=n_bins)

    prob_array = np.asarray(data.probabilities, dtype=float)
    label_array = np.asarray(data.labels, dtype=int)

    bin_edges = np.linspace(0.0, 1.0, data.n_bins + 1)
    bin_ids = np.digitize(prob_array, bin_edges[1:-1], right=True)

    total_count = len(prob_array)
    ece = 0.0

    for bin_index in range(data.n_bins):
        mask = bin_ids == bin_index
        if not np.any(mask):
            continue

        bin_probs = prob_array[mask]
        bin_labels = label_array[mask]

        avg_confidence = float(np.mean(bin_probs))
        avg_accuracy = float(np.mean(bin_labels))
        proportion = float(np.sum(mask)) / total_count

        ece += proportion * abs(avg_accuracy - avg_confidence)

    return float(ece)


def batch_ece(records: Iterable[CalibrationInput]) -> float:
    """Compute the mean ECE across multiple calibration batches."""

    ece_values = [expected_calibration_error(r.probabilities, r.labels, r.n_bins) for r in records]
    if not ece_values:
        raise ValueError("No calibration records provided.")
    return float(np.mean(ece_values))


__all__ = ["CalibrationInput", "expected_calibration_error", "batch_ece"]
