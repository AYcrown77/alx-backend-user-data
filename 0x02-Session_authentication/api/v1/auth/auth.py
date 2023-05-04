#!/usr/bin/env python3
"""Authentication module"""

from flask import request
from typing import List, TypeVar


class Auth():
    """User authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if the path requires authorization
        """
        if path is None or not excluded_paths:
            return True
        for ex_path in excluded_paths:
            if ex_path.endswith('*') and path.startswith(ex_path[:-1]):
                return False
            elif ex_path in {path, path + '/'}:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Checks for  Authorization key in request header
        """
        if request is None:
            return None
        if request.headers.get('Authorization'):
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Checks for current user
        """
        return None

     def session_cookie(self, request=None):
        """
        Returns a cookie value from a request
        """
        if request is None:
            return None
        cook = getenv("SESSION_NAME", None)
        return request.cookies.get(cook)
