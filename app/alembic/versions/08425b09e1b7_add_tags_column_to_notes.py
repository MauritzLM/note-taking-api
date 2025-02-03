"""add tags column to notes

Revision ID: 08425b09e1b7
Revises: ac11a3a25f7f
Create Date: 2025-02-03 10:20:19.975204

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08425b09e1b7'
down_revision: Union[str, None] = 'ac11a3a25f7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('notes', sa.Column('tags', sa.ARRAY(sa.String), autoincrement=False, nullable=True))


def downgrade() -> None:
    op.drop_column('notes', sa.Column('tags'))
