from flask import Blueprint, render_template, request, redirect, url_for
from app.models.carro_model import Carro
from app.repositories.carro_repository_mysql import CarroRepositoryMySQL
from app.services.carro_service import CarroService

def create_carro_blueprint(service):
    carros_bp = Blueprint('carros', __name__)

    @carros_bp.route('/')
    def index():
        carros = service.listar_carros()
        return render_template("index.html", carros=carros)

    @carros_bp.route('/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'POST':
            carro = Carro(
                marca=request.form['marca'],
                modelo=request.form['modelo'],
                ano=int(request.form['ano'])
            )
            service.adicionar_carro(carro)
            return redirect(url_for('carros.index'))
        return render_template("create.html")

    @carros_bp.route('/update/<int:carro_id>', methods=['GET', 'POST'])
    def update(carro_id):
        carro = service.buscar_por_id(carro_id)
        if request.method == 'POST':
            carro.marca = request.form['marca']
            carro.modelo = request.form['modelo']
            carro.ano = int(request.form['ano'])
            service.atualizar_carro(carro)
            return redirect(url_for('carros.index'))
        return render_template("update.html", carro=carro)

    @carros_bp.route('/delete/<int:carro_id>', methods=['POST'])
    def delete(carro_id):
        service.deletar_carro(carro_id)
        return redirect(url_for('carros.index'))

    return carros_bp
