from sqlalchemy import Column, String, ForeignKey, Integer

from blog.models.database import db


class Article(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    text = Column(String())
    author = Column(ForeignKey('users.id'))
