# SECUND LoopOS: Cognitive Reality Calibration Layer (CRCL)

[![CI Status](https://github.com/secund-ai-org/loopos-core/actions/workflows/ci.yml/badge.svg)](https://github.com/secund-ai-org/loopos-core/actions)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Status](https://img.shields.io/badge/Status-v0.1.0_Alpha-orange)]()
[![Compliance](https://img.shields.io/badge/EU_AI_Act-Ready-emerald)]()

**LoopOS** is an open-core middleware designed to measure and mitigate hallucinations in Large Language Models (LLMs). It forces standard generative models to pass through a verified state-machine protocol, transforming raw text into a structured, audit-ready **SECUND Output Block**.

> *"We don't just generate tokens; we engineer trust."*

---

## 💎 The SECUND Output Protocol

Unlike standard chatbots that output a stream of text, LoopOS produces a structured 4-quadrant response. This ensures that every answer is audited before it reaches the user.

| Block | Function | Underlying Metric |
| :--- | :--- | :--- |
| **1. [REALITY]** | **Fact Anchoring.** Verifies that claims are backed by source data. Filters out confident hallucinations. | **RBB** (Reality-Believability Balance) |
| **2. [CLARITY]** | **Signal-to-Noise.** Removes "fluff", hedging, and corporate filler to maximize information density. | **TOFU** (Totally Futile content Index) |
| **3. [MECHANICS]** | **Logic Trace.** Exposes the reasoning path (L0→L3) used to reach the conclusion. | **Graph State** (LangGraph) |
| **4. [CONTROL]** | **Safety & Compliance.** Checks against guardrails (e.g., EU AI Act Art. 13) and risk thresholds. | **ECE** (Expected Calibration Error) |

---

## 🧠 Core Architecture: The Loop

The system operates as a "Glass Box" (transparent state machine). It iterates through cognitive levels to reduce entropy.

| Level | Name | Description | Status |
| :--- | :--- | :--- | :--- |
| **L0** | **Raw Generation** | Standard single-shot inference. High speed, low reliability. | *Input Signal* |
| **L1** | **Critique** | Internal self-reflection. The model critiques its own logic gaps. | *Internal Check* |
| **L2** | **Verification** | **(Default Mode)** External validation against the prompt constraints. | **Production Standard** |
| **L3** | **Refinement** | **(Deep Mode)** Synthesis of the previous steps into the 4-Block SECUND Output. | **High-Precision** |

---

## 🎛️ Mission Control (Frontend)

This repository includes a full **Next.js Dashboard** to visualize the AI's thinking process in real-time.

[attachment_0](attachment)

* **Tech Stack:** Next.js 14 (App Router), Tailwind CSS, Framer Motion.
* **Visuals:** Glassmorphic "Deep Engineering" UI (Zinc-950 / Emerald-500).
* **Features:**
    * **Live Loop Visualizer:** Watch the transition from L0 to L3.
    * **Metric Gauges:** Real-time visualization of TOFU and RBB scores.
    * **Terminal Interface:** Command-line style interaction.

---

## 📂 Project Structure

```text
loopos-core/
├── src/               # 🐍 PYTHON BACKEND (The Engine)
│   ├── flow/          # Logic for L0-L3 Nodes
│   ├── metrics/       # Algorithms (TOFU, RBB, ECE)
│   └── config.py      # Configuration settings
├── frontend/          # ⚛️ NEXT.JS FRONTEND (The UI)
│   ├── app/           # React components & pages
│   └── components/    # Visualizers & Cards
└── tests/             # ✅ VALIDATION (Pytest suites)

🚀 Quickstart
1. Run the Backend (Python Engine)
Prerequisites: Python 3.11+
# Install the core package
pip install .

# Run the internal test suite to verify metrics
pytest

2. Run the Dashboard (Mission Control)
Prerequisites: Node.js 18+
cd frontend
npm install
npm run dev
# Open http://localhost:3000 to see the Mission Control

3. Python SDK Usage Example
from src.flow.graph import GraphConfig, LoopGraph

# Initialize in DEEP MODE (Required for 4-Block Output)
config = GraphConfig(deep_mode=True, loop_depth=4)
graph = LoopGraph(config)

# Run the verification loop
result = graph.run("Summarize the obligations of the EU AI Act.")

# Access the structured refinement
print(result.refinement)
# Output:
# 1. [REALITY] ...
# 2. [CLARITY] ...
# 3. [MECHANICS] ...
# 4. [CONTROL] ...

📜 Scientific Basis
This system addresses the Hirano Effect (Cognitive Inflation in LLMs) by applying recursive entropy reduction loops. It aligns with the OSF (Open Science Framework) standards for transparent AI research.
⚖️ License
This project is licensed under the Apache 2.0 License - see the LICENSE file for details.
