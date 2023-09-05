#!/usr/bin/env python3
""" Basic auth module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def __init__(self):
        """ Initialization function
        """
        super().__init__()

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Header extraction
        """
        if not authorization_header:
            return None
        elif not isinstance(authorization_header, str):
            return None

        if authorization_header.startswith('Basic '):
            return authorization_header.split(' ')[-1]
        return None
