import os
from flask import session, render_template
from datetime import timedelta

from app import create_app, db

app = create_app()
# gerando uma chave randomica para secret_key
app.secret_key = os.urandom(12).hex()

@app.before_request
def before_request():
    session.permanent = True
    #o padrão é 31 dias...
    app.permanent_session_lifetime = timedelta(minutes=30)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

