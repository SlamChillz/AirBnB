#!/usr/bin/python3

"""
A module that defines a class FileStorage for database engine
"""

import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances

    Attr:
        __file_path (str): path to the JSON file
        __objects (dictionary): empty dictionary,
        stores object with key as '<class name>.id
    """
    __file_path = "file_json"
    __objects = {}

    def all(self):
        """
        Return:
            dictionary (dict): __objects attribute
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Attr:
            obj (BaseModel): instance obj
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, mode='w', encoding='utf-8') as j_file:
            j_file.write(json.dumps(self.__objects))

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file exits)
        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as j_file:
                content = j_file.read()
            self.__objects.update(json.loads(content))
        except FileNotFoundError:
            pass
