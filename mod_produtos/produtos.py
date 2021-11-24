from flask import Blueprint, render_template, request, redirect, url_for
from mod_login.login import validaSessao
from database import Produto
from app import db



bp_produtos = Blueprint('produtos', __name__, url_prefix='/produtos', template_folder='templates')


@bp_produtos.route("/view")
@validaSessao
def formProduto():
    produto = Produto.query.all()
    return render_template("formProduto.html",produto=produto)


@bp_produtos.route('/', methods = ['GET', 'POST'])
def addProduto():
    if request.method == 'POST':
        produto = Produto(request.form['nome'], request.form['valor'])
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for('produtos.formProduto'))
    return render_template('addProduto.html')   


@bp_produtos.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    produto = Produto.query.get(id)
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.valor = request.form['valor']    
        db.session.commit()
        return redirect(url_for('produtos.formProduto'))
    return render_template('editProdutos.html', produto=produto)


@bp_produtos.route('/delete/<int:id>')
def delete(id):
    produto = Produto.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('produtos.formProduto'))








