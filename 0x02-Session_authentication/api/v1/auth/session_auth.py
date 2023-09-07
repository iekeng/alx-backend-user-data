#!/usr/bin/env python3
"""Session auth module
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """SessionAuth class
    """

    def __init__(self):
        """Initialization function
            """
        super().__init__()
