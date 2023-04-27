#!/usr/bin/env python3
"""Module used to encrypt passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Function that encrypts passwords"""
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(bytes(password, encoding='utf-8'), salt)

    return hashed_pwd
