#!/usr/bin/python3
"""Defines unittest classess for the Amenity class"""

import unittest
import os
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """
    Represents Test Cases for Amenity class
    """

    def setUp(self):
        """Sets up Amenity class test methods."""
        pass

    def tearDown(self):
        """Tears down Amenity class test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_create_new_instance_class(self):
        """Tests creation of new instance of Amenity class."""
        my_model = Amenity()
        self.assertIsInstance(my_model, Amenity)
        self.assertTrue(issubclass(type(my_model), Amenity))

    def test_create_new_instance_type(self):
        """Tests creation of new instance of Amenity class."""
        my_model = Amenity()
        instance_name = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(my_model)), instance_name)

    def test_create_new_instance_subclass(self):
        """Tests creation of new instance of Amenity class."""
        my_model = Amenity()
        self.assertTrue(issubclass(type(my_model), BaseModel))

    def test_user_class_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        model = Amenity()
        for key, value in attributes.items():
            self.assertTrue(hasattr(model, key))
            self.assertEqual(type(getattr(model, key, None)), value)


if __name__ == "__main__":
    unittest.main()
