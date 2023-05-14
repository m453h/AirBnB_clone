#!/usr/bin/python3
"""Defines unittest classess for the Review class"""

import unittest
import os
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """
    Represents Test Cases for Review class
    """

    def setUp(self):
        """Sets up Review class test methods."""
        pass

    def tearDown(self):
        """Tears down Review class test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_create_new_instance_class(self):
        """Tests creation of new instance of Review class."""
        my_model = Review()
        self.assertIsInstance(my_model, Review)
        self.assertTrue(issubclass(type(my_model), Review))

    def test_create_new_instance_type(self):
        """Tests creation of new instance of Review class."""
        my_model = Review()
        instance_name = "<class 'models.review.Review'>"
        self.assertEqual(str(type(my_model)), instance_name)

    def test_create_new_instance_subclass(self):
        """Tests creation of new instance of Review class."""
        my_model = Review()
        self.assertTrue(issubclass(type(my_model), BaseModel))

    def test_user_class_attributes(self):
        """Tests the attributes of Review class."""
        attributes = storage.attributes()["Review"]
        model = Review()
        for key, value in attributes.items():
            self.assertTrue(hasattr(model, key))
            self.assertEqual(type(getattr(model, key, None)), value)


if __name__ == "__main__":
    unittest.main()
