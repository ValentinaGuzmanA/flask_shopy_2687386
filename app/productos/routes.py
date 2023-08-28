
from flask import render_template
from app.productos import productos
from .forms import NewProductForm

@productos.route('/crear')
def crear():
    form =NewProductForm()
    return render_template('new.html',
                           form=form )
