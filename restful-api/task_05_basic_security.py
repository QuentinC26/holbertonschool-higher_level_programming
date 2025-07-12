#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import datetime
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = secrets.token_urlsafe(32)
jwt = JWTManager(app)

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

@auth.verify_password
def verify_password(username, password):
    if username in users:
        if not check_password_hash(users[username]["password"], password):
            return false, 401
        else:
            return username

@app.route('/login', methods=['POST'])
def post_receive_token():
    data = request.get_json()
    username = data.get("username")
    paswword = data.get("password")
    if username in users:
        if not check_password_hash(users["username"]["password"], password):
            return false, 401
        else:
            return jsonify(create_access_token(users))

if __name__ == '__main__':
    app.run(debug=True)
