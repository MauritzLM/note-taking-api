"""updated uuid columns

Revision ID: fe84ad3faf7d
Revises: 
Create Date: 2025-01-31 15:26:35.338263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe84ad3faf7d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_notes_id', table_name='notes')
    op.drop_index('ix_notes_title', table_name='notes')
    op.drop_table('notes')
    op.drop_index('ix_user_account_id', table_name='user_account')
    op.drop_index('ix_user_account_username', table_name='user_account')
    op.drop_table('user_account')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_account',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=30), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_account_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_user_account_username', 'user_account', ['username'], unique=False)
    op.create_index('ix_user_account_id', 'user_account', ['id'], unique=False)
    op.create_table('notes',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('isArchived', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('author', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user_account.id'], name='notes_author_fkey'),
    sa.PrimaryKeyConstraint('id', name='notes_pkey')
    )
    op.create_index('ix_notes_title', 'notes', ['title'], unique=False)
    op.create_index('ix_notes_id', 'notes', ['id'], unique=False)
    # ### end Alembic commands ###
