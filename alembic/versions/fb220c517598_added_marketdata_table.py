"""Added MarketData table

Revision ID: fb220c517598
Revises: f5c3b4b050af
Create Date: 2025-03-05 10:42:29.398076

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb220c517598'
down_revision: Union[str, None] = 'f5c3b4b050af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('market_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token_address', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_market_data_id'), 'market_data', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_market_data_id'), table_name='market_data')
    op.drop_table('market_data')
    # ### end Alembic commands ###
