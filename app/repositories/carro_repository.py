"""Responsável pelo CRUD diretamente com o Base de Dados"""
from app.models.carro_model import Carro
from app import db

class CarroRepository:
    @staticmethod
    def get_all():
        return Carro.query.all()

    @staticmethod
    def get_by_id(carro_id: int):
        return Carro.query.get(carro_id)

    @staticmethod
    def add(carro: Carro):
        db.session.add(carro)
        db.session.commit()

    @staticmethod
    def update(carro: Carro):
        db.session.commit()

    @staticmethod
    def delete(carro: Carro):
        db.session.delete(carro)
        db.session.commit()
