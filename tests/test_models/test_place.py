#!/usr/bin/python3
"""
This module is designed to test the Place model
"""
import unittest
import os
from unittest.mock import patch
from datetime import datetime
from io import StringIO
import uuid
import models.base_model
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Class to define the unittest
    """

    def test_Place(self):
        """
        Test the PlaceModel class
        """
        b = Place()
        self.assertIsInstance(b, models.base_model.BaseModel)
        self.assertTrue(issubclass(type(b), models.base_model.BaseModel))
        with patch('models.base_model.uuid4') as mock_id:
            mock_id.return_value = str(
                uuid.UUID("b6a6e15c-c67d-4312-9a75-9d084935e579"))

            base = Place()
            self.assertEqual(base.id, "b6a6e15c-c67d-4312-9a75-9d084935e579")

        with patch('models.base_model.datetime') as mock_date:
            mock_date.now.return_value = datetime(2022, 8, 7, 19, 2, 19, 10000)
            mock_date.side_effect = lambda *args, **kw: datetime(*args, **kw)

            base = Place()
            self.assertEqual(base.created_at, datetime(
                2022, 8, 7, 19, 2, 19, 10000))
            self.assertEqual(type(base.created_at), datetime)
            self.assertEqual(base.updated_at, datetime(
                2022, 8, 7, 19, 2, 19, 10000))
            self.assertEqual(type(base.updated_at), datetime)

        with patch('models.base_model.uuid4') as mock_id:
            with patch('models.base_model.datetime') as mock_date:
                mock_id.return_value = str(
                    uuid.UUID("4c977185-d3f7-4aaa-a46f-c9d27ec4bd5e"))
                mock_date.now.return_value = datetime(
                    2022, 8, 7, 19, 2, 19, 10000)
                mock_date.side_effect = lambda *args, **kw: datetime(
                    *args, **kw)
                b1 = Place('foo')
                self.assertEqual(b1.id, "4c977185-d3f7-4aaa-a46f-c9d27ec4bd5e")
                self.assertEqual(b1.created_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.created_at), datetime)
                self.assertEqual(b1.updated_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.updated_at), datetime)

                b1 = Place(2)
                self.assertEqual(b1.id, "4c977185-d3f7-4aaa-a46f-c9d27ec4bd5e")
                self.assertEqual(b1.created_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.created_at), datetime)
                self.assertEqual(b1.updated_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.updated_at), datetime)

                b1 = Place({})
                self.assertEqual(b1.id, "4c977185-d3f7-4aaa-a46f-c9d27ec4bd5e")
                self.assertEqual(b1.created_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.created_at), datetime)
                self.assertEqual(b1.updated_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.updated_at), datetime)

                b1 = Place(2, 'foo')
                self.assertEqual(b1.id, "4c977185-d3f7-4aaa-a46f-c9d27ec4bd5e")
                self.assertEqual(b1.created_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.created_at), datetime)
                self.assertEqual(b1.updated_at, datetime(
                    2022, 8, 7, 19, 2, 19, 10000))
                self.assertEqual(type(b1.updated_at), datetime)

        clsdict = {"id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                   "created_at": "2017-09-28T21:05:54.119434",
                   "updated_at": "2017-09-28T21:05:54.119434",
                   "__class__": "Place"}
        b2 = Place(**clsdict)
        self.assertEqual(b2.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(b2.created_at, datetime(
            2017, 9, 28, 21, 5, 54, 119434))
        self.assertEqual(type(b1.created_at), datetime)
        self.assertEqual(b2.updated_at, datetime(
            2017, 9, 28, 21, 5, 54, 119434))
        self.assertEqual(type(b2.updated_at), datetime)

        clsdict = {"id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                   "created_at": "2017-09-28T21:05:54.119434",
                   "__class__": "Place"}
        b2 = Place(**clsdict)
        self.assertEqual(b2.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(b2.created_at, datetime(
            2017, 9, 28, 21, 5, 54, 119434))
        self.assertEqual(type(b1.created_at), datetime)
        with self.assertRaises(AttributeError):
            print(b2.updated_at)

        clsdict = {"id": "56d43177-cc5f-4d6c-a0c1-e167f8c27337",
                   "__class__": "Place"}
        b2 = Place(**clsdict)
        self.assertEqual(b2.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        with self.assertRaises(AttributeError):
            print(b2.created_at)
        with self.assertRaises(AttributeError):
            print(b2.updated_at)

    @ patch('sys.stdout', new_callable=StringIO)
    def test_str(self, stdout):
        """
        Test the Place class __str__ method
        """
        with patch('models.base_model.uuid4') as mock_id:
            with patch('models.base_model.datetime') as mock_date:
                mock_id.return_value = str(
                    uuid.UUID("b6a6e15c-c67d-4312-9a75-9d084935e579"))
                mock_date.now.return_value = datetime(
                    2017, 9, 28, 21, 5, 54, 119434)
                mock_date.side_effect = lambda *args, **kw: datetime(
                    *args, **kw)
                base = Place()
                print(base)
                expted_out = ("[Place] "
                              "(b6a6e15c-c67d-4312-9a75-9d084935e579) "
                              "{'id': 'b6a6e15c-c67d-4312-9a75-9d08493"
                              "5e579', 'created_at': datetime.datetime"
                              "(2017, 9, 28, 21, 5, 54, 119434), "
                              "'updated_at': datetime.datetime(2017, "
                              "9, 28, 21, 5, 54, 119434)}\n")
                self.assertEqual(stdout.getvalue(), expted_out)
                stdout.truncate(0)
                stdout.seek(0)

    def test_save(self):
        """
        Test the Place class save method
        """
        PATH = 'file.json'
        with patch('models.base_model.uuid4') as mock_id:
            with patch('models.base_model.datetime') as mock_date:
                mock_id.return_value = str(
                    uuid.UUID("788f5f32-d874-4387-872c-e925314ba80a"))
                mock_date.now.return_value = datetime(
                    2017, 9, 28, 21, 5, 54, 119434)
                mock_date.side_effect = lambda *args, **kw: datetime(
                    *args, **kw)
                base = Place()
                self.assertEqual(base.updated_at, datetime(
                    2017, 9, 28, 21, 5, 54, 119434))
                mock_date.now.return_value = datetime(
                    2017, 9, 28, 21, 5, 54, 119572)
                base.save()
                self.assertEqual(base.updated_at, datetime(
                    2017, 9, 28, 21, 5, 54, 119572))
                self.assertEqual(os.path.isfile(
                    PATH) and os.access(PATH, os.R_OK), True)
                cont = self.write_file(PATH)
                expected = ('"Place.788f5f32-d874-4387-872c-e925314ba80a":'
                            ' {"id": "788f5f32-d874-4387-872c-e925314ba80a", '
                            '"created_at": "2017-09-28T21:05:54.119434", '
                            '"updated_at": "2017-09-28T21:05:54.119572", '
                            '"__class__": "Place"}')
                self.assertIn(expected, cont)
        with self.assertRaises(TypeError):
            base.save(2)
        with self.assertRaises(TypeError):
            base.save('foo')
        os.remove(PATH)

    def test_to_dict(self):
        """
        Test the Place class to_dict method
        """
        with patch('models.base_model.uuid4') as mock_id:
            with patch('models.base_model.datetime') as mock_date:
                mock_id.return_value = str(
                    uuid.UUID("07331301-1393-4f7f-8da5-1f9be6216ad4"))
                mock_date.now.return_value = datetime(
                    2017, 9, 28, 21, 5, 54, 119434)
                mock_date.side_effect = lambda *args, **kw: datetime(
                    *args, **kw)
                base = Place()
                clsdict = {"id": "07331301-1393-4f7f-8da5-1f9be6216ad4",
                           "created_at": "2017-09-28T21:05:54.119434",
                           "updated_at": "2017-09-28T21:05:54.119434",
                           "__class__": "Place"}
                self.assertEqual(base.to_dict(), clsdict)

        with self.assertRaises(TypeError):
            base.to_dict(2)
        with self.assertRaises(TypeError):
            base.to_dict('foo')

    def test_attrib(self):
        """
        Test the Place class public attributes
        """
        b = Place()
        self.assertTrue(hasattr(b, 'city_id'))
        self.assertEqual(b.city_id, "")
        self.assertEqual(type(b.city_id), str)

        self.assertTrue(hasattr(b, 'user_id'))
        self.assertEqual(b.user_id, "")
        self.assertEqual(type(b.user_id), str)

        self.assertTrue(hasattr(b, 'name'))
        self.assertEqual(b.name, "")
        self.assertEqual(type(b.name), str)

        self.assertTrue(hasattr(b, 'description'))
        self.assertEqual(b.description, "")
        self.assertEqual(type(b.description), str)

        self.assertTrue(hasattr(b, 'number_rooms'))
        self.assertEqual(b.number_rooms, 0)
        self.assertEqual(type(b.number_rooms), int)

        self.assertTrue(hasattr(b, 'number_bathrooms'))
        self.assertEqual(b.number_bathrooms, 0)
        self.assertEqual(type(b.number_bathrooms), int)

        self.assertTrue(hasattr(b, 'max_guest'))
        self.assertEqual(b.max_guest, 0)
        self.assertEqual(type(b.max_guest), int)

        self.assertTrue(hasattr(b, 'price_by_night'))
        self.assertEqual(b.price_by_night, 0)
        self.assertEqual(type(b.price_by_night), int)

        self.assertTrue(hasattr(b, 'latitude'))
        self.assertEqual(b.latitude, 0.0)
        self.assertEqual(type(b.latitude), float)

        self.assertTrue(hasattr(b, 'longitude'))
        self.assertEqual(b.longitude, 0.0)
        self.assertEqual(type(b.longitude), float)

        self.assertTrue(hasattr(b, 'amenity_ids'))
        self.assertEqual(b.amenity_ids, [])
        self.assertEqual(type(b.amenity_ids), list)

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
