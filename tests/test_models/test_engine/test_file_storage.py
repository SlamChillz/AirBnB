#!/usr/bin/python3
"""
This module is designed to test the base model
"""
import unittest
from unittest.mock import patch
from models import storage
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
import models.base_model
import uuid
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
        storage._FileStorage__objects = {}

    def test_file_storage(self):
        """
        Test the FileStorage class all method
        """
        self.assertTrue(hasattr(storage, '_FileStorage__objects'))
        self.assertFalse(hasattr(storage, '__objects'))
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)
        self.assertEqual(type(storage), FileStorage)
        with self.assertRaises(TypeError):
            fs = FileStorage(2)
        with self.assertRaises(TypeError):
            fs = FileStorage("foo")
        with self.assertRaises(TypeError):
            fs = FileStorage(None)

    def test_all(self):
        """
        Test the FileStorage class all method
        """
        self.assertEqual(storage.all(), {})
        self.assertEqual(type(storage.all()), dict)
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
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        """
        Test the FileStorage class new method
        """
        b = BaseModel()
        storage.new(b)
        key = "{:s}.{:s}".format(
            b.__class__.__name__, b.id)
        store = storage.all()
        self.assertIn(key, store)
        self.assertEqual(store[key], b)
        self.assertEqual(type(store[key]), type(b))

        b = User()
        storage.new(b)
        key = "{:s}.{:s}".format(
            b.__class__.__name__, b.id)
        store = storage.all()
        self.assertIn(key, store)
        self.assertEqual(store[key], b)
        self.assertEqual(type(store[key]), type(b))

        b = City()
        storage.new(b)
        key = "{:s}.{:s}".format(
            b.__class__.__name__, b.id)
        store = storage.all()
        self.assertIn(key, store)
        self.assertEqual(store[key], b)
        self.assertEqual(type(store[key]), type(b))

        b = State()
        storage.new(b)
        key = "{:s}.{:s}".format(
            b.__class__.__name__, b.id)
        store = storage.all()
        self.assertIn(key, store)
        self.assertEqual(store[key], b)
        self.assertEqual(type(store[key]), type(b))

        b = Place()
        storage.new(b)
        key = "{:s}.{:s}".format(
            b.__class__.__name__, b.id)
        store = storage.all()
        self.assertIn(key, store)
        self.assertEqual(store[key], b)
        self.assertEqual(type(store[key]), type(b))

        b = Amenity()
        storage.new(b)
        key = "{:s}.{:s}".format(
            b.__class__.__name__, b.id)
        store = storage.all()
        self.assertIn(key, store)
        self.assertEqual(store[key], b)
        self.assertEqual(type(store[key]), type(b))

        b = Review()
        storage.new(b)
        key = "{:s}.{:s}".format(
            b.__class__.__name__, b.id)
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
        with self.assertRaises(TypeError):
            storage.save(None)
        os.remove(PATH)

    def test_reload(self):
        """
        Test the FileStorage class save method
        """
        PATH = 'file.json'
        b = BaseModel()
        u = User()
        c = City()
        s = State()
        p = Place()
        a = Amenity()
        r = Review()
        storage.save()
        storage.reload()
        store = FileStorage._FileStorage__objects
        for k, v in store.items():
            self.assertTrue(isinstance(v, BaseModel))
        with self.assertRaises(TypeError):
            storage.reload(2)
        with self.assertRaises(TypeError):
            storage.reload('foo')
        with self.assertRaises(TypeError):
            storage.reload(None)
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
