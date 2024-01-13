from app.services import database
from app.services import email_sender
import random
from flask import url_for, request


class User:
    def __init__(self):
        self.name = None
        self.surname = None
        self.username = None
        self.email = None
        self.password = None
        self.logged = False
        self.database = database(host="109.123.240.145", user="root", password="qP4yzK2Lyz6XcGk7B2E7Z", database="orto")
        self.email_sender = email_sender('smtp.gmail.com', 587,
                                         'noreply.orto2.0@gmail.com',
                                         'kabo mmys fwip ldxl')

    def _generate_verification_code(self):
        return ''.join(random.choice("0123456789") for _ in range(6))

    def register(self, username, email, password, name, surname):
        # try:
        cursor = self.database.connection.cursor()
        query = "SELECT * FROM auth WHERE username = %s OR email = %s"
        data = (username, email)
        cursor.execute(query, data)

        if cursor.fetchone():
            return 'utente già esistente'
        else:
            codice_verifica = self._generate_verification_code()

            query_auth = "INSERT INTO auth (username, email, password_hash) VALUES (%s, %s, %s);"
            data_auth = (username, email, password)
            cursor.execute(query_auth, data_auth)

            cursor.execute("SELECT LAST_INSERT_ID();")
            id_auth_appena_inserito = cursor.fetchone()[0]

            query_users = "INSERT INTO users (id, nome, cognome, codice_verifica) VALUES (%s, %s, %s, %s);"
            data_users = (id_auth_appena_inserito, name, surname, codice_verifica)
            cursor.execute(query_users, data_users)

            # Esegui il commit delle modifiche
            self.database.connection.commit()

            url = url_for('auth.verify', codice_verifica=codice_verifica, _external=True)

            self.email_sender.invia_mail(email,
                                         'Verifica il tuo Account',
                                        '<html>'
                                            '<body>'
                                                '<h2>Verifica il tuo Account</h2>'
                                                '<a href=' + '"' + url + '"' + '>'
                                                    '<button>Verifica</button>' 
                                                '</a>'
                                                '<p>Se il bottone non funziona, copia e incolla questo new tuo browser: ' + url + '</p>'
                                            '</body>'
                                        '</(html>')

            return 'successo'
        # except Exception as e:
        #     print("errore durante la registrazione: ", e)
        #     return 'errore interno'

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

    def verify(self, codice_verifica):
        try:
            cursor = self.database.connection.cursor()
            query = "SELECT * FROM users WHERE codice_verifica = %s"
            data = (codice_verifica,)
            cursor.execute(query, data)
            result = cursor.fetchone()
            if result:
                query = "UPDATE users SET codice_verifica = NULL WHERE codice_verifica = %s"
                cursor.execute(query, data)
                self.database.connection.commit()
                return 'successo'
            else:
                return 'codice_verifica non trovato'
        except Exception as e:
            print("errore durante la verifica: ", e)
            return 'errore interno'
