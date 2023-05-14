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
        """
        Tests initialization of FileStorage class with multiple arguments.
        """
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

    def helper_file_storage_save(self, classname):
        """Helper method to test for save() method of the FileStorage class."""
        cls = storage.classes().get(classname)
        if cls is None:
            raise ValueError(f"Invalid classname '{classname}'")
        obj = cls()
        storage.new(obj)
        key = f"{type(obj).__name__}.{obj.id}"
        storage.save()
        file_path = FileStorage._FileStorage__file_path
        self.assertTrue(os.path.isfile(file_path))
        with open(file_path, "r", encoding="utf-8") as file:
            file_contents = file.read()
            self.assertIn(key, file_contents)
            self.assertIn('"created_at":', file_contents)
            self.assertIn('"updated_at":', file_contents)
            expected_dict = {key: obj.to_dict()}
            actual_dict = json.loads(file_contents)
            self.assertEqual(actual_dict, expected_dict)

    def test_save_base_model(self):
        """Tests save() method for BaseModel class."""
        self.helper_file_storage_save("BaseModel")

    def test_save_user_class(self):
        """Tests save() method for User class."""
        self.helper_file_storage_save("User")

    def test_save_state_class(self):
        """Tests save() method for State class."""
        self.helper_file_storage_save("State")

    def test_save_city_class(self):
        """Tests save() method for City class."""
        self.helper_file_storage_save("City")

    def test_save_amenity_class(self):
        """Tests save() method for Amenity class."""
        self.helper_file_storage_save("Amenity")

    def test_save_place_class(self):
        """Tests save() method for Place class."""
        self.helper_file_storage_save("Place")

    def test_save_review_class(self):
        """Tests save() method for Review class."""
        self.helper_file_storage_save("Review")

    def helper_test_new(self, classname):
        """Helper method to test for new() method of the FileStorage class."""
        cls = storage.classes().get(classname)
        if cls is None:
            raise ValueError(f"Invalid classname '{classname}'")
        obj = cls()
        storage.new(obj)
        key = f"{type(obj).__name__}.{obj.id}"
        objects_dict = FileStorage._FileStorage__objects
        self.assertIn(key, objects_dict)
        self.assertIs(objects_dict[key], obj)

    def test_new_base_model(self):
        """Tests new() method for BaseModel class."""
        self.helper_test_new("BaseModel")

    def test_new_user(self):
        """Tests new() method for User class."""
        self.helper_test_new("User")

    def test_new_state(self):
        """Tests new() method for State class."""
        self.helper_test_new("State")

    def test_new_city(self):
        """Tests new() method for City class."""
        self.helper_test_new("City")

    def test_new_amenity(self):
        """Tests new() method for Amenity class."""
        self.helper_test_new("Amenity")

    def test_new_place(self):
        """Tests new() method for Place class."""
        self.helper_test_new("Place")

    def test_new_review(self):
        """Tests new() method for Review class."""
        self.helper_test_new("Review")


if __name__ == '__main__':
    unittest.main()
