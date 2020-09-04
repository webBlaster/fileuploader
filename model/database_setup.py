from flask_sqlalchemy import SQLAlchemy
from config import app

db = SQLAlchemy(app)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(225), unique=True, nullable=False)

class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(80), unique=True, nullable=False)
    url = db.Column(db.String(225), unique=True, nullable=False)

db.create_all()