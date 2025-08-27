from flask import Flask
from config import DevelopmentConfig
from app.extensions import db
from app.repositories.carro_repository_mysql import CarroRepositoryMySQL
from app.services.carro_service import CarroService
from app.controllers.carro_controller import create_carro_blueprint

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    service = CarroService(CarroRepositoryMySQL())

    carros_bp = create_carro_blueprint(service)
    app.register_blueprint(carros_bp, url_prefix='/')

    return app
