# Project Plan

## Goal

Build a reproducible analysis pipeline for studying decision stability in AlphaGo-style Go search.

## Engine

Use KataGo locally. The engine and model files are external dependencies and are not stored in this repository.

## Key variables

- Position
- Search budget, primarily `maxVisits`
- Top recommended move
- Visit count distribution
- Policy prior
- Winrate
- Score lead
- Top-k move set

## Initial budgets

Use:

- 1
- 4
- 8
- 16
- 32
- 64
- 128
- 256
- 512
- 1000

## Initial metrics

For each position and budget:

1. Top move
2. Top-move agreement with high-budget reference
3. Top-k overlap with high-budget reference
4. Visit distribution entropy
5. Winrate difference from reference
6. Score lead difference from reference
7. Whether search overturns the raw policy prior

## Design principle

Keep scripts small, testable, and composable. Avoid one large script that does everything.