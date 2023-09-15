#!/usr/bin/env python3
"""flask app module
"""
from flask import Flask, jsonify, request
from auth import Auth
from user import User

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """home route view
    """
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


@app.route("/users", methods=['POST'], strict_slashes=False)
def users():
    """user registration app
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        response = f'{"email": "{email}", "message": "user created"}'
        return jsonify(response), 200

    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
