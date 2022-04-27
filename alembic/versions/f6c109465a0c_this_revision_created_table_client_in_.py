"""This revision created table client in md schema

Revision ID: f6c109465a0c
Revises: aa82846178f0
Create Date: 2022-04-18 04:31:52.497902

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'f6c109465a0c'
down_revision = 'aa82846178f0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'client',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address', sa.String, nullable=False),
        sa.Column("city", sa.String(), nullable=True),
        sa.Column("country", sa.String(), nullable=False),
        sa.Column("contact_name", sa.String(), nullable=True),
        sa.Column("contact_phone", sa.String(), nullable=True),
        sa.Column("contact_email", sa.String(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False, default=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("goverment_id", sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('modified_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('goverment_id'),
        sa.UniqueConstraint('contact_email'),
        sa.ForeignKeyConstraint(['user_id'], ['md.user.id'], name='user_id_fkey', ondelete='CASCADE'),
        schema='md'
    )


def downgrade():
    op.drop_table('client', schema='md')
