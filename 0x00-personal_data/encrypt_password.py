#!/usr/bin/env python3
'''encrypt_password'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''password hasher'''
    return bcrypt.hashpw(password.encode(),
                         bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''Validate password'''
    encoded_bytes = password.encode()
    return bcrypt.checkpw(encoded_bytes, hashed_password)
