#!/usr/bin/python3
"""Defines unittest classess for the City class"""

import unittest
import os
from models.city import City
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """
    Represents Test Cases for City class
    """

    def setUp(self):
        """Sets up City class test methods."""
        pass

    def tearDown(self):
        """Tears down City class test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_create_new_instance_class(self):
        """Tests creation of new instance of City class."""
        my_model = City()
        self.assertIsInstance(my_model, City)
        self.assertTrue(issubclass(type(my_model), City))

    def test_create_new_instance_type(self):
        """Tests creation of new instance of City class."""
        my_model = City()
        instance_name = "<class 'models.city.City'>"
        self.assertEqual(str(type(my_model)), instance_name)

    def test_create_new_instance_subclass(self):
        """Tests creation of new instance of City class."""
        my_model = City()
        self.assertTrue(issubclass(type(my_model), BaseModel))

    def test_user_class_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        model = City()
        for key, value in attributes.items():
            self.assertTrue(hasattr(model, key))
            self.assertEqual(type(getattr(model, key, None)), value)


if __name__ == "__main__":
    unittest.main()
