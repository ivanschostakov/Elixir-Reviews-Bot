# Elixir Reviews Bot

Telegram workflow for collecting, editing, and publishing structured customer experience reports with optional photos and product references.

## Highlights

- Guided review drafts stored in PostgreSQL.
- Optional anonymous publication.
- Up to three before/after photos per draft.
- Product search and structured result fields.
- Admin moderation, user blocking, and direct support messages.
- amoCRM integration and Alembic-managed database migrations.

## Project Structure

- `src/bot/`: user and admin handlers, keyboards, state machines, and text.
- `src/database/`: users, review drafts, schemas, and persistence.
- `migrations/`: database schema history.

## Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
python run.py
```

## Privacy and Security

- Review photos and user-submitted information are runtime data and must remain outside Git.
- Do not commit Telegram identifiers, CRM credentials, database exports, or logs.
- Use synthetic records for public demonstrations.
