from flask import request, redirect, url_for, render_template
from app import app, db
from app.models import Carros

@app.route('/')
def index():
    carros_ = Carros.query.all()
    return render_template('index.html', carros=carros_)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        ano = request.form['ano']
        
        # cria um novo objeto Carros
        new_carro = Carros(marca=marca, modelo=modelo, ano=ano)
        
        db.session.add(new_carro)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    carro = Carros.query.get_or_404(id)  # busca o carro pelo ID
    if request.method == 'POST':
        carro.marca = request.form['marca']
        carro.modelo = request.form['modelo']
        carro.ano = request.form['ano']
        db.session.commit()
        return redirect(url_for('index'))  # volta para a lista
    return render_template('update.html', carro=carro)

@app.route('/delete/<int:id>')
def delete(id):
    carro = Carros.query.get_or_404(id)
    db.session.delete(carro)
    db.session.commit()
    return redirect(url_for('index'))
