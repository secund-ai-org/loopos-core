from src.flow.graph import GraphConfig, LoopGraph


def test_loop_graph_l2_mode_skips_refinement():
    graph = LoopGraph(config=GraphConfig(deep_mode=False))

    state = graph.run("Summarize the findings.")

    assert state.refinement is None


def test_loop_graph_l3_mode_includes_refinement():
    graph = LoopGraph(config=GraphConfig(deep_mode=True, loop_depth=3))

    state = graph.run("List mitigation steps for AI safety.")

    assert state.refinement is not None
