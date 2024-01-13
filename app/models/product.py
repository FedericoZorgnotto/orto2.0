from app.services import database
from flask import url_for, request, jsonify

class Product:
    def __init__(self):
        self.database = database(host="109.123.240.145", user="root", password="qP4yzK2Lyz6XcGk7B2E7Z", database="orto")

    def get_list(self, offset, limit=8):
        cursor = self.database.connection.cursor()
        cursor.execute("SELECT * FROM products")
        cursor.execute("ORDER BY data_pubblicazione")
        cursor.execute("LIMIT %s OFFSET %s", (limit, offset,))
        result = cursor.fetchall()
        offset += 8
        return jsonify({"offset": offset, "result": result})

    def get(self, id):
        cursor = self.database.connection.cursor()
        cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
        result = cursor.fetchone()
        return jsonify(result)

    def get_by_vendor(self, id_vendor):
        cursor = self.database.connection.cursor()
        cursor.execute("SELECT * FROM products WHERE id_venditore = %s", (id_vendor,))
        result = cursor.fetchall()
        return jsonify(result)

    def get_pictures(self, id):
        cursor = self.database.connection.cursor()
        cursor.execute("SELECT * FROM images WHERE id_prodotto = %s", (id,))
        result = cursor.fetchall()
        return jsonify(result)

    def add_picture(self, id, base64):
        cursor = self.database.connection.cursor()
        cursor.execute("INSERT INTO images (id_prodotto, immagine_base64) VALUES (%s, %s)", (id, base64,))
        self.database.connection.commit()
        return True

    def remove_picture(self, id):
        cursor = self.database.connection.cursor()
        cursor.execute("DELETE FROM images WHERE id = %s", (id,))
        self.database.connection.commit()
        return True

    def change_quantity(self, id, quantity):
        cursor = self.database.connection.cursor()
        cursor.execute("UPDATE products SET quantita = %s WHERE id = %s", (quantity, id,))
        self.database.connection.commit()
        return True

    def add(self, id_vendor, nome, descrizione, prezzo, quantita):
        cursor = self.database.connection.cursor()
        cursor.execute("INSERT INTO products (id_venditore, nome, descrizione, costo, quantita) VALUES (%s, %s, %s, %s, %s)", (id_vendor, nome, descrizione, prezzo, quantita,))
        self.database.connection.commit()
        return True
