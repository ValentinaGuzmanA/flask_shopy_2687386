
#dependencias
from flask import Flask 
from .config  import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .mi_blueprint import  mi_blueprint
from app.productos import productos 
from flask_bootstrap import Bootstrap



#inicializar el objeto flask 
app = Flask(__name__)
app.config .from_object(Config)
bootstrap=Bootstrap(app)

#inicializar objeto sqlalchemy 
db = SQLAlchemy(app)
migrate =Migrate(app , db )

#registrar modulos (lueprint)
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)

from .models import Cliente,Venta,Producto,Detalle 
