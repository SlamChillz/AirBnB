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

from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
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
        FileStorage._FileStorage__objects = {}

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
        print(value)
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
        """"""
