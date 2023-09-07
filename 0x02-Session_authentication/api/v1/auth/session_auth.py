#!/usr/bin/env python3
"""Session auth module
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """SessionAuth class
    """

    user_id_by_session_id = {}

    def __init__(self):
        """Initialization function
        """
        super().__init__()

    def create_session(self, user_id: str = None) -> str:
        """ Creates user session
        """
        if not user_id:
            return None

        if not isinstance(user_id, str):
            return None

        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
