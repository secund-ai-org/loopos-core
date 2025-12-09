"""Semantic density calculator for TOFU (Totally Futile content Index)."""
from __future__ import annotations

import re
from typing import Iterable, List, Sequence, Set

from pydantic import BaseModel, Field, validator


def _default_stopwords() -> Set[str]:
    return {
        "a",
        "an",
        "the",
        "and",
        "or",
        "but",
        "so",
        "to",
        "of",
        "for",
        "in",
        "on",
        "with",
        "at",
        "from",
        "by",
        "about",
        "as",
        "into",
        "like",
        "through",
        "after",
        "over",
        "between",
        "out",
        "against",
        "during",
        "without",
        "before",
        "under",
        "around",
        "among",
        "just",
        "very",
        "really",
        "actually",
        "basically",
        "literally",
        "simply",
        "kind",
        "sort",
        "maybe",
        "perhaps",
    }


class TofuInput(BaseModel):
    """Input schema for TOFU evaluation."""

    text: str = Field(..., description="Text to analyze for semantic density.")
    stopwords: Sequence[str] | None = Field(
        default=None, description="Optional custom stopword list to override the default set."
    )

    @validator("text")
    def validate_text(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Input text must not be empty.")
        return value


class TofuScore(BaseModel):
    """Result of a TOFU calculation."""

    fluff_tokens: List[str]
    entity_tokens: List[str]
    total_tokens: int
    density_ratio: float = Field(..., description="Fluff-to-entity ratio; lower is better.")

    @property
    def has_signal(self) -> bool:
        return self.total_tokens > 0 and bool(self.entity_tokens)


_TOKEN_PATTERN = re.compile(r"[A-Za-z0-9']+")


def _tokenize(text: str) -> List[str]:
    return [token for token in _TOKEN_PATTERN.findall(text) if token]


def _identify_entities(tokens: Sequence[str], stopwords: Set[str]) -> List[str]:
    entities: list[str] = []
    for index, token in enumerate(tokens):
        normalized = token.lower()
        is_stopword = normalized in stopwords
        looks_numeric = any(char.isdigit() for char in token)
        looks_title = token[0].isupper() and (index != 0 or len(token) > 1)
        is_acronym = token.isupper() and len(token) > 1
        if not is_stopword and (looks_title or looks_numeric or is_acronym):
            entities.append(token)
    return entities


def _identify_fluff(tokens: Sequence[str], stopwords: Set[str]) -> List[str]:
    return [token for token in tokens if token.lower() in stopwords]


def compute_tofu(text: str, stopwords: Iterable[str] | None = None) -> TofuScore:
    """Compute the semantic density of text as a TOFU score.

    The score is defined as the ratio of filler/stopwords to detected entities.
    A lower ratio indicates denser, more information-rich content.
    """

    stopword_set = set(stopwords) if stopwords else _default_stopwords()
    input_model = TofuInput(text=text, stopwords=list(stopword_set))

    tokens = _tokenize(input_model.text)
    fluff_tokens = _identify_fluff(tokens, stopword_set)
    entity_tokens = _identify_entities(tokens, stopword_set)

    entity_count = max(len(entity_tokens), 1)  # avoid division by zero
    density_ratio = len(fluff_tokens) / entity_count

    return TofuScore(
        fluff_tokens=fluff_tokens,
        entity_tokens=entity_tokens,
        total_tokens=len(tokens),
        density_ratio=density_ratio,
    )


__all__ = ["TofuInput", "TofuScore", "compute_tofu"]
