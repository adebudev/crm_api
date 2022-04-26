"""This revision adds a quote table to qt schema

Revision ID: 6c4a073a3403
Revises: f4b4e7bba301
Create Date: 2022-04-16 19:05:31.595383

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '6c4a073a3403'
down_revision = 'f4b4e7bba301'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'quotes',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('quote_num', sa.Integer(), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('client_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("quote_status", sa.Boolean(), nullable=False, default=True),
        sa.Column("exp_date", sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('modified_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='qt'
    )


def downgrade():
    op.drop_table('quotes', schema='qt')
