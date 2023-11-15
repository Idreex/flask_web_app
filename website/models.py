from . import db
from sqlalchemy import Column, String, Integer, Date, ForeignKey,
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id =  db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    firstname = db.Column(db.String(150))
    password = db.Column(db.String(150))
    notes = db.Relationship('Note', backref='owned_user', lazy=True)

    

    