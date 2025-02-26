"""update password column

Revision ID: 4f258bec63ab
Revises: c9d234705b43
Create Date: 2025-02-26 10:58:55.771619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f258bec63ab'
down_revision: Union[str, None] = 'c9d234705b43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(table_name='user_account', column_name='password', type_=sa.String(255), nullable=False)


def downgrade() -> None:
    op.alter_column(table_name='user_account', column_name='password', type_=sa.String(255), nullable=False)
