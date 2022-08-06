#!/usr/bin/python3

"""
A module that defines a Place class which inherits BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Defines all common attribute/methods for other classes

    Attr:
        id (str)
        created_at (datetime)
        updated_at (datetime)
        city_id (str)
        user_id (str)
        name (str)
        description (str)
        number_rooms (int)
        number_bathrooms (int)
        max_guest (int)
        price_by_night (int)
        latitude (int)
        longitude (int)
        amenity_ids (int)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
