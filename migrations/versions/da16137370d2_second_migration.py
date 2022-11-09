"""Second migration

Revision ID: da16137370d2
Revises: 8c92ef275f25
Create Date: 2022-11-05 17:03:00.116447

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import create_engine, MetaData, Table, Column, String
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'da16137370d2'
down_revision = 'cbb1f6f5ea7b'
branch_labels = None
depends_on = None

engine = create_engine("postgresql://postgres:qwerty@localhost:5432/test")

meta_data = MetaData()

book_1 = Table(
    "book_1",
    meta_data,
    Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    Column('title', sa.String(length=70), nullable=True),
    Column("email_address", String(60)),
    Column('author', sa.String(length=70), nullable=True),
)


def upgrade():
    meta_data.create_all(engine)
    meta_data.bind(book)


def downgrade():
    meta_data.drop_all(engine)


# native
# copy (select title from book) to '/var/backups/user_table.csv' with csv header;