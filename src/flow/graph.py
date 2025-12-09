"""LangGraph-like orchestration for looped verification."""
from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field, validator

from .nodes import (
    LoopState,
    Node,
    critique_node,
    generation_node,
    refinement_node,
    verification_node,
)


class GraphConfig(BaseModel):
    """Configuration for controlling loop depth and behavior."""

    deep_mode: bool = Field(
        default=False, description="When True, run critique/refinement for L3 depth."
    )
    loop_depth: int = Field(
        default=2,
        ge=1,
        le=4,
        description="Configured depth of the loop. L2=2 steps, L3=3+ steps.",
    )

    @validator("loop_depth")
    def validate_depth(cls, value: int, values: dict) -> int:
        if values.get("deep_mode") and value < 3:
            raise ValueError("Deep mode requires loop_depth >= 3.")
        return value


class LoopGraph:
    """Stateful runner that simulates a LangGraph workflow."""

    def __init__(self, config: GraphConfig | None = None):
        self.config = config or GraphConfig()
        self.l2_nodes: List[Node] = [
            Node(name="generation", handler=generation_node),
            Node(name="verification", handler=verification_node),
        ]
        self.l3_nodes: List[Node] = self.l2_nodes + [
            Node(name="critique", handler=critique_node),
            Node(name="refinement", handler=refinement_node),
        ]

    def run(self, prompt: str) -> LoopState:
        state = LoopState(prompt=prompt)
        nodes = self._select_nodes()
        for node in nodes:
            state = node.run(state)
        if self.config.deep_mode:
            state = state.copy_with(final_output=state.refinement)
        else:
            state = state.copy_with(final_output=state.verification or state.generation)
        return state

    def _select_nodes(self) -> List[Node]:
        if self.config.deep_mode:
            return self.l3_nodes[: self.config.loop_depth]
        return self.l2_nodes[: self.config.loop_depth]


__all__ = ["GraphConfig", "LoopGraph"]
