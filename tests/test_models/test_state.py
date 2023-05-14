#!/usr/bin/python3
"""Defines unittest classess for the State class"""

import unittest
import os
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """
    Represents Test Cases for State class
    """

    def setUp(self):
        """Sets up State class test methods."""
        pass

    def tearDown(self):
        """Tears down State class test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_create_new_instance_class(self):
        """Tests creation of new instance of State class."""
        my_model = State()
        self.assertIsInstance(my_model, State)
        self.assertTrue(issubclass(type(my_model), State))

    def test_create_new_instance_type(self):
        """Tests creation of new instance of State class."""
        my_model = State()
        instance_name = "<class 'models.state.State'>"
        self.assertEqual(str(type(my_model)), instance_name)

    def test_create_new_instance_subclass(self):
        """Tests creation of new instance of State class."""
        my_model = State()
        self.assertTrue(issubclass(type(my_model), BaseModel))

    def test_user_class_attributes(self):
        """Tests the attributes of State class."""
        attributes = storage.attributes()["State"]
        model = State()
        for key, value in attributes.items():
            self.assertTrue(hasattr(model, key))
            self.assertEqual(type(getattr(model, key, None)), value)


if __name__ == "__main__":
    unittest.main()
