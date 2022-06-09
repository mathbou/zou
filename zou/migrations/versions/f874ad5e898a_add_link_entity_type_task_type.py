"""Add link entity type -> task type

Revision ID: f874ad5e898a
Revises: 5ab9d7a75887
Create Date: 2022-06-06 22:33:26.331874

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = "f874ad5e898a"
down_revision = "d80267806131"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "task_type_asset_type_link",
        sa.Column(
            "asset_type_id",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            default=uuid.uuid4,
            nullable=True,
        ),
        sa.Column(
            "task_type_id",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            default=uuid.uuid4,
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["asset_type_id"],
            ["entity_type.id"],
        ),
        sa.ForeignKeyConstraint(
            ["task_type_id"],
            ["task_type.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("task_type_asset_type_link")
    # ### end Alembic commands ###
