import mysql.connector
from mysql.connector import Error


class MySQLController:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if not self.connection.is_connected():
                print("Errore durante la connessione a MySQL")
        except Error as e:
            print(f"Errore durante la connessione a MySQL: {e}")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()

    def esegui_query(self, query, dati=None):
        try:
            cursor = self.connection.cursor()

            if dati:
                cursor.execute(query, dati)
            else:
                cursor.execute(query)

            self.connection.commit()
        except Error as e:
            print(f"Errore durante l'esecuzione della query: {e}")

    def fetch_data(self, query):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"Errore durante il recupero dei dati: {e}")
            return None

    def __del__(self):
        self.disconnect()