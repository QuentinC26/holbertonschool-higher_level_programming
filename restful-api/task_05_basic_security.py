#!/usr/bin/python3
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import datetime
import jwt

app = Flask(__name__)
auth = HTTPBasicAuth()
secret_key = secrets.token_urlsafe(32)

Users = {
    "Anissa_du_06": generate_password_hash("bella"),
    "surfeur_du_07": generate_password_hash("pacific_dream")
    }

payload = {
    'Users': 'test',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
}

token = jwt.encode(payload, secret_key, algorithm='HS256')

@auth.login_required
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/login')
@auth.login_required

if __name__ == '__main__':
    app.run(debug=True)