from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash

from blog.extensions import db

article_tag_associations_table = Table(
    'article_tag_associations',
    db.metadata,
    db.Column('article_id', db.Integer, ForeignKey('articles.id'),
              nullable=False),
    db.Column('tag_id', db.Integer, ForeignKey('tags.id'), nullable=False),
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), default='1')
    is_staff = db.Column(db.Boolean, nullable=False, default=False)
    is_active = db.Column(db.Boolean, default=True)

    author = relationship('Author', back_populates='user', uselist=False)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(ForeignKey('users.id'), nullable=False, unique=True)

    user = relationship('User', back_populates='author')
    # articles = relationship('Article', back_populates='author')

    def __str__(self):
        return self.user.username


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.String())
    author_id = db.Column(ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow)

    # author = relationship('Author', back_populates='articles')
    tags = relationship('Tag', secondary=article_tag_associations_table,
                        back_populates='articles')


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    articles = relationship('Article',
                            secondary=article_tag_associations_table,
                            back_populates='tags')

    def __str__(self):
        return self.name
