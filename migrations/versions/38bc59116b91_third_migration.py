"""Third migration

Revision ID: 38bc59116b91
Revises: da16137370d2
Create Date: 2022-11-08 16:57:48.999453

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy import create_engine, MetaData, Table, Column, String

# revision identifiers, used by Alembic.
revision = '38bc59116b91'
down_revision = 'da16137370d2'
branch_labels = None
depends_on = None

engine = create_engine("postgresql://postgres:qwerty@localhost:5432/test")
meta_data = MetaData()


def upgrade():
    op.create_table('book_1',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(length=70), nullable=True),
    sa.Column('author', sa.String(length=70), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    )
    op.bulk_insert([dict('book')])


def downgrade():
    pass


# def add_data():
#     users.insert().values(title='foo', author='foo', specific='foo')
