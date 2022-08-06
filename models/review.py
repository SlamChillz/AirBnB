#!/usr/bin/python3

"""
A module that defines a Review class which inherits BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines all common attribute/methods for other classes

    Attr:
        id (str)
        created_at (datetime)
        updated_at (datetime)
        place_id (str)
        user_id (str)
        text (str)
    """
    place_id = ""
    user_id = ""
    text = ""
