from flask import Blueprint, render_template, request, redirect, session, url_for
from app.models import User

auth_bp = Blueprint('auth', __name__)

#region pagine (GET)
@auth_bp.route('/')
def index():
    return ("<a href='/auth/login'>Login</a> "
            "<br>"
            " <a href='/auth/register'>Register</a>"
            )
@auth_bp.route('/login', methods=['GET'])
def login():
    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET'])
def register_form():
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

#endregion

#region API (POST)
@auth_bp.route('/login', methods=['POST'])
def check_login():

    if request.is_json:
        username = request.json.get('username')
        password = request.json.get('password')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

    user = User(username, password)
    if user.check_password(password):
        session['username'] = username
        session['logged_in'] = True
        session['hash_password'] = user.hash_password
        if request.is_json:
            return "accesso effettuato"
        else:
            return redirect(url_for("auth.success", azione="login"))
    else:
        if request.is_json:
            return "username o password sbagliati"
        else:
            return render_template('auth/login.html', error='username o password sbagliati')
@auth_bp.route('/register', methods=['POST'])
def register():
    if request.is_json:
        username = request.json.get('username')
        password = request.json.get('password')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
    if username and password:
        new_user = User(username, password)
        if (new_user.user_exists()):
            if request.is_json:
                return "utente già registrato"
            else:
                return render_template('auth/register.html', error='Utente già registrato')
        else:
            new_user.save()

            user = User(username, password)
            session['username'] = username
            session['logged_in'] = True
            session['hash_password'] = user.hash_password
            if request.is_json:
                return "registrazione effettuata"
            else:
                return redirect(url_for("auth.success", azione='register'))
    else:
        if request.is_json:
            return "username o password non inseriti"
        else:
            return render_template('auth/register.html')
@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.permanent = False
    session.clear()
    return redirect(url_for("auth.success", azione='logout'))
@auth_bp.route('/change_password', methods=['POST'])
def cambia_password():
    if 'logged_in' in session and session.get('logged_in'):
        user = User(session.get('username'), session.get('hash_password'))
        if user.check_password(session.get('hash_password')):
            if request.is_json:
                password = request.json.get('password')
            else:
                password = request.form.get('password')
            user.change_password(password)
            session['hash_password'] = user.hash_password
            if request.is_json:
                return "password cambiata"
            else:
                return redirect(url_for("auth.success", azione='cambio password'))
        else:
            if request.is_json:
                return "password errata"
            else:
                return redirect('/auth')
    else:
        if request.is_json:
            return "non sei loggato"
        else:
            return redirect('/auth')
@auth_bp.route('/delete', methods=['POST'])
def delete():
    if 'logged_in' in session and session.get('logged_in'):
        user = User(session.get('username'), session.get('hash_password'))
        if user.check_password(session.get('hash_password')):
            user.delete()
            session.permanent = False
            session.clear()
            if request.is_json:
                return "utente cancellato"
            else:
                return redirect(url_for("auth.success", azione='delete'))
        else:
            if request.is_json:
                return "password errata"
            else:
                return redirect('/auth')
    else:
        if request.is_json:
            return "non sei loggato"
        else:
            return redirect('/auth')

#endregion