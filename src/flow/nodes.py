"""Graph nodes implementing the verification loop steps."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from pydantic import BaseModel


class LoopState(BaseModel):
    """State passed through the LangGraph pipeline."""

    prompt: str
    generation: str | None = None
    verification: str | None = None
    critique: str | None = None
    refinement: str | None = None
    final_output: str | None = None

    def copy_with(self, **updates: str | None) -> "LoopState":
        data = self.dict()
        data.update(updates)
        return LoopState(**data)


def generation_node(state: LoopState) -> LoopState:
    """Produce an initial answer by echoing and summarizing the prompt."""

    summary = state.prompt.strip()
    generation = f"Answering: {summary}" if summary else "No prompt provided."
    return state.copy_with(generation=generation)


def verification_node(state: LoopState) -> LoopState:
    """Verify that the generation addresses the prompt and flag gaps."""

    if not state.generation:
        return state.copy_with(verification="Generation missing; cannot verify.")

    prompt_keywords = {token.lower() for token in state.prompt.split() if len(token) > 3}
    response_tokens = {token.lower() for token in state.generation.split() if len(token) > 3}
    missing = prompt_keywords.difference(response_tokens)

    if not missing:
        verification = "Response covers prompt keywords."
    else:
        missing_part = ", ".join(sorted(missing))
        verification = f"Missing coverage for: {missing_part}"

    return state.copy_with(verification=verification)


def critique_node(state: LoopState) -> LoopState:
    """Critique the verification outcome to identify weaknesses."""

    if not state.verification:
        return state.copy_with(critique="Verification was not run.")

    if "Missing coverage" in state.verification:
        critique = "Gaps detected; add detail for uncovered keywords."
    else:
        critique = "No major issues detected; tighten concision if possible."

    return state.copy_with(critique=critique)


def refinement_node(state: LoopState) -> LoopState:
    """Refine the generation using critique feedback."""

    if not state.generation:
        return state.copy_with(refinement="Cannot refine without an initial generation.")

    critique_note = state.critique or ""
    refinement = f"{state.generation} | Refinement: {critique_note}".strip()
    return state.copy_with(refinement=refinement)


@dataclass
class Node:
    name: str
    handler: Callable[[LoopState], LoopState]

    def run(self, state: LoopState) -> LoopState:
        return self.handler(state)


__all__ = [
    "LoopState",
    "Node",
    "generation_node",
    "verification_node",
    "critique_node",
    "refinement_node",
]
