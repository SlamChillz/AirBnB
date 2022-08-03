#!/usr/bin/python3

"""
A module that defines a BaseModel class
"""

from datetime import datetime
from models import storage
from uuid import uuid4


class BaseModel:
    """
    Defines all common attribute/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Instantiation method for class instances

        Arguments:
            args (tuple): variadic number of positional arguments, not used
            kwargs (dict): variadic number of key-words arguments
        """
        if kwargs != {} and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """Write new obj to json file"""
            storage.new(self)

    def __str__(self):
        """
        String representation of instances

        Return:
            (str): string representation of model instance
        """
        return "[{0}] ({1}) {2}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates instance 'update_at' to the current datetime
        """
        self.updated_at = datetime.now()

        """Calls 'storage' save method"""
        storage.save()

    def __format_time(self, time):
        """
        Converts datetime object to "%Y-%m-%dT%H:%M:%S.%f"

        Return:
            time object
        """
        return time.strftime("%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        """
        Return:
            (dict): a dictionary containing all
            keys/values of __dict__ of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary['created_at'] = self.__format_time(dictionary['created_at'])
        dictionary['updated_at'] = self.__format_time(dictionary['updated_at'])
        dictionary['__class__'] = self.__class__.__name__
        return dictionary