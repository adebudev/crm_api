"""create IV schema

Revision ID: 9ec64b014395
Revises: f6c109465a0c
Create Date: 2022-04-23 17:32:49.065073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ec64b014395'
down_revision = 'f6c109465a0c'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE SCHEMA IF NOT EXISTS iv;")


def downgrade():
    op.execute("DROP SCHEMA IF EXISTS iv CASCADE;")
