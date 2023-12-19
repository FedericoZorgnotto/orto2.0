import bcrypt

from app.services import database

class User:
    def __init__(self, email, password):
        self.email = email
        self.hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.database = database('users')

    def save(self):
        self.database.set(self.email, self.hash_password)

    def check_password(self, password):
        if self.database.get(self.email):
            return bcrypt.checkpw(password.encode('utf-8'), self.database.get(self.email).encode('utf-8'))
        else:
            return False

    def delete(self):
        self.database.delete(self.email)

    def user_exists(self):
        return self.database.get(self.email) is not None

    def __repr__(self):
        return '<User %r>' % self.email
