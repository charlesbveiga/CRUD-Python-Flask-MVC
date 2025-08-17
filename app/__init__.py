from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'random_secret_key'
app.config.from_object('config.Config')

db = SQLAlchemy(app)

from app import routes, models