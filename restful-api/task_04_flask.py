#!/usr/bin/python3
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = {}


@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def get_users():
    return jsonify(list(users.keys()))


@app.route('/status', methods=['GET'])
def get_status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if username in users:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data or "username" not in data or not data["username"]:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
