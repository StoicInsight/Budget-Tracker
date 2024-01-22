"""empty message

Revision ID: 1ed91d1b6441
Revises: 327b4318571c
Create Date: 2024-01-19 20:20:08.235706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ed91d1b6441'
down_revision = '327b4318571c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('firstName', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('lastName', sa.String(length=50), nullable=True))
        batch_op.drop_column('name')
        batch_op.drop_column('lastname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lastname', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.drop_column('lastName')
        batch_op.drop_column('firstName')

    # ### end Alembic commands ###