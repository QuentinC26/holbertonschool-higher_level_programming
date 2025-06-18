#!/usr/bin/python3
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route('/')
def home():
    return jsonify("Welcome to the Flask API!")

@app.route('/data')
def get_users():
    return jsonify(list(users))

@app.route('/status')
def get_status():
    return jsonify("OK")

@app.route('/users/<username>')
def get_username(username):
    for user in users:
        if user['username'] == username:
            return jsonify(user)
    return jsonify({"error": "User not found"})

if __name__ == "__main__":
    app.run(debug=True)
