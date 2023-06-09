#!/usr/bin/env python3
"""Authentication module for the API
"""
import re
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth class module"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """authentication checks"""
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Geting the authorization header from the req"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Geting the current user"""
        return None
