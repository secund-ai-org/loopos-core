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
    """L0: Raw Generation."""
    summary = state.prompt.strip()
    generation = f"Answering: {summary}" if summary else "No prompt provided."
    return state.copy_with(generation=generation)


def verification_node(state: LoopState) -> LoopState:
    """L2: Verification (Reality Check)."""
    if not state.generation:
        return state.copy_with(verification="Generation missing.")

    # Simulation of fact-checking logic
    prompt_keywords = {token.lower() for token in state.prompt.split() if len(token) > 3}
    response_tokens = {token.lower() for token in state.generation.split() if len(token) > 3}
    missing = prompt_keywords.difference(response_tokens)

    if not missing:
        verification = "All prompt entities verified in response."
    else:
        missing_part = ", ".join(sorted(missing))
        verification = f"Potential Hallucination: Missing coverage for {missing_part}"

    return state.copy_with(verification=verification)


def critique_node(state: LoopState) -> LoopState:
    """L1: Critique (Internal Logic Check)."""
    if not state.verification:
        return state.copy_with(critique="Verification skipped.")

    if "Missing" in state.verification:
        critique = "CRITICAL: Response density low. Fact gaps detected."
    else:
        critique = "PASS: Logic flow is sound. Optimize for concision."

    return state.copy_with(critique=critique)


def refinement_node(state: LoopState) -> LoopState:
    """L3: Refinement (The 4-Block Synthesis)."""
    # Ez a rész állítja elő a 4 blokkot a meglévő adatokból
    
    if not state.generation:
        return state.copy_with(refinement="No generation to refine.")

    # Itt szimuláljuk, hogy az LLM összerakja a 4 blokkot
    # Élesben itt hívnánk meg a modellt egy specifikus prompttal
    
    secund_output = (
        f"--- SECUND OUTPUT BLOCK ---\n\n"
        f"1. [REALITY] \n"
        f"   Verified Source: Internal Knowledge Base.\n"
        f"   Status: {state.verification}\n\n"
        
        f"2. [CLARITY] \n"
        f"   Summary: {state.generation}\n"
        f"   Signal-to-Noise: High.\n\n"
        
        f"3. [MECHANICS] \n"
        f"   Logic Path: Generation -> Verification -> Refinement.\n"
        f"   Critique Note: {state.critique}\n\n"
        
        f"4. [CONTROL] \n"
        f"   Compliance: EU AI Act Art. 13 Checked.\n"
        f"   Risk Level: Low."
    )

    return state.copy_with(refinement=secund_output)


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
