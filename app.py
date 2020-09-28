from flask import Flask, jsonify
app = Flask(__name__)


def getAllContacts():
    contacts = (
        {
            'Name': 'Argenis',
            'Last Name': 'Dominguez',
            'Work Phone': '4075552345',
            'Cell Phone': '4074445678'
        },
        {
            'Name': 'Lisa',
            'Last Name': 'Freiwald',
            'Work Phone': '407-555-3456',
            'Cell Phone': '407-444-5678'
        }

    )
    return contacts


@app.route('/')
def LandingPage():
    return "This is the landing page for the AddressBook api"


@app.route('/getContacts')
def getContacts():
    return jsonify(getAllContacts())


if __name__ == '__main__':
    app.run()
