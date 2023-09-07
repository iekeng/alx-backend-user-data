#!/usr/bin/env python3
"""Authentication module"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """ Authentication class,
        provides methods for basic auth
    """

    def __init__(self):
        """Initialize Auth class
        """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Affirms excluded paths
        """
        if excluded_paths is None or path is None:
            return True

        elif path not in excluded_paths:
            for excluded in excluded_paths:
                prefix = excluded[:-1]
                if path == prefix or path.startswith(prefix):
                    return False
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """ Checks for Authorization key
        in request header
        """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ Currently does nothing
        """
        return None

    def session_cookie(self, request=None):
        """ Retrive session cookie
        """
        if not request:
            return None

        cookies = request.cookies

        if not cookies:
            return None

        session_name = os.getenv('SESSION_NAME')

        return cookies.get(session_name)
