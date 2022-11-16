"""Added macros to flavors

Revision ID: 722f5ac2f89e
Revises: 4d3110a6e11d
Create Date: 2022-10-27 13:25:36.313584

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '722f5ac2f89e'
down_revision = '4d3110a6e11d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('platform_flavours', sa.Column('data', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('platform_flavours', 'data')
    # ### end Alembic commands ###