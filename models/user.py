#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents User class instance
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
