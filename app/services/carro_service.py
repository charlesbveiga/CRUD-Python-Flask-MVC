class CarroService:
    def __init__(self, repository):
        self.repository = repository

    def listar_carros(self):
        return self.repository.listar()

    def buscar_por_id(self, carro_id):
        return self.repository.buscar_por_id(carro_id)

    def adicionar_carro(self, carro):
        self.repository.adicionar(carro)

    def atualizar_carro(self, carro):
        self.repository.atualizar(carro)

    def deletar_carro(self, carro_id):
        self.repository.deletar(carro_id)
