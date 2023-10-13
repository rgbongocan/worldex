"""Create h3 data indices

Revision ID: a906141b23f0
Revises: be3aa22ec420
Create Date: 2023-09-14 11:07:16.369064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a906141b23f0"
down_revision: Union[str, None] = "be3aa22ec420"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        "ix_h3_data_h3_index_as_point",
        "h3_data",
        [sa.text("h3_cell_to_geometry(h3_index)")],
        unique=False,
        postgresql_using="gist",
    )
    op.create_index('ix_h3_data_h3_index_parent_res1', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 1)')], unique=False, postgresql_where=sa.text('h3_get_resolution(h3_index) > 1'))
    op.create_index('ix_h3_data_h3_index_parent_res2', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 2)')], unique=False, postgresql_where=sa.text('h3_get_resolution(h3_index) > 2'))
    op.create_index('ix_h3_data_h3_index_parent_res3', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 3)')], unique=False, postgresql_where=sa.text('h3_get_resolution(h3_index) > 3'))
    op.create_index('ix_h3_data_h3_index_parent_res4', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 4)')], unique=False, postgresql_where=sa.text('h3_get_resolution(h3_index) > 4'))
    op.create_index('ix_h3_data_h3_index_parent_res5', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 5)')], unique=False, postgresql_where=sa.text('h3_get_resolution(h3_index) > 5'))
    op.create_index('ix_h3_data_h3_index_parent_res6', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 6)')], unique=False, postgresql_where=sa.text('h3_get_resolution(h3_index) > 6'))
    op.create_index('ix_h3_data_h3_index_parent_res7', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 7)')], unique=False, postgresql_where=sa.text('h3_get_resolution(h3_index) > 7'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_h3_data_h3_index_parent_res7', table_name='h3_data')
    op.drop_index('ix_h3_data_h3_index_parent_res6', table_name='h3_data')
    op.drop_index('ix_h3_data_h3_index_parent_res5', table_name='h3_data')
    op.drop_index('ix_h3_data_h3_index_parent_res4', table_name='h3_data')
    op.drop_index('ix_h3_data_h3_index_parent_res3', table_name='h3_data')
    op.drop_index('ix_h3_data_h3_index_parent_res2', table_name='h3_data')
    op.drop_index('ix_h3_data_h3_index_parent_res1', table_name='h3_data')
    op.drop_index(
        "ix_h3_data_h3_index_as_point", table_name="h3_data"
    )
    # ### end Alembic commands ###