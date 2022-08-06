#!/usr/bin/python3

"""
A module that defines a User class which inherits BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines all common attribute/methods for other classes

    Attr:
        state_id (str)
        name (str)
    """
    name = ""
    state_id = ""
