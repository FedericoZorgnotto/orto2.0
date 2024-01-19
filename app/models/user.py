from app.services import database
from app.services import email_sender
import random
from flask import url_for, request, jsonify


class User:
    def __init__(self):
        self.name = None
        self.surname = None
        self.username = None
        self.email = None
        self.city = None
        self.address = None
        self.password = None
        self.logged = False
        self.database = database(host="109.123.240.145", user="root", password="qP4yzK2Lyz6XcGk7B2E7Z", database="orto")
        self.email_sender = email_sender('smtp.gmail.com', 587,
                                         'noreply.orto2.0@gmail.com',
                                         'kabo mmys fwip ldxl')

    def _generate_verification_code(self):
        return ''.join(random.choice("0123456789") for _ in range(6))

    def register(self, username, email, password, name, surname):
        try:
            cursor = self.database.connection.cursor()
            query = "SELECT * FROM auth WHERE username = %s"
            data = (username,)
            cursor.execute(query, data)

            if cursor.fetchone():
                return 'username già esistente'
            else:
                query = "SELECT * FROM auth WHERE email = %s"
                data = (email,)
                cursor.execute(query, data)
                if cursor.fetchone():
                    return 'email già esistente'
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
                                                 '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">'
                                                 '<html xmlns="http://www.w3.org/1999/xhtml">'
                                                 '<head>'
                                                 '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
                                                 '<meta http-equiv="X-UA-Compatible" content="IE=edge" />'
                                                 '<meta name="viewport" content="width=device-width, initial-scale=1.0">'

                                                 '<style type="text/css">'
                                                 '@import url(' + "https: // fonts.googleapis.com / css2?family = Roboto + Mono" + ');'

                                                                                                                                   'body {'
                                                                                                                                   'font-family: ' + 'Roboto Mono' + ', monospace;'
                                                                                                                                                                     'background-color: F5F5F7;'
                                                                                                                                                                     'display: flex;'
                                                                                                                                                                     'justify-content: center;'
                                                                                                                                                                     'align-items: center;'
                                                                                                                                                                     '}'

                                                                                                                                                                     'img {'
                                                                                                                                                                     'width: 70px;'
                                                                                                                                                                     'height: 70px;'
                                                                                                                                                                     'margin: 0 auto;'
                                                                                                                                                                     'margin-bottom: 20px;'
                                                                                                                                                                     '}'

                                                                                                                                                                     '#card {'
                                                                                                                                                                     'background-color: white;'
                                                                                                                                                                     'display: flex;'
                                                                                                                                                                     'flex-direction: column;'
                                                                                                                                                                     'text-align: center;'
                                                                                                                                                                     'position: absolute;'
                                                                                                                                                                     'width: 480px;'
                                                                                                                                                                     'height: 705px;'
                                                                                                                                                                     'padding: 35px 50px 30px 55px;'
                                                                                                                                                                     'border-radius: 35px;'
                                                                                                                                                                     'box-shadow: 0 0 20px rgba(0, 0, 0, 0.25);'
                                                                                                                                                                     '}'

                                                                                                                                                                     'h2 {'
                                                                                                                                                                     'color: #44653B;'
                                                                                                                                                                     'font-size: 36px;'
                                                                                                                                                                     'font-weight: bolder;'
                                                                                                                                                                     'margin-top: 5px;'
                                                                                                                                                                     'margin-bottom: 35px;'
                                                                                                                                                                     '}'

                                                                                                                                                                     'span {'
                                                                                                                                                                     'font-style: italic;'
                                                                                                                                                                     '}'

                                                                                                                                                                     '#outline {'
                                                                                                                                                                     'color: #44653B;'
                                                                                                                                                                     'height: 450px;'
                                                                                                                                                                     'font-size: 24px;'
                                                                                                                                                                     'font-weight: bolder;'
                                                                                                                                                                     'text-align: left;'
                                                                                                                                                                     'border: #44653B solid 5px;'
                                                                                                                                                                     'border-radius: 35px;'
                                                                                                                                                                     'padding: 25px;'
                                                                                                                                                                     '}'

                                                                                                                                                                     'p {'
                                                                                                                                                                     'color: #44653B;'
                                                                                                                                                                     'font-size: 18px;'
                                                                                                                                                                     'font-weight: bolder;'
                                                                                                                                                                     'margin-top: 0;'
                                                                                                                                                                     'margin-bottom: 35px;'
                                                                                                                                                                     '}'

                                                                                                                                                                     'button {'
                                                                                                                                                                     'color: #F5F5F7;'
                                                                                                                                                                     'background-color: #44653B;'
                                                                                                                                                                     'font-weight: bold;'
                                                                                                                                                                     'font-style: italic;'
                                                                                                                                                                     'font-size: 16px;'
                                                                                                                                                                     'text-align: left;'
                                                                                                                                                                     'width: 300px;'
                                                                                                                                                                     'height: 50px;'
                                                                                                                                                                     'padding-left: 20px;'
                                                                                                                                                                     'padding-top: 4px;'
                                                                                                                                                                     'border-radius: 35px;'
                                                                                                                                                                     'border: none;'
                                                                                                                                                                     'margin-left: 15%;'
                                                                                                                                                                     'margin-bottom: 30px;'
                                                                                                                                                                     'transition: text-indent 0.5s ease;'
                                                                                                                                                                     '}'

                                                                                                                                                                     'button:hover {'
                                                                                                                                                                     'text-indent: 80px;'
                                                                                                                                                                     'cursor: pointer;'
                                                                                                                                                                     '}'
                                                                                                                                                                     '</style>'
                                                                                                                                                                     '</head>'
                                                                                                                                                                     '<body>'
                                                                                                                                                                     '<div id="card">'
                                                                                                                                                                     '<img src=' + "" + 'alt="Orto 2.0" />'
                                                                                                                                                                                        '<h2 id="title">Is it <span>REALLY</span> you?</h2>'
                                                                                                                                                                                        '<div id="outline">'
                                                                                                                                                                                        '<p>Hello<br><br>For security purposes, we need to verify your email address before continuing on our platform.</p>'
                                                                                                                                                                                        '<a href=' + '"' + url + '"' + '>'
                                                                                                                                                                                                                       '<button>VERIFY YOUR EMAIL</button>'
                                                                                                                                                                                                                       '</a>'
                                                                                                                                                                                                                       '<p>Or, copy and paste this link into your browser: + url + <a href=""></a><br><br><br><br><br><br>Thank you,<br>The Orto 2.0 Team</p>'
                                                                                                                                                                                                                       '</div>'
                                                                                                                                                                                                                       '</div>'
                                                                                                                                                                                                                       '</body>'
                                                                                                                                                                                                                       '</html>')

                    return jsonify({"message": "successo", "url": url_for("auth.verification")})
        except Exception as e:
            print("errore durante la registrazione: ", e)
            return jsonify({"message": "errore interno"})

    def login(self, password, username=None, email=None):
        try:
            cursor = self.database.connection.cursor()
            if username:
                query = "SELECT * FROM auth WHERE username = %s"
                data = (username,)
            else:
                query = "SELECT * FROM auth WHERE email = %s"
                data = (email,)
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
    def getId(self, username):
        try:
            cursor = self.database.connection.cursor()
            query = "SELECT id FROM users WHERE nome = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return 'id non trovato'
        except Exception as e:
            print("errore durante la verifica: ", e)
            return 'errore interno'
