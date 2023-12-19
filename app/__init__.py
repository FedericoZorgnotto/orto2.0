from flask import Flask, request, redirect
from config.config import Config
app = Flask(__name__)
app.config.from_object(Config)


ssl_cert_path = app.config.get('SSL_CERT_PATH', 'path/to/cert.pem')
ssl_key_path = app.config.get('SSL_KEY_PATH', 'path/to/key.pem')

from app.routes.home import home_bp

app.register_blueprint(home_bp)

app.run(ssl_context=(ssl_cert_path, ssl_key_path))
