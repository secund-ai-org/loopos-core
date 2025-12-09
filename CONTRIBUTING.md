# Contributing to loopos-core

Thank you for your interest in improving `loopos-core`! We welcome contributions that make the system more reliable, transparent, and scientifically grounded. This guide summarizes our expectations and provides practical steps to get your changes merged quickly.

## Philosophy: Glass Box Development
We practice **Glass Box** development: code, design decisions, and evaluation methods are open and inspectable. Please:
- Prefer clear implementations and comments over hidden magic.
- Link decisions to evidence (benchmarks, papers, or experiments).
- Keep discussion and review conversations public whenever possible.

Our work aligns with **OSF Research** standards to ensure scientific validity of metrics such as TOFU and RBB. When you change measurement logic or evaluation flows, include rationale and references to supporting research.

## Getting Started
1. Fork the repository and clone your fork.
2. Create a feature branch for your changes.
3. Ensure you have Python 3.11 available.

## Development Environment
Install dependencies (including dev tools):

```bash
pip install .[dev]
```

### Running Tests
Execute the full test suite with:

```bash
pytest
```

Please add or update tests alongside code changes to maintain coverage, especially for core metrics and flow logic.

## Pull Request Process
- Write clear, descriptive titles and summaries. Include motivation and references to OSF-aligned research when relevant.
- Ensure all tests pass locally and in CI.
- Keep commits focused; rebase on the latest `main` before submitting.
- Fill out the pull request template and describe any user-facing changes or new behaviors.
- Be responsive to review feedback and maintain the Glass Box ethos—if a reviewer asks "why", answer with evidence.

## Code Style and Quality
- Follow the existing project patterns and keep functions small and purposeful.
- Use automated formatting tools (`black`, `isort`) when appropriate.
- Document public APIs and add in-line comments where they clarify intent.

## Reporting Issues
If you find a bug or have a feature idea, please open an issue with:
- A concise description of the problem or proposal.
- Reproduction steps or example scenarios.
- Why the change matters for transparency, reliability, or OSF-aligned research goals.

We appreciate your contributions and commitment to building robust, transparent, and scientifically valid software.
