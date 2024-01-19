from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from app.models import Product

products_bp = Blueprint('products', __name__)


@products_bp.route('/')
def index():
    return redirect(url_for('products.research'))


@products_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('products/add.html')
    else:
        product = Product()
        return jsonify({"message": product.add(request.form["id_vendor"], request.form['name'], request.form['description'],
                                   request.form['price'], request.form['quantity'], request.form['publication_date'])})


@products_bp.route('/remove', methods=['POST'])
def remove():
    product = Product()
    return jsonify({"message": product.remove(request.form["id_vendor"], request.form['id_product'])})


@products_bp.route('/research', methods=['GET', 'POST'])
def research():
    """
    params: name, description, price, quantity, category
    casi:
    - andato a buon fine -> return success code, url home
    - name già esistente -> return error code (name already exists)
    - errore interno -> return error code (internal error)
    """
    if request.method == 'GET':
        return render_template('products/research.html')
    else:
        product = Product()
        return jsonify({"message": product.get_list(int(request.form['offset']), int(request.form['limit']))})


@products_bp.route('/addImage', methods=['POST'])
def addImage():
    product = Product()
    return jsonify({"message": product.add_picture(request.form['id_product'], request.form['base64'], request.form['main'])})


@products_bp.route('/getImages', methods=['POST'])
def getImages():
    product = Product()
    return jsonify({"message": product.get_pictures(request.form['id_product'])})


@products_bp.route('/removeImage', methods=['POST'])
def removeImage():
    product = Product()
    return jsonify({"message": product.remove_picture(request.form['id_image'])})

