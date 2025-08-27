""" Classe que representa um Carro."""
from app.extensions import db

class Carro(db.Model):
    __tablename__ = "carros"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    marca = db.Column(db.String(15), nullable=False)
    modelo = db.Column(db.String(25), nullable=False)
    ano = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Carro {self.marca} {self.modelo} ({self.ano})>"
