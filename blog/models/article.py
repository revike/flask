from datetime import datetime

from sqlalchemy import Column, String, ForeignKey, Integer, DateTime

from blog.extensions import db


class Article(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    text = Column(String())
    author_id = Column(ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    # author = relationship('Author', back_populates='articles')
