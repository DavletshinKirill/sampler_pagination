"""Second migration

Revision ID: da16137370d2
Revises: 8c92ef275f25
Create Date: 2022-11-05 17:03:00.116447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da16137370d2'
down_revision = 'cbb1f6f5ea7b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('book', sa.Column('publication_house', sa.String(length=70), nullable=True))
    op.execute('UPDATE book SET publication_house = author, author = Null;')


def downgrade():
    op.execute('UPDATE book SET author = publication_house')
    op.drop_column('book', 'publication_house')


# native
# copy (select title from book) to '/var/backups/user_table.csv' with csv header;