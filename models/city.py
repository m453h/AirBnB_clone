#!/usr/bin/python3
"""This module creates a City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents City class instance
    """

    state_id = ""
    name = ""
