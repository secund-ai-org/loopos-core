from src.flow.graph import GraphConfig, LoopGraph


def test_loop_graph_l2_stops_after_verification():
    graph = LoopGraph(GraphConfig(deep_mode=False, loop_depth=2))

    state = graph.run("Summarize the findings.")

    assert state.refinement is None
    assert state.final_output == state.verification or state.final_output == state.generation


def test_loop_graph_l3_runs_refinement():
    graph = LoopGraph(GraphConfig(deep_mode=True, loop_depth=4))

    state = graph.run("List mitigation steps for AI safety.")

    assert state.refinement is not None
    assert state.final_output == state.refinement
