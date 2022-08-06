#!/usr/bin/python3

"""
A module that defines a User class which inherits BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines all common attribute/methods for other classes

    Attr:
        name (str)
    """
    name = ""
