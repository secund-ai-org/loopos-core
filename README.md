# loopos-core

Middleware for measuring and mitigating LLM hallucinations using iterative verification loops. Implements TOFU, RBB, and ECE metrics for EU AI Act compliance.

## Architecture
- **L2 (Default)**: Generation → Verification → Final Output (optimized for speed and cost).
- **L3 (Deep)**: Generation → Verification → Critique → Refinement → Final Output (optimized for precision).

## Components
- `src/metrics/`: Evaluation utilities
  - `tofu.py`: Semantic density (fluff-to-entity ratio)
  - `rbb.py`: Reality-Believability Balance
  - `ece.py`: Expected Calibration Error
- `src/flow/`: LangGraph-style orchestration
  - `nodes.py`: Implements generation, verification, critique, and refinement nodes
  - `graph.py`: Configurable runner that toggles between L2 and L3
- `src/config.py`: Pydantic settings for loop depth and mode

## Quickstart
```bash
python -m compileall src
```

## Usage Example
```python
from src.flow.graph import GraphConfig, LoopGraph

config = GraphConfig(deep_mode=True, loop_depth=4)
graph = LoopGraph(config)
result = graph.run("Summarize the EU AI Act obligations for high-risk systems.")
print(result.final_output)
```
