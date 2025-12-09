"""Expected Calibration Error metric implementation."""
from __future__ import annotations

from typing import Iterable, Sequence

import numpy as np
from pydantic import BaseModel, Field, field_validator, model_validator


class CalibrationInput(BaseModel):
    """Validation schema for calibration data."""

    probabilities: Sequence[float]
    labels: Sequence[int]
    n_bins: int = Field(default=10, ge=1, description="Number of bins for calibration.")

    @field_validator("probabilities")
    @classmethod
    def validate_probabilities(cls, values: Sequence[float]) -> Sequence[float]:
        if not values:
            raise ValueError("At least one probability is required.")
        for probability in values:
            if not 0.0 <= probability <= 1.0:
                raise ValueError("Probabilities must be between 0 and 1.")
        return values

    @field_validator("labels")
    @classmethod
    def validate_labels(cls, values: Sequence[int]) -> Sequence[int]:
        if not values:
            raise ValueError("At least one label is required.")
        for label in values:
            if label not in (0, 1):
                raise ValueError("Labels must be 0 or 1 for ECE computation.")
        return values

    @model_validator(mode='after')
    def validate_lengths(self) -> 'CalibrationInput':
        if len(self.probabilities) != len(self.labels):
            raise ValueError("Probabilities and labels must have the same length.")
        return self


def expected_calibration_error(
    probabilities: Sequence[float], labels: Sequence[int], n_bins: int = 10
) -> float:
    """Compute Expected Calibration Error (ECE)."""

    # Validate inputs using Pydantic V2
    data = CalibrationInput(probabilities=probabilities, labels=labels, n_bins=n_bins)

    prob_array = np.asarray(data.probabilities, dtype=float)
    label_array = np.asarray(data.labels, dtype=int)

    bin_edges = np.linspace(0.0, 1.0, data.n_bins + 1)
    bin_ids = np.digitize(prob_array, bin_edges[1:-1], right=True)

    ece = 0.0
    total_count = len(prob_array)

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
    # Note: inputs here are already validated objects
    ece_values = [
        expected_calibration_error(r.probabilities, r.labels, r.n_bins) 
        for r in records
    ]
    if not ece_values:
        raise ValueError("No calibration records provided.")
    return float(np.mean(ece_values))
