"""Initial Migration

Revision ID: e7cf5ab8b9e1
Revises:
Create Date: 2024-08-03 16:41:57.268857

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e7cf5ab8b9e1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "movie",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("image", sa.String(length=200), nullable=True),
        sa.Column("language", sa.String(length=50), nullable=False),
        sa.Column("genre", sa.String(length=50), nullable=False),
        sa.Column("director", sa.String(length=100), nullable=False),
        sa.Column("trailer", sa.String(length=200), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("duration", sa.Integer(), nullable=False),
        sa.Column("start_date", sa.DateTime(), nullable=False),
        sa.Column("end_date", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "theatre",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("city", sa.String(length=100), nullable=False),
        sa.Column("ticket_price", sa.Float(), nullable=False),
        sa.Column("seats", sa.JSON(), nullable=False),
        sa.Column("image", sa.String(length=200), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("password", sa.String(length=120), nullable=False),
        sa.Column("role", sa.Enum("Admin", "Customer", "SuperAdmin"), nullable=False),
        sa.Column("phone", sa.String(length=20), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "reservation",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column("start_at", sa.DateTime(), nullable=False),
        sa.Column("seats", sa.JSON(), nullable=False),
        sa.Column("order_id", sa.String(length=100), nullable=False),
        sa.Column("ticket_price", sa.Float(), nullable=False),
        sa.Column("total", sa.Float(), nullable=False),
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.Column("theatre_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("phone", sa.String(length=20), nullable=False),
        sa.ForeignKeyConstraint(
            ["movie_id"],
            ["movie.id"],
        ),
        sa.ForeignKeyConstraint(
            ["theatre_id"],
            ["theatre.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("order_id"),
    )
    op.create_table(
        "showtime",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("ticket_price", sa.Float(), nullable=False),
        sa.Column("start_date", sa.DateTime(), nullable=False),
        sa.Column("end_date", sa.DateTime(), nullable=False),
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.Column("theatre_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["movie_id"],
            ["movie.id"],
        ),
        sa.ForeignKeyConstraint(
            ["theatre_id"],
            ["theatre.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("showtime")
    op.drop_table("reservation")
    op.drop_table("user")
    op.drop_table("theatre")
    op.drop_table("movie")
    # ### end Alembic commands ###
