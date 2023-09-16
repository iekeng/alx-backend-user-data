#!/usr/bin/env python3
"""Authentication module"""
from db import DB
from user import User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a salted password
    """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    return hash


def _generate_uuid() -> str:
    """Return string representation of new uuid
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialization method
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """User registration method
        """
        db = self._db
        user_email = email

        try:
            user = db.find_user_by(email=user_email)

            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            passwd = _hash_password(password)
            user = db.add_user(email, passwd)

            return user

    def valid_login(self, email: str, password: str) -> bool:
        """validate user
        """
        db = self._db
        user_email = email
        try:
            user = db.find_user_by(email=user_email)
            passwd = password.encode('utf-8')
            return bcrypt.checkpw(passwd, user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """create session for user
        """
        db = self._db
        user_email = email
        try:
            user = db.find_user_by(email=user_email)
            session_id = _generate_uuid()
            db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ get user using User.session_id
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """destroy session by user_id
        """
        user = self._db.find_user_by(id=user_id)
        user.session_id = None

    def get_reset_password_token(self, email: str) -> str:
        """generate reset token
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        reset_token = _generate_uuid()
        user.reset_token = reset_token
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Update password
        """
        user_reset_token = reset_token
        try:
            user = self._db.find_user_by(reset_token=user_reset_token)
            hashed_password = _hash_password(password)
        except NoResultFound:
            raise ValueError

        user.hashed_password = hashed_password
        user.reset_token = None
