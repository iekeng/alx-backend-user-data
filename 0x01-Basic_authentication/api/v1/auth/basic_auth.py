#!/usr/bin/env python3
""" Basic auth module
"""
import base64
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
        """ Header extractor
        """
        if not authorization_header:
            return None
        elif not isinstance(authorization_header, str):
            return None

        if authorization_header.startswith('Basic '):
            return authorization_header.split(' ')[-1]
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        """
        if not base64_authorization_header:
            return None

        elif isinstance(base64_authorization_header, str):
            try:
                header_encode = base64_authorization_header.encode('utf-8')
                return base64.b64decode(header_encode)
            except base64.binascii.Error:
                return None
