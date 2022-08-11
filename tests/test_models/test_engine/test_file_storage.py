#!/usr/bin/python3
"""
This module is designed to test the base model
"""
import unittest
from models import storage
import os
from models.engine.file_storage import FileStorage
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
        self.assertEqual(FileStorage._FileStorage__objects, {})
        self.assertEqual(storage._FileStorage__objects, {})
        self.assertTrue(hasattr(storage, '_FileStorage__objects'))
        self.assertFalse(hasattr(storage, '__objects'))
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)
        self.assertEqual(type(storage._FileStorage__objects), dict)
        self.assertEqual(type(storage), FileStorage)
        with self.assertRaises(AttributeError):
            print(storage.__objects)
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
        key = "{:s}.{:s}".format(
            b.__class__.__name__, b.id)
        self.assertIn(key, cont)
        key = "{:s}.{:s}".format(
            u.__class__.__name__, u.id)
        self.assertIn(key, cont)
        key = "{:s}.{:s}".format(
            c.__class__.__name__, c.id)
        self.assertIn(key, cont)
        key = "{:s}.{:s}".format(
            s.__class__.__name__, s.id)
        self.assertIn(key, cont)
        key = "{:s}.{:s}".format(
            p.__class__.__name__, p.id)
        self.assertIn(key, cont)
        key = "{:s}.{:s}".format(
            a.__class__.__name__, a.id)
        self.assertIn(key, cont)
        key = "{:s}.{:s}".format(
            r.__class__.__name__, r.id)
        self.assertIn(key, cont)
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
        storage.reload()
        self.assertEqual(FileStorage._FileStorage__objects, {})
        b = BaseModel()
        u = User()
        c = City()
        s = State()
        p = Place()
        a = Amenity()
        r = Review()
        storage.save()
        storage.reload()
        store = storage._FileStorage__objects
        for k, v in store.items():
            self.assertTrue(isinstance(v, BaseModel))
        self.assertIn(b.__class__.__name__ + '.' + b.id, store.keys())
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
