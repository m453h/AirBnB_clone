#!/usr/bin/python3
"""
Defines unittest classess for the BaseModel class
"""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid


class TestBaseModel(unittest.TestCase):

    """
    Represents Test Cases for BaseModel class
    """

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_create_new_instance_class(self):
        """Tests creation of new instance of BaseModel class."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(issubclass(type(my_model), BaseModel))

    def test_create_new_instance_type(self):
        """Tests creation of new instance of BaseModel class."""
        my_model = BaseModel()
        instance_name = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(my_model)), instance_name)

    def test_create_new_instance_subclass(self):
        """Tests creation of new instance of BaseModel class."""
        my_model = BaseModel()
        self.assertTrue(issubclass(type(my_model), BaseModel))

    def test_init_with_no_args(self):
        with self.assertRaises(TypeError):
            BaseModel.__init__()

    def test_init_with_multiple_args(self):
        """Tests __init__ with multiple arguments."""
        args = [i for i in range(9999)]
        model = BaseModel(0, 2, 4, 6, 8, 10, 12)
        model = BaseModel(*args)
        model = BaseModel("zero", "one", "two", "three")

    def test_init_with_kwargs(self):
        """Tests creation of new instance with **kwargs from JSON."""
        my_model = BaseModel()
        my_model.shape = "Circle"
        my_model.radius = 7
        my_model.colour = "blue"
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_init_from_dict(self):
        """Tests creation of new instance with **kwargs from dict."""
        data = {"__class__": "BaseModel",
                "updated_at": datetime.now().isoformat(),
                "created_at": datetime.now().isoformat(),
                "id": uuid.uuid4(),
                "name": "circle",
                "radius": 7,
                "constant": 3.14}
        model = BaseModel(**data)
        self.assertEqual(model.to_dict(), data)

    def test_base_model_attributes(self):
        """Tests attributes value for instance of a BaseModel class."""
        attributes = storage.attributes()["BaseModel"]
        model = BaseModel()
        for key, value in attributes.items():
            self.assertTrue(hasattr(model, key))
            self.assertEqual(type(getattr(model, key, None)), value)

    def test_base_model_time_of_creation(self):
        """Tests if updated_at/created_at attributes are correct."""
        date_now = datetime.now()
        b = BaseModel()
        time_difference = b.updated_at - b.created_at
        self.assertTrue(abs(time_difference.total_seconds()) < 0.01)
        time_difference = b.created_at - date_now
        self.assertTrue(abs(time_difference.total_seconds()) < 0.1)

    def test_base_model_unique_ids(self):
        """Tests for unique BaseModel unique ids."""
        ids = []
        for i in range(9999):
            ids.append(BaseModel().id)
        self.assertEqual(len(set(ids)), len(ids))

    def test_base_model_save(self):
        """Tests the save() BaseModel method."""
        model = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        model.save()
        diff = model.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_storage_save(self):
        """Tests that storage.save() method works as intended"""
        m = BaseModel()
        m.save()
        key = "{}.{}".format(type(m).__name__, m.id)
        expected_dict = {key: m.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            file_contents = f.read()
            self.assertIn(key, file_contents)
            self.assertIn(m.id, file_contents)
            self.assertIn('"created_at":', file_contents)
            self.assertIn('"updated_at":', file_contents)
            actual_dict = json.loads(file_contents)
            self.assertEqual(actual_dict, expected_dict)

    def test_save_with_no_args(self):
        """Tests calling save() method with no arguments."""
        with self.assertRaises(TypeError):
            BaseModel.save()

    def test_save_with_extra_args(self):
        """Tests calling save() with too many arguments."""
        with self.assertRaises(TypeError):
            BaseModel.save(self, 1001, 23)

    def test_base_model_str(self):
        """Tests calling __str__ BaseModel method."""
        m = BaseModel()
        expected_str = f"[BaseModel] ({m.id}) {m.__dict__}"
        self.assertEqual(str(m), expected_str)

    def test_base_model_to_dict(self):
        """Tests the to_dict() BaseModel method."""
        m = BaseModel()
        m.width = 8
        m.height = 12
        d = m.to_dict()
        self.assertEqual(d["id"], m.id)
        self.assertEqual(d["__class__"], type(m).__name__)
        self.assertEqual(d["created_at"], m.created_at.isoformat())
        self.assertEqual(d["updated_at"], m.updated_at.isoformat())
        self.assertEqual(d["width"], m.width)
        self.assertEqual(d["height"], m.height)

    def test_base_model_to_dict_with_no_args(self):
        """Tests to_dict() with no arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()

    def test_base_model_to_dict_with_extra_args(self):
        """Tests to_dict() with extra arguments."""
        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict(self, 98)


if __name__ == '__main__':
    unittest.main()
