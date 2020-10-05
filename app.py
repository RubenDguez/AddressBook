import flask
import sqlite3

from sqlite3 import Error
from flask import request, jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config["DEBUG"] = False
db_file = 'test.db'

contacts = []


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_all_contacts():
    contacts.clear()
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = dict_factory
        cur = conn.cursor()
        all_contacts = cur.execute(
            'SELECT * FROM contacts WHERE contacts.ACTIVE = 1').fetchall()

        for c in all_contacts:
            contacts.append(c)

    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


@ app.route('/api/v1/resources/contacts/updateFavoriteContact/<id>', methods=['POST'])
def updateFavoriteContact(id):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = dict_factory
        cur = conn.cursor()
        updateFavContact = cur.execute(
            'UPDATE contacts set FAVORITE = NOT FAVORITE WHERE contacts.ID = ' + id + ';')
        conn.commit()
        get_all_contacts()
        return jsonify(contacts)

    except Error as e:
        return jsonify(e)

    finally:
        if conn:
            conn.close()


@ app.route('/api/v1/resources/contacts/deleteContact/<id>', methods=['POST'])
def deleteContact(id):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = dict_factory
        cur = conn.cursor()
        updateFavContact = cur.execute(
            'UPDATE contacts set ACTIVE = NOT ACTIVE WHERE contacts.ID = ' + id + ';')
        conn.commit()
        get_all_contacts()
        return jsonify(contacts)

    except Error as e:
        return jsonify(e)

    finally:
        if conn:
            conn.close()


@ app.route('/api/v1/resources/contacts/all', methods=['GET'])
def api_all():
    get_all_contacts()
    return jsonify(contacts)


if __name__ == '__main__':
    app.run()
