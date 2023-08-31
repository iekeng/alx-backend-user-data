#!/usr/bin/env python3
'''encrypt_password'''
import bcrypt


def hash_password(password):
    '''password hasher'''
    return bcrypt.hashpw(password.encode('utf-8'),
                         bcrypt.gensalt())
