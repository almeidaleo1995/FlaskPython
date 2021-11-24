from flask import Blueprint, render_template, request, redirect, url_for
from mod_login.login import validaSessao
from database import Produto



bp_produtos = Blueprint('produtos', __name__, url_prefix='/produtos', template_folder='templates')


@bp_produtos.route("/")
@validaSessao
def formProduto():
    produto = Produto.query.all()
    return render_template("formProduto.html",produto=produto)


@bp_produtos.route('/addProduto', methods = ['GET', 'POST'])
def addProduto():
    if request.method == 'POST':
        produto = Produto(request.form['nome'], request.form['valor'])
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for('produtos.formProduto'))
    return render_template('addProduto.html')   









