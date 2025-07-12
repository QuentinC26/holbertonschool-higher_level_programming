#!/usr/bin/python3
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

Users = {
    "Anissa_du_06": generate_password_hash("bella"),
    "surfeur_du_07": generate_password_hash("pacific_dream")
    }

@auth.login_required
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

if __name__ == '__main__':
    app.run(debug=True)