from flask import Flask, request, redirect, session
from config.config import Config
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(Config)

app.permanent_session_lifetime = timedelta(days=7)


ssl_cert_path = app.config.get('SSL_CERT_PATH', 'path/to/cert.pem')
ssl_key_path = app.config.get('SSL_KEY_PATH', 'path/to/key.pem')

from app.routes.home import home_bp
from app.routes.auth import auth_bp
from app.routes.wip import  wip_bp

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(wip_bp)
@app.before_request
def make_session_permanent():
    session.permanent = True

app.run(ssl_context=(ssl_cert_path, ssl_key_path))
