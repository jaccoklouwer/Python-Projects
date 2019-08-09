from flask import current_app
from WhatsUp import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    mobileNumber = db.Column(db.string(10), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    contacts = db.Relationship("Contact", backref="owner", lazy=True)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    mobileNumber = db.Column(db.string(15), unique=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Relationship("Account", backref="sender", lazy=True)
    reciever = db.Relationship("Contact", backref="reciever", lazy=True)
    message = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
