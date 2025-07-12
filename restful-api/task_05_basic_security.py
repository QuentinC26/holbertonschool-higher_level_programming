#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from datetime import timedelta
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = secrets.token_urlsafe(32)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

jwt = JWTManager(app)

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401
      
@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

users = {
    "Anissa_du_06": {
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "surfeur_du_07": {
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        if check_password_hash(users[username]["password"], password):
            return username
        else:
            return False

@app.route('/login', methods=['POST'])
def post_receive_token():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password or username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    else:
        access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
        return jsonify(access_token=access_token)

@app.route('/basic-protected')
@auth.login_required
def get_basic_protected_authorization():
    return jsonify({"Basic Auth: Access Granted"})

@app.route('/jwt-protected')
@jwt_required()
def get_jwt_protected_authorization():
    return jsonify({"JWT Auth: Access Granted"})

@app.route('/admin-only')
@jwt_required()
def get_admin_only():
    data_of_admin = get_jwt_identity()
    role = data_of_admin.get("role")
    if not role == "admin":
        return jsonify({"error": "Admin access required"}), 403
    else:
        return jsonify({"Admin Access: Granted"})


if __name__ == '__main__':
    app.run(debug=True)
