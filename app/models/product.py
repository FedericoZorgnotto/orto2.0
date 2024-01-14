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

    def add_picture(self, id, base64, main):
        cursor = self.database.connection.cursor()
        cursor.execute("INSERT INTO images (id_prodotto, immagine_base64, principale) VALUES (%s, %s, %s)",
                       (id, base64, main,))
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

    def add(self, id_vendor, name, description, price, quantity, publication_date):
        cursor = self.database.connection.cursor()
        cursor.execute("SELECT MAX(id) FROM products;")
        if cursor.fetchone()[0] is not None:
            id_element = cursor.fetchone()[0]+1
        else:
            id_element = 0
        print(id_element)
        cursor.execute(
            "INSERT INTO products (id, id_venditore, nome, descrizione, costo, quantita, data_pubblicazione) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (id_element, id_vendor, name, description, price, quantity, publication_date))
        self.database.connection.commit()
        return True

    def remove(self, id_vendor, id):
        cursor = self.database.connection.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s AND id_venditore = %s", (id, id_vendor,))
        self.database.connection.commit()
        return True
