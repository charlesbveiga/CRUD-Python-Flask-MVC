from app.models.carro_model import Carro
from app.repositories.carro_repository_interface import CarroRepositoryInterface

class CarroRepositoryMock(CarroRepositoryInterface):
    
    def __init__(self):
        self.carros = []

    def listar(self):
        return self.carros

    def buscar_por_id(self, carro_id):
        for carro in self.carros:
            if carro.id == carro_id:
                return carro
        return None

    def adicionar(self, carro):
        self.carros.append(carro)

    def atualizar(self, carro):
        for i, c in enumerate(self.carros):
            if c.id == carro.id:
                self.carros[i] = carro

    def deletar(self, carro_id):
        self.carros = [c for c in self.carros if c.id != carro_id]
