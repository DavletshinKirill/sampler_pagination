from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(70))
    author = db.Column(db.String(70))

    def __init__(self, title, author):
        self.author = author
        self.title = title
