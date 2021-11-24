from flask import Blueprint, render_template, request, redirect, url_for
from mod_login.login import validaSessao

from database import Usuario
from app import db

bp_usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios', template_folder='templates')


@bp_usuarios.route("/")
@validaSessao
def formUsuario():
    usuario = Usuario.query.all()
    return render_template("formUsuario.html", usuario=usuario)


@bp_usuarios.route('/add', methods = ['GET', 'POST'])
def addUsuario():
    if request.method == 'POST':
        usuario = Usuario(request.form['login'], request.form['senha'])
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('usuarios.formUsuario'))
    return render_template('addUsuario.html')    


@bp_usuarios.route('/edit/<int:id>', methods=['GET', 'POST'])
def editUsuario(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        usuario.login = request.form['login']
        usuario.senha = request.form['senha']     
        db.session.commit()
        return redirect(url_for('usuarios.formUsuario'))
    return render_template('editUsuario.html', usuario=usuario)


@bp_usuarios.route('/delete/<int:id>')
def delete(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('usuarios.formUsuario'))



