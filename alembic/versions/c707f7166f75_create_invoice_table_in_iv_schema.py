"""create invoice table in iv schema

Revision ID: c707f7166f75
Revises: 9ec64b014395
Create Date: 2022-04-23 17:33:44.311338

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'c707f7166f75'
down_revision = '9ec64b014395'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('invoices',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('invoice_num', sa.Integer(), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('client_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('detail', sa.String, nullable=False),
        sa.Column('total', sa.Numeric(precision=14, scale=2), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('modified_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema='iv'
    )


def downgrade():
    op.drop_table('invoices', schema='iv')
