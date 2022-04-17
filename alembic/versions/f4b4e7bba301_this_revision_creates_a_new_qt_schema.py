"""this revision creates a new qt schema

Revision ID: f4b4e7bba301
Revises: 9c75b9ca70a8
Create Date: 2022-04-16 18:22:29.814653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4b4e7bba301'
down_revision = '9c75b9ca70a8'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE SCHEMA IF NOT EXISTS qt;")


def downgrade():
    op.execute("DROP SCHEMA IF EXISTS qt CASCADE;")
