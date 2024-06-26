"""Adicionando campo idade na tabela pessoa 2

Revision ID: d8ef4bed783a
Revises: 0f9273c29cb8
Create Date: 2024-06-24 23:40:25.785715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8ef4bed783a'
down_revision: Union[str, None] = '0f9273c29cb8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pessoa2', sa.Column('idade', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pessoa2', 'idade')
    # ### end Alembic commands ###
