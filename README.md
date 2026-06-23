# Chentago: Damaging the AlphaGo-Style Go engine to match my personal level of Go playing

This project studies how neural policy priors and MCTS search budget affect move recommendation stability in AlphaGo-Style Go engines. The motivation was to reduce the model's ability to match my personal level, 5 dan, and then use it against my friends.

The project uses KataGo as an experimental platform. It does not train a Go engine from scratch. Instead, it runs controlled analysis on fixed Go positions while varying search budget, then measures how recommendations, visit distributions, winrate estimates, score estimates, and policy/search agreement change.

Core research question:

How does increasing MCTS budget transform a neural policy prior into a stable final decision?

KataGo executable, model files, and local paths are not tracked in Git. They are configured locally through `local_config.yaml`.