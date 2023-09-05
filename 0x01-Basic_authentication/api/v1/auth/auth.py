#!/usr/bin/env python3
"""Authentication module"""
from flask import request
from typing import List, TypeVar


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
            for _ in excluded_paths:
                excluded = list(_)
                excluded.pop()
                url = list(path)
                if url == excluded:
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
