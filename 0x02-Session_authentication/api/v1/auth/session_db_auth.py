#!/usr/bin/env python3
"""
API session db module
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """ Session DB Authentication 
    """

    def create_session(self, user_id: str = None) -> str:
        """ Creating  Session 
        """
        pass

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ User id for session"""

        if session_id is None or isinstance(session_id, str) is False:
            return None
        else:
            pass

    def destroy_session(self, request=None):
        """ Now deleting user session """
        pass
