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


def _generate_uuid(self) -> str:
    """Generates a new uuid"""
    from uuid import uuid4

    return str(uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Method to validat Login from email and password"""
        try:
            usr = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  usr.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Method to create new session for a user"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """Method that gets an instance of User from session id"""
        if not session_id:
            return None
        try:
            user = self.db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Method that destroys user's session"""
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Method that returns a reset password token"""
        user = self._db.find_user_by(email=email)
        if not user:
            raise ValueError("wrong email")
        reset_token = self._generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)

        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Method that updates password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_pwd = _hash_password(password)
            self._db.update_user(user.id,
                                 hashed_password=hashed_pwd,
                                 reset_token=None)
        except Exception:
            raise ValueError("invalid reset token")
