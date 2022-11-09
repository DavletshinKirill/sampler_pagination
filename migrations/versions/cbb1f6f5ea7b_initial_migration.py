"""Initial migration

Revision ID: cbb1f6f5ea7b
Revises: 
Create Date: 2022-11-05 12:55:42.589246

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cbb1f6f5ea7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('book',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(length=70), nullable=True),
    sa.Column('author', sa.String(length=70), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    )


def downgrade():
    op.drop_table('book')
