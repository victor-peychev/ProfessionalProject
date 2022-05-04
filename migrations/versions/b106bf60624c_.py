"""empty message

Revision ID: b106bf60624c
Revises: a2e6913ca0a1
Create Date: 2022-04-21 03:05:39.633447

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b106bf60624c'
down_revision = 'a2e6913ca0a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submissions', sa.Column('foreign_id', sa.Integer(), nullable=True))
    op.alter_column('submissions', 'dogs_name',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('submissions', 'dogs_breed',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('submissions', 'dogs_sex',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('submissions', 'dogs_neutered',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.create_foreign_key(None, 'submissions', 'users', ['foreign_id'], ['id'])
    op.drop_column('submissions', 'secondary_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submissions', sa.Column('secondary_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'submissions', type_='foreignkey')
    op.alter_column('submissions', 'dogs_neutered',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('submissions', 'dogs_sex',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('submissions', 'dogs_breed',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('submissions', 'dogs_name',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.drop_column('submissions', 'foreign_id')
    # ### end Alembic commands ###