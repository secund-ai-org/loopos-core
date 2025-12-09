import pytest
from src.flow.graph import LoopGraph, GraphConfig

def test_loop_graph_l2_mode_excludes_refinement():
    # L2 mode (Default) should stop after verification
    graph = LoopGraph(config=GraphConfig(deep_mode=False, loop_depth=2))
    state = graph.run("List mitigation steps for AI safety.")
    
    assert state.verification is not None
    assert state.refinement is None

def test_loop_graph_l3_mode_includes_refinement():
    # JAVÍTVA: loop_depth=4 (hogy elérje a Refinement lépést)
    graph = LoopGraph(config=GraphConfig(deep_mode=True, loop_depth=4))
    
    state = graph.run("List mitigation steps for AI safety.")
    
    assert state.critique is not None
    assert state.refinement is not None
    # Verify that final output is indeed the refined version
    assert state.final_output == state.refinement
