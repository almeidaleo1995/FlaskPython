from flask import Flask
from app import db
from flask_sqlalchemy import SQLAlchemy


class Cliente(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))    
    cpf= db.Column(db.String(150))   
    idade = db.Column(db.Integer)
    

    def __init__(self, nome,cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def __repr__(self):
        return '<Cliente %r>' % self.id
 
        
class Produto(db.Model): 
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))    
    valor = db.Column(db.String(150)) 
    image = db.Column(db.Text)

    def __init__(self, nome,valor, image):
        self.nome = nome    
        self.valor = valor 
        self.image = image

    def __repr__(self):
        return '<Produto %r>' % self.id


     
 
db.create_all()




