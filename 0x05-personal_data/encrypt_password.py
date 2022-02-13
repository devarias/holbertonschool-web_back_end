#!/usr/bin/env python3
""" module docs """
import bcrypt


def hash_password(password: str) -> bytes:
    """ method docs """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ method docs """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
