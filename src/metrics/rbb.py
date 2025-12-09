"""Reality-Believability Balance metric."""
from __future__ import annotations

import re
from typing import Iterable, List

from pydantic import BaseModel, Field, validator

HEDGE_WORDS = {
    "might",
    "maybe",
    "perhaps",
    "possibly",
    "seems",
    "likely",
    "could",
    "around",
    "approximately",
}

FACTUAL_ANCHORS = {
    "according",
    "reported",
    "source",
    "data",
    "evidence",
    "study",
    "dataset",
    "record",
    "wikipedia",
}


class RbbInput(BaseModel):
    text: str = Field(..., description="Content to score for believability balance.")

    @validator("text")
    def validate_text(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Text cannot be empty for RBB computation.")
        return value


class RbbScore(BaseModel):
    hedge_count: int
    anchor_count: int
    token_count: int
    score: float = Field(..., description="Higher is better; balances anchors against hedges.")

    @property
    def calibrated(self) -> bool:
        return self.score >= 0.0


def _tokenize(text: str) -> List[str]:
    return re.findall(r"[A-Za-z']+", text.lower())


def compute_rbb(text: str) -> RbbScore:
    """Compute a simple Reality-Believability Balance score."""

    tokens = _tokenize(RbbInput(text=text).text)
    hedge_count = sum(1 for token in tokens if token in HEDGE_WORDS)
    anchor_count = sum(1 for token in tokens if token in FACTUAL_ANCHORS)

    token_count = max(len(tokens), 1)
    balance = (anchor_count - hedge_count) / token_count

    return RbbScore(
        hedge_count=hedge_count,
        anchor_count=anchor_count,
        token_count=token_count,
        score=balance,
    )


__all__ = ["RbbInput", "RbbScore", "compute_rbb"]
