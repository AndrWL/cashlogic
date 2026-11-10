# Cashlogic

AI-first personal finance tracker built on top of open banking APIs.

> Work in progress — learning project on the path from iOS to AI engineering.

## Planned features
- Auto-categorization of transactions (MCC + description) that learns from corrections
- "Ask your money" — an agent with a SQL tool
- Budget coach, subscriptions & anomaly detection
- SwiftUI client

## Stack
Python 3.14 · uv workspace · httpx · pydantic · pytest

## Run

cp .env.example .env # add your bank API token
uv sync
uv run python -m api.mono.client
uv run pytest apps/api/tests


## Privacy
Real bank data never leaves your machine: `.env` and `data/` are git-ignored,
tests use synthetic fixtures only.
