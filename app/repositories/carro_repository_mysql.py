from app.models.carro_model import Carro
from app import db
from app.repositories.carro_repository_interface import CarroRepositoryInterface

class CarroRepositoryMySQL(CarroRepositoryInterface):
    
    def listar(self):
        return Carro.query.all()

    def buscar_por_id(self, carro_id):
        return Carro.query.get(carro_id)

    def adicionar(self, carro):
        db.session.add(carro)
        db.session.commit()

    def atualizar(self, carro):
        db.session.commit()

    def deletar(self, carro_id):
        carro = Carro.query.get(carro_id)
        if carro:
            db.session.delete(carro)
            db.session.commit()
