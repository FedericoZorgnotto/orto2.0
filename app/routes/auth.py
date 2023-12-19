from flask import Blueprint, render_template, request, redirect, session, url_for
from app.models import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
def index():
    return ("<a href='/auth/login'>Login</a> "
            "<br>"
            " <a href='/auth/register'>Register</a>"
            )


@auth_bp.route('/login', methods=['GET'])
def login():
    return render_template('auth/login.html')


@auth_bp.route('/login', methods=['POST'])
def check_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User(username, password)
    if user.check_password(password):
        session['username'] = username
        session['logged_in'] = True
        session['hash_password'] = user.hash_password
        return redirect(url_for("auth.success", azione="login"))
    else:
        return render_template('auth/login.html', error='username o password sbagliati')


@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.permanent = False
    session.clear()
    return redirect(url_for("auth.success", azione='logout'))


@auth_bp.route('/register', methods=['GET'])
def register_form():
    return render_template('auth/register.html')


@auth_bp.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password:
        new_user = User(username, password)
        if (new_user.user_exists()):
            user = User(username, password)
            session['username'] = username
            session['logged_in'] = True
            session['hash_password'] = user.hash_password
            return render_template('auth/register.html', error='Utente già registrato')
        else:
            new_user.save()
            return redirect(url_for("auth.success", azione='register'))
    else:
        return render_template('auth/register.html')


@auth_bp.route('/success/<azione>')
def success(azione):
    if 'logged_in' in session and session.get('logged_in'):
        user = User(session.get('username'), session.get('hash_password'))
        if user.check_password(session.get('hash_password')):
            return render_template('auth/success.html', azione=azione)
        else:
            return redirect('/auth')
    else:
        return redirect('/auth')
