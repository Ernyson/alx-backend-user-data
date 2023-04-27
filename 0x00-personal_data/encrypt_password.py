#!/usr/bin/env python3
"""Module for encrypting password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Now return a hashed password after hashes using a random salt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checking to see if the password is valid
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
