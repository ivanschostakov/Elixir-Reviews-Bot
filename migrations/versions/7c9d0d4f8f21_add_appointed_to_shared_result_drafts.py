"""add appointed to shared result drafts

Revision ID: 7c9d0d4f8f21
Revises: 5b4f8ee39605
Create Date: 2026-02-08 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7c9d0d4f8f21"
down_revision: Union[str, Sequence[str], None] = "5b4f8ee39605"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("shared_result_drafts", sa.Column("appointed", sa.String(), nullable=True))
    op.create_check_constraint(
        "ck_shared_result_drafts_appointed",
        "shared_result_drafts",
        "appointed IS NULL OR appointed in ('врач','сам(а) себе','ботом')",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("ck_shared_result_drafts_appointed", "shared_result_drafts", type_="check")
    op.drop_column("shared_result_drafts", "appointed")
