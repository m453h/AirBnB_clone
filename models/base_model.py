#!/usr/bin/python3
"""This module creates the base model for the AirBnb Clone project"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """
    Represents the Base Class in which all classes
    the AirBnb clone project will inherit from
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method to initialize the instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns the string representation of BaseModel instance
        """

        return "[{}] ({}) {}".format(
            type(self).__name__,
            self.id,
            self.__dict__)

    def save(self):
        """
        Method to update the instance attribute: updated_at
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary that contains all keys/values of __dict__
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
