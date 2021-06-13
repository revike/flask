from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from blog.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(255), unique=True)
    password = Column(String(255), default='1')
    is_staff = Column(Boolean, nullable=False, default=False)
    is_active = Column(Boolean, default=True)
