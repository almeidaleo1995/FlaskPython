from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def create_app():
    app = Flask(__name__,  template_folder='../templates', static_folder="../static")
    app.app_context().push()

    # apply app configurations
    app.config.from_pyfile('../config.py')

    db.init_app(app)

    # with app.app_context():
    db.create_all()

    from mod_login.login import bp_login
    from mod_home.home import bp_home
    from mod_clientes.clientes import bp_clientes
    from mod_produtos.produtos import bp_produtos
    from mod_usuarios.usuarios import bp_usuarios

    app.register_blueprint(bp_login)
    app.register_blueprint(bp_home)
    app.register_blueprint(bp_clientes)
    app.register_blueprint(bp_produtos)
    app.register_blueprint(bp_usuarios)

    return app