#!/usr/bin/python3
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route('/', methods=['GET'])
def home():
    return jsonify("Welcome to the Flask API!")

@app.route('/data', methods=['GET'])
def get_users():
    return jsonify(list(users.keys()))

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify("OK")

@app.route('/users/<username>', methods=['GET'])
def get_username(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"})

@app.route('/add_user', methods=['POST'])
def post_add_user(username):
    username = request.get_json()
    if not username or 'username' not in users:
        return jsonify({"error": "User is required"}), 400
    if users:
        users = username[-1]['username'] + 1
    else:
        users = 1
    new_user = {
        "message": "User added",
        "user": 
        {
        "username": "",
        "name": "",
        "age": "",
        "city": ""
        }
    }
    users.append(new_user)
    save_users(users)
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(debug=True)
