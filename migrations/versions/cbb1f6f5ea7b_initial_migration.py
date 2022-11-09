"""Initial migration

Revision ID: cbb1f6f5ea7b
Revises: 
Create Date: 2022-11-05 12:55:42.589246

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy import create_engine, MetaData, Table, Column, String

# revision identifiers, used by Alembic.
revision = 'cbb1f6f5ea7b'
down_revision = None
branch_labels = None
depends_on = None

engine = create_engine("postgresql://postgres:qwerty@localhost:5432/test")
meta_data = MetaData()

book = Table(
    "book",
    meta_data,
    Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    Column('title', sa.String(length=70), nullable=True),
    Column("email_address", String(60)),
    Column('author', sa.String(length=70), nullable=True),
)


def upgrade():
    meta_data.create_all(book)


def downgrade():
    meta_data.drop_all(engine)
