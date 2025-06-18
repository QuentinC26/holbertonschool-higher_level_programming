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
    for index in users:
        if index == get(username):
            return jsonify(get(username))

if __name__ == "__main__":
    app.run(debug=True)
