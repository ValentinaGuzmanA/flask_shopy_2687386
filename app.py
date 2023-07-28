#dependecias u importaciones 
from flask import Flask 
from config  import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#inicializar el objeto flask 
app = Flask(__name__)
app.config .from_object(Config)

#inicializar objeto sqlalchemy 
db = SQLAlchemy(app)
migrate =Migrate(app , db )
#modelos-entidades proyecto

class Cliente(db.Model):
    #creando las columnas de db 
    __tablename__="clientes" #nombre que tendra la tabla 
    id = db.Column(db.Integer, primary_key =True )
    username = db .Column(db.String(100), unique= True) 
    password = db .Column(db.String(200)) 
    email = db .Column(db.String(100), unique= True) 

    