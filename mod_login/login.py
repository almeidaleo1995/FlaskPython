#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps

bp_login = Blueprint('login', __name__, url_prefix='/', template_folder='templates')


@bp_login.route("/Paginalogin", methods=['GET', 'POST'])
def login():
    return render_template("formLogin.html")

@bp_login.route("/validalogin", methods=['POST'])
def validaLogin():
    _name = request.form['usuario']
    _pass = request.form['senha']
    # verifica se foi informado usuario e senha
    if _name and _pass and request.method == 'POST' and _name == "abc" and _pass == "123456":
        #limpa a sessão
        session.clear()
        #registra usuario na sessão, armazenando o login do usuário
        session['usuario'] = _name
        #abre a aplicação na tela home
        return redirect(url_for('home.home'))
    else:
        #retorna para a tela de login
        return redirect(url_for('login.login',falhaLogin=1))


@bp_login.route("/logoff", methods=['GET'])
def validaLogoff():
    #remove um item individual da sessão
    session.pop('usuario',None)
    #limpa a sessão
    session.clear()

    #retorna para a tela de login
    return redirect(url_for('login.login'))
    

# valida se o usuário esta ativo na sessão 
# from functools import wraps
def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            #descarta os dados copiados da função original e retorna a tela de login
            return redirect(url_for('login.login',falhaSessao=1))
        else:
            #retorna os dados copiados da função original
            return f(*args, **kwargs)
    #retorna o resultado do if acima
    return decorated_function
