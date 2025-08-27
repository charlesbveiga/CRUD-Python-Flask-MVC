from abc import ABC, abstractmethod

class CarroRepositoryInterface(ABC):
    
    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def buscar_por_id(self, carro_id):
        pass

    @abstractmethod
    def adicionar(self, carro):
        pass

    @abstractmethod
    def atualizar(self, carro):
        pass

    @abstractmethod
    def deletar(self, carro_id):
        pass
