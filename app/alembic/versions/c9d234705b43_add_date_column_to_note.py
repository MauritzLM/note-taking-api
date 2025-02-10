"""add date column to note

Revision ID: c9d234705b43
Revises: c9ba1d897cf8
Create Date: 2025-02-10 09:58:59.609834

"""
from typing import Sequence, Union
import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9d234705b43'
down_revision: Union[str, None] = 'c9ba1d897cf8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('notes', sa.Column('date', sa.DateTime, default=datetime.datetime.now(), autoincrement=False, nullable=True))


def downgrade() -> None:
    op.drop_column('notes', 'date')
