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


def removeSpecialCharacters(text_string):
    alphanumeric = ""

    for char in text_string:
        if char == '@' or char == '.' or char == '-' or char == ' ':
            alphanumeric += char
        elif char.isalnum():
            alphanumeric += char

    return alphanumeric


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
        update_Fav_Contact = cur.execute(
            'UPDATE contacts set FAVORITE = NOT FAVORITE WHERE contacts.ID = ' + id + ';')
        conn.commit()
        get_all_contacts()
        return jsonify(contacts)

    except Error as e:
        return jsonify(e)

    finally:
        if conn:
            conn.close()


@ app.route('/api/v1/resources/contacts/updateContact/', methods=['POST'])
def updateContact():
    try:
        data = request.get_json()
        conn = None
        sql_string = ""

        id = 0
        if "ID" in data:
            id = data['ID']

        if "FIRST_NAME" in data:
            firstName = removeSpecialCharacters(data['FIRST_NAME'])
        else:
            return jsonify(contacts)

        if "LAST_NAME" in data:
            lastName = removeSpecialCharacters(data['LAST_NAME'])
        else:
            return jsonify(contacts)

        if "WORK_PHONE" in data:
            workPhone = removeSpecialCharacters(data['WORK_PHONE'])
        else:
            workPhone = ''

        if "CELL_PHONE" in data:
            cellPhone = removeSpecialCharacters(data['CELL_PHONE'])
        else:
            return jsonify(contacts)

        if "EMAIL" in data:
            email = removeSpecialCharacters(data['EMAIL'])
        else:
            email = ''

        if "BIRTHDATE" in data:
            birthdate = removeSpecialCharacters(data['BIRTHDATE'])
        else:
            birthdate = ''

        if "STREET_ADDRESS" in data:
            streetAddress = removeSpecialCharacters(data['STREET_ADDRESS'])
        else:
            streetAddress = ''

        if "CITY" in data:
            city = removeSpecialCharacters(data['CITY'])
        else:
            city = ''

        if "STATE" in data:
            state = removeSpecialCharacters(data['STATE'])
        else:
            state = ''

        if "ZIP" in data:
            zip = removeSpecialCharacters(data['ZIP'])
        else:
            zip = ''

        if "NOTE" in data:
            note = removeSpecialCharacters(data['NOTE'])
        else:
            note = ''

        favorite = 0
        active = 1

        conn = sqlite3.connect(db_file)
        conn.row_factory = dict_factory
        cur = conn.cursor()

        # NEW contact insert to database
        if id == 0:
            sql_string = 'INSERT INTO contacts (FIRST_NAME, LAST_NAME, WORK_PHONE, CELL_PHONE,EMAIL, BIRTHDATE, STREET_ADDRESS, CITY, STATE, ZIP, NOTE, FAVORITE, ACTIVE)  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
            val = (firstName, lastName, workPhone, cellPhone, email, birthdate,
                   streetAddress, city, state, zip, note, favorite, active)
        else:
            sql_string = 'UPDATE contacts SET FIRST_NAME = ?, LAST_NAME = ?, WORK_PHONE = ?, CELL_PHONE = ?, EMAIL = ?, BIRTHDATE = ?, STREET_ADDRESS = ?, CITY = ?, STATE = ?, ZIP = ?, NOTE = ?, FAVORITE = ?, ACTIVE = ? WHERE ID = ?;'
            val = (firstName, lastName, workPhone, cellPhone, email, birthdate,
                   streetAddress, city, state, zip, note, favorite, active, id)

        create_update_Contact = cur.execute(sql_string, val)
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
        delete_contact = cur.execute(
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
