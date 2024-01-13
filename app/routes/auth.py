from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from app.models import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
def index():
    return ("<a href='/auth/login'>Login</a> "
            "<br>"
            " <a href='/auth/register'>Register</a>"
            )


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
        messaggio = user.register(request.json['username'], request.json['email'], request.json['password'], request.json["username"], request.json["username"])
        if messaggio != "successo":
            return jsonify({'message': messaggio})
        else:
            return render_template('auth/signup.html', codice=2)


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
        if (request.form['username']):
            return jsonify({'message': user.login(request.json['password'], username=request.json['username'])})
        else:
            return jsonify({'message': user.login(request.json['password'], mail=request.json['email'])})
