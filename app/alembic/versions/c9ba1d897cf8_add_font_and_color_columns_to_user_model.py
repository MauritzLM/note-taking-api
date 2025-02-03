"""add font and color columns to user model

Revision ID: c9ba1d897cf8
Revises: 08425b09e1b7
Create Date: 2025-02-03 11:24:54.667591

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9ba1d897cf8'
down_revision: Union[str, None] = '08425b09e1b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user_account', sa.Column('color_theme', sa.String, default='light', autoincrement=False, nullable=True))
    op.add_column('user_account', sa.Column('font_theme', sa.String, default='serif', autoincrement=False, nullable=True))


def downgrade() -> None:
    op.drop_column('user_account', sa.Column('color_theme'))
    op.drop_column('user_account', sa.Column('font_theme'))
