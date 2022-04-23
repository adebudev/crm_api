"""this revision add  items, details, comments and taxes to qt schema

Revision ID: aa82846178f0
Revises: 6c4a073a3403
Create Date: 2022-04-17 20:17:07.138543

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "aa82846178f0"
down_revision = "6c4a073a3403"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "items",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("quantity", sa.Integer(), nullable=True),
        sa.Column("unit_value", sa.Numeric(precision=14, scale=2), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "modified_on",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("quote_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["quote_id"],
            ["qt.quotes.id"],
            ondelete='CASCADE'
        ),
        schema="qt",
    )

    op.create_table(
        "details",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("valid_time", sa.Integer(), nullable=True),
        sa.Column("deliver_time", sa.DateTime(), nullable=True),
        sa.Column("currency_type", sa.String(), nullable=True),
        sa.Column("payment_terms", sa.String(), nullable=True),
        sa.Column("sub_total", sa.Numeric(precision=14, scale=2), nullable=True),
        sa.Column("total", sa.Numeric(precision=14, scale=2), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "modified_on",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("quote_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["quote_id"],
            ["qt.quotes.id"],
            ondelete='CASCADE'
        ),
        schema="qt",
    )

    op.create_table(
        "comments",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("comment", sa.String(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "modified_on",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("quote_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["quote_id"],
            ["qt.quotes.id"],
            ondelete='CASCADE'
        ),
        schema="qt",
    )

    op.create_table(
        "taxes",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("tax_name", sa.String(), nullable=True),
        sa.Column("tax_value", sa.Numeric(precision=14, scale=2), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "modified_on",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("quote_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["quote_id"],
            ["qt.quotes.id"],
            ondelete='CASCADE'
        ),
        schema="qt",
    )


def downgrade():
    op.drop_table("items", schema="qt")
    op.drop_table("details", schema="qt")
    op.drop_table("comments", schema="qt")
    op.drop_table("taxes", schema="qt")
