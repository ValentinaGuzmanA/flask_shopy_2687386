#dependecias u importaciones 
from flask import Flask 
from config  import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
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
    id = db.Column(db.Integer, 
                   primary_key =True )
    username = db .Column(db.String(100), 
                   unique= True) 
    password = db .Column(db.String(200)) 
    email = db .Column(db.String(100), 
                   unique= True) 

class Productos(db.Model):
    #creando las columnas de db 
    __tablename__="productos" #nombre que tendra la tabla 
    id = db.Column(db.Integer, 
                   primary_key =True )
    nombre = db.Column(db.String(120),
                   unique= True) 
    precio = db.Column(db.Numeric( precision =10,
                   scale=2 ))
    imagen = db.Column(db.String(120),
                        unique =True)
    

class Venta(db.Model):
    #creando las columnas de db 
    __tablename__="Ventas" #nombre que tendra la tabla 
    id = db.Column(db.Integer,
                    primary_key =True )
    fecha = db.Column(db.DateTime, 
                    default = datetime.utcnow) 
    
    precio = db.Column(db.Numeric( precision =10,scale=2 ))
    imagen = db.Column(db.String(120),
                        unique =True)
    
    