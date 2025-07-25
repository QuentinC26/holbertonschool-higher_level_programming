#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity,  get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "the-secret_key"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

jwt = JWTManager(app)

users = {
    "user1": {
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(users[username]["password"], password):
        return username
    else:
        return None

@app.route('/login', methods=['POST'])
def post_receive_token():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password or username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    else:
        user = users[username]
        access_token = create_access_token(identity=username, additional_claims={"role": user["role"]})
        return jsonify(access_token=access_token), 200

@app.route('/basic-protected')
@auth.login_required
def get_basic_protected_authorization():
    return "Basic Auth: Access Granted"

@app.route('/jwt-protected')
@jwt_required()
def get_jwt_protected_authorization():
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def get_admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

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
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401
      
@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()
