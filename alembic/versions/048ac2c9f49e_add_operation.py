"""Add Operation

Revision ID: 048ac2c9f49e
Revises: 74c3030c0b1d
Create Date: 2023-06-08 00:33:12.191822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '048ac2c9f49e'
down_revision = '74c3030c0b1d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Название', sa.String(), nullable=True),
    sa.Column('Дата_начала', sa.Date(), nullable=True),
    sa.Column('Дата_сдачи', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_operation_id'), 'operation', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_operation_id'), table_name='operation')
    op.drop_table('operation')
    # ### end Alembic commands ###
