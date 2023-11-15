"""DB Creation

Revision ID: 58d359747156
Revises: 
Create Date: 2023-11-15 18:26:22.514120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '58d359747156'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('linux_host',
    sa.Column('linux_host_id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('ip_address', postgresql.INET(), nullable=False),
    sa.Column('port', sa.Integer(), nullable=False),
    sa.Column('distributor_id', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('release', sa.String(), nullable=True),
    sa.Column('codename', sa.String(), nullable=True),
    sa.Column('kernel_name', sa.String(), nullable=True),
    sa.Column('nodename', sa.String(), nullable=True),
    sa.Column('kernel_release', sa.String(), nullable=True),
    sa.Column('kernel_version', sa.String(), nullable=True),
    sa.Column('architecture', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('linux_host_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('linux_host')
    # ### end Alembic commands ###