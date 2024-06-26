"""Rm unused indices

Revision ID: 048fd4a97938
Revises: 1fab309748e6
Create Date: 2023-11-30 17:45:59.864276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '048fd4a97938'
down_revision: Union[str, None] = '1fab309748e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_h3_data_h3_index_as_point', table_name='h3_data', postgresql_using='gist')
    op.drop_index('ix_h3_data_res1_parent_dataset_id', table_name='h3_data', postgresql_where='(h3_get_resolution(h3_index) > 1)')
    op.drop_index('ix_h3_data_res2_parent_dataset_id', table_name='h3_data', postgresql_where='(h3_get_resolution(h3_index) > 2)')
    op.drop_index('ix_h3_data_res3_parent_dataset_id', table_name='h3_data', postgresql_where='(h3_get_resolution(h3_index) > 3)')
    op.drop_index('ix_h3_data_res4_parent_dataset_id', table_name='h3_data', postgresql_where='(h3_get_resolution(h3_index) > 4)')
    op.drop_index('ix_h3_data_res5_parent_dataset_id', table_name='h3_data', postgresql_where='(h3_get_resolution(h3_index) > 5)')
    op.drop_index('ix_h3_data_res6_parent_dataset_id', table_name='h3_data', postgresql_where='(h3_get_resolution(h3_index) > 6)')
    op.drop_index('ix_h3_data_res7_parent_dataset_id', table_name='h3_data', postgresql_where='(h3_get_resolution(h3_index) > 7)')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_h3_data_res7_parent_dataset_id', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 7)'), 'dataset_id'], unique=False, postgresql_where='(h3_get_resolution(h3_index) > 7)')
    op.create_index('ix_h3_data_res6_parent_dataset_id', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 6)'), 'dataset_id'], unique=False, postgresql_where='(h3_get_resolution(h3_index) > 6)')
    op.create_index('ix_h3_data_res5_parent_dataset_id', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 5)'), 'dataset_id'], unique=False, postgresql_where='(h3_get_resolution(h3_index) > 5)')
    op.create_index('ix_h3_data_res4_parent_dataset_id', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 4)'), 'dataset_id'], unique=False, postgresql_where='(h3_get_resolution(h3_index) > 4)')
    op.create_index('ix_h3_data_res3_parent_dataset_id', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 3)'), 'dataset_id'], unique=False, postgresql_where='(h3_get_resolution(h3_index) > 3)')
    op.create_index('ix_h3_data_res2_parent_dataset_id', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 2)'), 'dataset_id'], unique=False, postgresql_where='(h3_get_resolution(h3_index) > 2)')
    op.create_index('ix_h3_data_res1_parent_dataset_id', 'h3_data', [sa.text('h3_cell_to_parent(h3_index, 1)'), 'dataset_id'], unique=False, postgresql_where='(h3_get_resolution(h3_index) > 1)')
    op.create_index('ix_h3_data_h3_index_as_point', 'h3_data', [sa.text('h3_cell_to_geometry(h3_index)')], unique=False, postgresql_using='gist')
    # ### end Alembic commands ###
