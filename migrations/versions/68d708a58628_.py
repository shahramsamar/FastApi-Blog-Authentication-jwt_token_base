"""empty message

Revision ID: 68d708a58628
Revises: 
Create Date: 2024-10-18 21:52:48.697737

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '68d708a58628'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('expiration_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tokens_token'), 'tokens', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tokens_token'), table_name='tokens')
    op.drop_table('tokens')
    op.drop_table('users')
    op.drop_table('students')
    # ### end Alembic commands ###