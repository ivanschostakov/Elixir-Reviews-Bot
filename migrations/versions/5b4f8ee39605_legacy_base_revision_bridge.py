"""legacy base revision bridge

Revision ID: 5b4f8ee39605
Revises: None
Create Date: 2026-02-08 00:00:01.000000

"""
from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = "5b4f8ee39605"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
