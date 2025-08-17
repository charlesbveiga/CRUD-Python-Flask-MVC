from app import db
from sqlalchemy import CheckConstraint

class Carros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(15), nullable=False)
    modelo = db.Column(db.String(25), nullable=False)
    ano = db.Column(db.Integer, CheckConstraint('ano >= 1000 AND ano <= 9999'), nullable=False)
