# Contributing Guide

Thanks for your interest in improving **Daily 100 Content Method**. Contributions of all sizes are welcome — this project thrives on real-world adaptations.

## How to Contribute

### 1. New industry adaptations (highest value)

The method is designed to be adapted per industry. If you've applied it to a specific vertical, share the result:

```
examples/{your-industry}/
├── plan.md          # The full adapted plan
└── scripts.json     # Pre-written scripts (machine-readable, see schema below)
```

Please follow the structure of [`examples/decoration-company/`](examples/decoration-company/plan.md) as a reference.

### 2. Prompt improvements

Found a prompt in [`prompts/`](prompts/) that gives weak results? Improve it and submit a PR. Keep prompts:

- Copy-paste ready (no placeholders the LLM can't infer)
- Language-agnostic where possible (works with any LLM)
- Framed around **roles** (boss / employee / creator), not just topics

### 3. Code contributions

`src/generate_script.py` is intentionally small. Ideas that add real value:

- Support for more `--type` values (story-hook, methodology, etc.)
- Batch generation from a JSON list of topics
- Output to JSON/Markdown/HTML
- A lightweight web UI (if you want to build one)

Keep the CLI dependency-free (stdlib only) so it runs anywhere.

### 4. Documentation & translation

README translations are welcome. Mark the language in the filename, e.g. `README.ja-JP.md`.

## Contribution Workflow

1. Fork the repo and create a branch: `git checkout -b feature/your-feature`
2. Make your changes with clear commit messages
3. Test what can be tested (`python src/generate_script.py --help`)
4. Open a pull request describing what you changed and why

## Code Style

- Python: PEP 8, type hints optional but appreciated
- No external dependencies unless absolutely necessary
- Keep files focused — one concern per file

## Code of Conduct

Be respectful. This project is used by real businesses and creators; assume good intent, give constructive feedback, and never disparage an adaptation because it doesn't fit your industry.
