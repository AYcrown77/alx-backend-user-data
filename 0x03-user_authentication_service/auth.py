#!/usr/bin/env python3
"""Authentication module"""

import bcrypt
from db import DB
from user import User
from typing import Union

from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """used for password hashing"""
    salt = bcrypt.gensalt()

    byte_pwd = password.encode('utf-8')
    hash_pwd = bcrypt.hashpw(byte_pwd, salt)

    return hash_pwd

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

     def register_user(self, email: str, password: str) -> User:
        """Saves a user with email and password to DB"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hash_pwd = _hash_password(password)
            return self._db.add_user(email=email, hashed_password=hash_pwd)
