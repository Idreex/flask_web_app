from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Integer, String,DateTime,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column



class Note(db.Model):
    id: Mapped[str] = mapped_column(Integer, primary_key=True)
    data: Mapped[str] = mapped_column(String, nullable=False)
    date:Mapped[DateTime] = mapped_column(DateTime(timezone=True),default=func.now())
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    notes = db.relationship('Note', backref='owned_user', lazy=True)

    

    