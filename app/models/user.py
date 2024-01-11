import bcrypt

from app.services import database


class User:
    def __init__(self):
        self.username = None
        self.email = None
        self.password = None
        self.logged = False
        self.database = database(host="109.123.240.145", user="root", password="qP4yzK2Lyz6XcGk7B2E7Z", database="orto")

    def register(self, username, email, password):
        try:
            cursor = self.database.connection.cursor()
            query = "SELECT * FROM auth WHERE username = %s OR email = %s"
            data = (username, email)
            cursor.execute(query, data)

            if cursor.fetchone():
                return 'utente già esistente'
            else:
                query = "INSERT INTO auth (username, email, password_hash) VALUES (%s, %s, %s)"
                data = (username, email, password)
                cursor.execute(query, data)
                self.database.connection.commit()
                return 'successo'
        except Exception as e:
            print("errore durante la registrazione: ", e)
            return 'errore interno'

    def login(self, password, username=None, mail=None):
        try:
            cursor = self.database.connection.cursor()
            if username:
                query = "SELECT * FROM auth WHERE username = %s"
                data = (username,)
            else:
                query = "SELECT * FROM auth WHERE email = %s"
                data = (mail,)
            cursor.execute(query, data)
            result = cursor.fetchone()
            if result:
                if password == result[3]:
                    self.logged = True
                    self.username = result[1]
                    self.email = result[2]
                    self.password = result[3]
                    return 'successo'
                else:
                    return 'password errata'
            else:
                return 'utente non trovato'
        except Exception as e:
            print("errore durante il login: ", e)
            return 'errore interno'
