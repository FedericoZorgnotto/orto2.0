from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from app.models import User
import re

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
def index():
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    params: username, email, password
    casi:
    - andato a buon fine -> return success code, url home
    - username già esistente -> return error code (username already exists)
    - email già esistente -> return error code (email already exists)
    - errore interno -> return error code (internal error)
    """
    if request.method == 'GET':
        return render_template('auth/signup.html', codice=1)
    else:
        user = User()
        return user.register(request.form['username'], request.form['email'], request.form['password'],
                             request.form["username"], request.form["username"])


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    params: username, password
    casi:
    - andato a buon fine -> return success code, url home
    - username non esistente -> return error code (user not found)
    - password errata -> return error code (wrong password)
    - errore interno -> return error code (internal error)
    """
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:
        user = User()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.fullmatch(regex, request.form['username']):
            return jsonify({'message': user.login(request.form['password'], email=request.form['username'])})
        else:
            return jsonify({'message': user.login(request.form['password'], username=request.form['username'])})





@auth_bp.route('/verify/<codice_verifica>')
def verify(codice_verifica):
    """
    params: codice_verifica
    casi:
    - andato a buon fine -> return success code, url home
    - codice_verifica non esistente -> return error code (verification code not found)
    - errore interno -> return error code (internal error)
    """
    user = User()
    code = 0
    if user.verify(codice_verifica) == "successo":
        code = 1
    else:
        code = 3
    return render_template("auth/codeverification.html", verificationstatus=code)


@auth_bp.route("/verification")
def verification():
    return render_template("auth/verification.html")
