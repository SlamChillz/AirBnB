#!/usr/bin/python3
"""
This module is designed to test the base model
"""
import unittest
from unittest.mock import patch
from models.engine.file_storage import FileStorage
import os
from datetime import datetime
from io import StringIO
import uuid
import models.base_model
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Class to define the unittest
    """

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """
        Test the FileStorage class all method
        """
        storage = FileStorage()
        self.assertEqual(storage.all(), {})
        b = BaseModel()
        u = User()
        a = Amenity()
        self.assertEqual(len(storage.all()), 3)
        for k, v in storage.all().items():
            self.assertTrue(isinstance(v, BaseModel))
        with self.assertRaises(TypeError):
            storage.all(2)
        with self.assertRaises(TypeError):
            storage.all('foo')

    def test_new(self):
        """
        Test the FileStorage class new method
        """
        storage = FileStorage()
        with patch('models.base_model.uuid4') as mock_id:
            mock_id.return_value = str(
                uuid.UUID("b6a6e15c-c67d-4312-9a75-9d084935e579"))
            b = BaseModel()
            storage.new(b)
            key = "{:s}.{:s}".format(
                b.__class__.__name__, "b6a6e15c-c67d-4312-9a75-9d084935e579")
            store = storage.all()
            self.assertIn(key, store)
            self.assertEqual(store[key], b)
            self.assertEqual(type(store[key]), type(b))

            b = User()
            storage.new(b)
            key = "{:s}.{:s}".format(
                b.__class__.__name__, "b6a6e15c-c67d-4312-9a75-9d084935e579")
            store = storage.all()
            self.assertIn(key, store)
            self.assertEqual(store[key], b)
            self.assertEqual(type(store[key]), type(b))

            b = City()
            storage.new(b)
            key = "{:s}.{:s}".format(
                b.__class__.__name__, "b6a6e15c-c67d-4312-9a75-9d084935e579")
            store = storage.all()
            self.assertIn(key, store)
            self.assertEqual(store[key], b)
            self.assertEqual(type(store[key]), type(b))

            b = State()
            storage.new(b)
            key = "{:s}.{:s}".format(
                b.__class__.__name__, "b6a6e15c-c67d-4312-9a75-9d084935e579")
            store = storage.all()
            self.assertIn(key, store)
            self.assertEqual(store[key], b)
            self.assertEqual(type(store[key]), type(b))

            b = Place()
            storage.new(b)
            key = "{:s}.{:s}".format(
                b.__class__.__name__, "b6a6e15c-c67d-4312-9a75-9d084935e579")
            store = storage.all()
            self.assertIn(key, store)
            self.assertEqual(store[key], b)
            self.assertEqual(type(store[key]), type(b))

            b = Amenity()
            storage.new(b)
            key = "{:s}.{:s}".format(
                b.__class__.__name__, "b6a6e15c-c67d-4312-9a75-9d084935e579")
            store = storage.all()
            self.assertIn(key, store)
            self.assertEqual(store[key], b)
            self.assertEqual(type(store[key]), type(b))

            b = Review()
            storage.new(b)
            key = "{:s}.{:s}".format(
                b.__class__.__name__, "b6a6e15c-c67d-4312-9a75-9d084935e579")
            store = storage.all()
            self.assertIn(key, store)
            self.assertEqual(store[key], b)
            self.assertEqual(type(store[key]), type(b))

            with self.assertRaises(AttributeError):
                storage.new(2)
            with self.assertRaises(AttributeError):
                storage.new('foo')
            with self.assertRaises(TypeError):
                storage.new()
            with self.assertRaises(TypeError):
                storage.new(2, 'foo')
            with self.assertRaises(AttributeError):
                storage.new(None)

    def test_save(self):
        """
        Test the FileStorage class save method
        """
        PATH = 'file.json'
        storage = FileStorage()
        with patch('models.base_model.uuid4') as mock_id:
            with patch('models.base_model.datetime') as mock_date:
                mock_id.return_value = str(
                    uuid.UUID("788f5f32-d874-4387-872c-e925314ba80a"))
                mock_date.now.return_value = datetime(
                    2022, 8, 7, 19, 2, 19, 10000)
                mock_date.side_effect = lambda *args, **kw: datetime(
                    *args, **kw)
                b = BaseModel()
                u = User()
                c = City()
                s = State()
                p = Place()
                a = Amenity()
                r = Review()
                storage.save()
                self.assertEqual(os.path.isfile(
                    PATH) and os.access(PATH, os.R_OK), True)
                cont = self.write_file(PATH)
                expected = ('{"BaseModel.788f5f32-d874-4387-872c-e925314ba80a"'
                            ': {"id": "788f5f32-d874-4387-872c-e925314ba80a", '
                            '"created_at": "2022-08-07T19:02:19.010000", '
                            '"updated_at": "2022-08-07T19:02:19.010000", '
                            '"__class__": "BaseModel"}, '
                            '"User.788f5f32-d874-4387-872c-e925314ba80a": '
                            '{"id": "788f5f32-d874-4387-872c-e925314ba80a", '
                            '"created_at": "2022-08-07T19:02:19.010000", '
                            '"updated_at": "2022-08-07T19:02:19.010000", '
                            '"__class__": "User"}, "City.788f5f32-d874-4387-'
                            '872c-e925314ba80a": {"id": "788f5f32-d874-4387-'
                            '872c-e925314ba80a", "created_at": "2022-08-07T19:'
                            '02:19.010000", "updated_at": "2022-08-07T19:02:'
                            '19.010000", "__class__": "City"}, "State.788f5f32'
                            '-d874-4387-872c-e925314ba80a": {"id": "788f5f32-'
                            'd874-4387-872c-e925314ba80a", "created_at": "2022'
                            '-08-07T19:02:19.010000", "updated_at": "2022-08-'
                            '07T19:02:19.010000", "__class__": "State"}, '
                            '"Place.788f5f32-d874-4387-872c-e925314ba80a": '
                            '{"id": "788f5f32-d874-4387-872c-e925314ba80a", '
                            '"created_at": "2022-08-07T19:02:19.010000", '
                            '"updated_at": "2022-08-07T19:02:19.010000", '
                            '"__class__": "Place"}, "Amenity.788f5f32-d874-'
                            '4387-872c-e925314ba80a": {"id": "788f5f32-d874'
                            '-4387-872c-e925314ba80a", "created_at": "2022-'
                            '08-07T19:02:19.010000", "updated_at": "2022-08-'
                            '07T19:02:19.010000", "__class__": "Amenity"}, '
                            '"Review.788f5f32-d874-4387-872c-e925314ba80a": '
                            '{"id": "788f5f32-d874-4387-872c-e925314ba80a", '
                            '"created_at": "2022-08-07T19:02:19.010000", '
                            '"updated_at": "2022-08-07T19:02:19.010000", '
                            '"__class__": "Review"}}')
                self.assertEqual(expected, cont)
        with self.assertRaises(TypeError):
            storage.save(2)
        with self.assertRaises(TypeError):
            storage.save('foo')
        os.remove(PATH)

    def test_reload(self):
        """
        Test the FileStorage class save method
        """
        PATH = 'file.json'
        storage = FileStorage()
        b = BaseModel()
        u = User()
        c = City()
        s = State()
        p = Place()
        a = Amenity()
        r = Review()
        storage.save()
        storage.reload()
        for k, v in storage.all().items():
            self.assertTrue(isinstance(v, BaseModel))
        with self.assertRaises(TypeError):
            storage.reload(2)
        with self.assertRaises(TypeError):
            storage.reload('foo')
        os.remove(PATH)

        if os.path.isfile(
                PATH) and os.access(PATH, os.R_OK) is False:
            with self.assertRaises(FileNotFoundError):
                storage.reload()

    @staticmethod
    def write_file(filename):
        """
        A function that opens and reads a file
        Args:
            filename (str)
        Returns:
            number of characters written into file
        """
        with open(filename, 'r', encoding="utf-8") as f:
            text = ""
            for line in f:
                text += line
            return text
