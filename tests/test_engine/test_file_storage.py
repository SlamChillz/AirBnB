#!/usr/bin/python3
"""
This module is designed to test the base model
"""
import unittest
from unittest.mock import patch
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Class to define the unittest
    """

    def test_base(self):
        """
        Test the FileStorage class
        """
