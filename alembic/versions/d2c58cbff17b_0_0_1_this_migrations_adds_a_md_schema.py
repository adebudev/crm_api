"""0.0.1 - This migrations adds a md schema.

Revision ID: d2c58cbff17b
Revises:
Create Date: 2022-03-27 00:04:46.813507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d2c58cbff17b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute("CREATE SCHEMA IF NOT EXISTS md;")


def downgrade():
    op.execute("DROP SCHEMA IF EXISTS md CASCADE;")
