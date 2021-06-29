from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Table, \
    Boolean
from sqlalchemy.orm import relationship

from blog.extensions import db

article_tag_associations_table = Table(
    'article_tag_associations',
    db.metadata,
    Column('article_id', Integer, ForeignKey('articles.id'), nullable=False),
    Column('tag_id', Integer, ForeignKey('tags.id'), nullable=False),
)


class Article(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    text = Column(String())
    author_id = Column(ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    # authors = relationship('Author', back_populates='articles')
    tags = relationship('Tag', secondary=article_tag_associations_table,
                        back_populates='articles')


class Tag(db.Model):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)

    articles = relationship('Article',
                            secondary=article_tag_associations_table,
                            back_populates='tags')


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(255), unique=True)
    password = Column(String(255), default='1')
    is_staff = Column(Boolean, nullable=False, default=False)
    is_active = Column(Boolean, default=True)

    author = relationship('Author', back_populates='user', uselist=False)


class Author(db.Model):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, unique=True)

    user = relationship('User', back_populates='author')
    # articles = relationship('Article', back_populates='author')
