#!/usr/bin/env python3
""" Basic auth module
"""
import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
from models.base import DATA


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
        """ Decode authorization header
        """
        if not base64_authorization_header:
            return None

        elif not isinstance(base64_authorization_header, str):
            return None

        try:
            header_encode = base64_authorization_header.encode('ascii')
            data_bytes = base64.b64decode(header_encode)

            return data_bytes.decode('ascii')

        except base64.binascii.Error:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extract user credentials
        """
        if not decoded_base64_authorization_header:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_info = decoded_base64_authorization_header.split(':')
        return user_info[0], user_info[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Retrieves user credentials from header
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        elif user_pwd is None or not isinstance(user_pwd, str):
            return None

        if 'User' not in DATA:
            return None
        users = User.search({'email': user_email})

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
