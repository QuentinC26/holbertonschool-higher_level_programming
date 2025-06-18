#!/usr/bin/python3
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_users():
    return jsonify(list(users.keys())), 200

@app.route('/status', methods=['GET'])
def get_status():
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_username(username):
    if username in users:
        return jsonify(users[username]), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "User is required"}), 400
    user = data['username']
    age = data['age']
    city = data['city']
    users[user] = {
        "message": "User added",
        "user":
        {
        "username": user,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
        }
    }
    return jsonify({users[user]}), 201

if __name__ == "__main__":
    app.run(debug=True)
