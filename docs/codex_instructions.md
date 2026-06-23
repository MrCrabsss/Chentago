# Codex Instructions

This repository is a research-code project for analyzing KataGo decision stability.

Rules:

1. Do not add KataGo binaries, model files, or large raw outputs to Git.
2. Do not assume absolute paths. Read local paths from `local_config.yaml`.
3. Keep scripts modular and simple.
4. Prefer readable Python over clever abstractions.
5. Add clear command-line interfaces using `argparse`.
6. Write outputs to `data_processed/` or `figures/`.
7. Use `pathlib` for paths.
8. Use `yaml.safe_load` for config.
9. Avoid changing files outside this repository.
10. When writing scripts, include a short usage example at the top or in the help text.

The project uses Windows PowerShell as the main shell environment.