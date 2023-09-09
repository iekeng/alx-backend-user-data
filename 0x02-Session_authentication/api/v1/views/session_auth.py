#!/usr/bin/env python3
"""Session auth module
"""
from models.user import User
from flask import jsonify, session, make_response, request
from api.v1.views import app_views
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_handler():
    """ Session authentication
    """
    email = request.form.get('email')
    if not email or email == '':
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if not user.is_valid_password:
            return jsonify({"error": "wrong password"}), 401

        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        session_name = os.getenv('SESSION_NAME')
        response = make_response(user.to_json())
        response.set_cookie(session_name, session_id)

    return response
