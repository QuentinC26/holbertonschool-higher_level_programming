#!/usr/bin/python3
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import datetime
from flask_jwt_extended import JWTManager, create_access_token
import jwt

app = Flask(__name__)
auth = HTTPBasicAuth()
secret_key = secrets.token_urlsafe(32)

users = {
    "Anissa_du_06": {
        "password": generate_password_hash("bella"),
        "role": "user"
    },
    "surfeur_du_07": {
        "password": generate_password_hash("pacific_dream"),
        "role": "admin"
    }
}

payload = {
    'Username': users,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
}

token = jwt.encode(payload, secret_key, algorithm='HS256')
verif_token = jwt.decode(token, key=secret_key, algorithms=['HS256', ])
verif_token.validate()

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/login')
@jwt_required()

if __name__ == '__main__':
    app.run(debug=True)
