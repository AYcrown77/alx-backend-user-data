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
