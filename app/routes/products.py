from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify

products_bp = Blueprint('products', __name__)


@products_bp.route('/')
def index():
    return redirect(url_for('products.research'))


@products_bp.route('/sell', methods=['GET', 'POST'])
def sell():
    if request.method == 'GET':
        return render_template('products/sell.html')
    else:
        return jsonify({'message': 'ok'})


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
        return jsonify({'message': 'ok'})