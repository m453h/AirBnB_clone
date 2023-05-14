#!/usr/bin/python3
"""
Defines unittest classess for the TestFileStorage class
"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os


class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tears down test methods for the TestFileStorage."""
        self.resetStorage()
        pass

    def test_filestorage_init(self):
        """Tests initialization of FileStorage class."""
        storage = FileStorage()
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_filestorage_init_with_no_args(self):
        """Tests initialization of FileStorage class with no arguments."""
        with self.assertRaises(TypeError):
            FileStorage.__init__()

    def test_filestorage_init_with_multi_args(self):
        """Tests initialization of FileStorage class with multiple arguments."""
        FileStorage.__init__(200, "School", "ALX", "Python", "C")

    def test_create_new_instance_class(self):
        """Tests creation of new instance of FileStorage class."""
        my_model = FileStorage()
        self.assertIsInstance(my_model, FileStorage)
        self.assertTrue(issubclass(type(my_model), FileStorage))

    def test_create_new_instance_type(self):
        """Tests creation of new instance of FileStorage class."""
        my_model = FileStorage()
        instance_name = "<class 'models.engine.file_storage.FileStorage'>"
        self.assertEqual(str(type(my_model)), instance_name)

    def test_create_new_instance_subclass(self):
        """Tests creation of new instance of FileStorage class."""
        my_model = FileStorage()
        self.assertTrue(issubclass(type(my_model), FileStorage))

    def test_class_attributes(self):
        """Tests FileStorage class attributes."""
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

if __name__ == '__main__':
    unittest.main()
