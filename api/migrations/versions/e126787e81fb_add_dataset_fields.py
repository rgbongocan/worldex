"""Add dataset fields

Revision ID: e126787e81fb
Revises: d93f2a583709
Create Date: 2023-09-22 10:21:23.518788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import geoalchemy2

# revision identifiers, used by Alembic.
revision: str = "e126787e81fb"
down_revision: Union[str, None] = "d93f2a583709"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("datasets", sa.Column("source_org", sa.String(), nullable=True))
    op.add_column(
        "datasets",
        sa.Column(
            "last_fetched",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.add_column(
        "datasets", sa.Column("files", postgresql.ARRAY(sa.String()), nullable=True)
    )
    op.add_column("datasets", sa.Column("description", sa.String(), nullable=True))
    op.add_column("datasets", sa.Column("data_format", sa.String(), nullable=False))
    op.add_column("datasets", sa.Column("projection", sa.String(), nullable=False))
    op.add_column(
        "datasets",
        sa.Column("properties", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    )
    op.add_column(
        "datasets",
        sa.Column(
            "bbox",
            geoalchemy2.types.Geometry(
                from_text="ST_GeomFromEWKT", name="geometry", nullable=True
            ),
            nullable=False,
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("datasets", "bbox")
    op.drop_column("datasets", "properties")
    op.drop_column("datasets", "projection")
    op.drop_column("datasets", "data_format")
    op.drop_column("datasets", "description")
    op.drop_column("datasets", "files")
    op.drop_column("datasets", "last_fetched")
    op.drop_column("datasets", "source_org")
    # ### end Alembic commands ###
