#!/usr/bin/python3

"""
Test module for the console 'create' command
"""
import os
import sys
import json
import unittest
from io import StringIO
from unittest.mock import patch

import models
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from console import HBNBCommand as CMD

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
"""Add parent dir to sys path"""
sys.path.append(parent_dir)


class TestCreateCommand(unittest.TestCase):
    """
    Tests for create command
    """

    def setUp(self):
        """Reset storage object"""
        models.storage.clean()

    def tearDown(self):
        """Remove storage after every test"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def output(self, cmd):
        """Returns console output"""
        with patch('sys.stdout', new=StringIO()) as f:
            CMD().onecmd(cmd)
            return f.getvalue()

    def storage(self):
        """Retrieves storage content"""
        with open('file.json', mode='r', encoding='utf-8') as file:
            data = file.read()
            return json.loads(data)

    def validModel(self, model):
        """Tests with valid model"""
        cmd = "{} {}".format("create", model)
        output = (self.output(cmd)).strip("\n")
        data = self.storage()
        """Check json content"""
        self.assertEqual(1, len(data))
        """Validate key"""
        key = "{}.{}".format(model, output)
        self.assertIn(key, data.keys())
        """Validate initial attributes"""
        value = data.get(key, {})
        values = value.keys()
        self.assertTrue(type(value) == dict)
        self.assertIn("id", values)
        self.assertIn("created_at", values)
        self.assertIn("updated_at", values)
        self.assertTrue("__class__", values)
        """Check attribute values"""
        self.assertEqual(value.get("id", None), output)
        self.assertEqual(value.get("__class__", None), model)

    def test_without_model(self):
        """without model"""
        output = self.output('create')
        expected = '** class name missing **\n'
        self.assertEqual(output, expected)

    def test_with_unknown_model(self):
        """With unknown model"""
        output = self.output("create Django")
        expected = "** class doesn't exist **\n"
        self.assertEqual(output, expected)

    def test_with_user_model(self):
        """with User model"""
        self.validModel("User")

    def test_with_base_model(self):
        """with BaseModel model"""
        self.validModel("BaseModel")


class TestShowCommand(unittest.TestCase):
    """
    Test show command
    """

    def setUp(self):
        """Reset storage object"""
        models.storage.clean()

    def tearDown(self):
        """Remove storage after every test"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def output(self, cmd):
        """Returns console output"""
        with patch('sys.stdout', new=StringIO()) as f:
            CMD().onecmd(cmd)
            return f.getvalue()

    def test_without_model(self):
        """test without model"""
        output = self.output("show")
        expected = "** class name missing **\n"
        self.assertEqual(output, expected)

    def test_with_invalid_model(self):
        """test with invalid model"""
        output = self.output("show MyModel")
        expected = "** class doesn't exist **\n"
        self.assertEqual(output, expected)

    def test_with_base_model_without_id(self):
        """test with BaseModel model no id"""
        expected = "** instance id missing **\n"
        output = self.output("show User")
        self.assertEqual(output, expected)
    
    def test_with_user_model_without_id(self):
        """test with User model no id"""
        expected = "** instance id missing **\n"
        output = self.output("show BaseModel")
        self.assertEqual(output, expected)
    
    def test_with_city_model_without_id(self):
        """test with City model no id"""
        expected = "** instance id missing **\n"
        output = self.output("show City")
        self.assertEqual(output, expected)
    
    def test_with_state_model_without_id(self):
        """test with State model no id"""
        expected = "** instance id missing **\n"
        output = self.output("show State")
        self.assertEqual(output, expected)
    
    def test_with_place_model_without_id(self):
        """test with Place model no id"""
        expected = "** instance id missing **\n"
        output = self.output("show Place")
        self.assertEqual(output, expected)
    
    def test_with_review_model_without_id(self):
        """test with Review model no id"""
        expected = "** instance id missing **\n"
        output = self.output("show Review")
        self.assertEqual(output, expected)
    
    def test_with_amenity_model_without_id(self):
        """test with Amenity model no id"""
        expected = "** instance id missing **\n"
        output = self.output("show Amenity")
        self.assertEqual(output, expected)

    def test_with_base_model_invalid_id(self):
        expected = "** no instance found **\n"
        output = self.output("show BaseModel 88888")
        self.assertEqual(output, expected)

    def test_with_user_model_invalid_id(self):
        expected = "** no instance found **\n"
        output = self.output("show User 88888")
        self.assertEqual(output, expected)

    def test_with_city_model_invalid_id(self):
        expected = "** no instance found **\n"
        output = self.output("show City 88888")
        self.assertEqual(output, expected)

    def test_with_state_model_invalid_id(self):
        expected = "** no instance found **\n"
        output = self.output("show State 88888")
        self.assertEqual(output, expected)

    def test_with_place_model_invalid_id(self):
        expected = "** no instance found **\n"
        output = self.output("show Place 88888")
        self.assertEqual(output, expected)

    def test_with_review_model_invalid_id(self):
        expected = "** no instance found **\n"
        output = self.output("show Review 88888")
        self.assertEqual(output, expected)

    def test_with_amenity_model_invalid_id(self):
        expected = "** no instance found **\n"
        output = self.output("show Amenity 88888")
        self.assertEqual(output, expected)

    def test_with_user_model_valid_id(self):
        user = User()
        cmd = "show User {}".format(user.id)
        output = (self.output(cmd)).strip('\n')
        expected = str(user)
        self.assertEqual(output, expected)
    
    def test_with_base_model_valid_id(self):
        base = BaseModel()
        cmd = "show BaseModel {}".format(base.id)
        output = (self.output(cmd)).strip('\n')
        expected = str(base)
        self.assertEqual(output, expected)

    def test_with_city_model_valid_id(self):
        city = City()
        cmd = "show City {}".format(city.id)
        output = (self.output(cmd)).strip('\n')
        expected = str(city)
        self.assertEqual(output, expected)

    def test_with_state_model_valid_id(self):
        state = State()
        cmd = "show State {}".format(state.id)
        output = (self.output(cmd)).strip('\n')
        expected = str(state)
        self.assertEqual(output, expected)

    def test_with_place_model_valid_id(self):
        place = Place()
        cmd = "show Place {}".format(place.id)
        output = (self.output(cmd)).strip('\n')
        expected = str(place)
        self.assertEqual(output, expected)

    def test_with_review_model_valid_id(self):
        review = Review()
        cmd = "show Review {}".format(review.id)
        output = (self.output(cmd)).strip('\n')
        expected = str(review)
        self.assertEqual(output, expected)

    def test_with_amenity_model_valid_id(self):
        amenity = Amenity()
        cmd = "show Amenity {}".format(amenity.id)
        output = (self.output(cmd)).strip('\n')
        expected = str(amenity)
        self.assertEqual(output, expected)
