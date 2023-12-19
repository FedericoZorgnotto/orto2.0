import os
class Config:
    DEBUG = True

    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_secret_key')

    SSL_CERT_PATH = os.environ.get('SSL_CERT_PATH', 'path/to/cert.pem')
    SSL_KEY_PATH = os.environ.get('SSL_KEY_PATH', 'path/to/key.pem')
