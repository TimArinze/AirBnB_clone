#!/usr/bin/env bash

""" BaseModel that defines all common attributes/methods for other classes """

import uuid
from datetime import datetime


class BaseModel():
    """ Base Model """

    def __init__(self, *args, **kwargs):
        """initialization of the class"""
        if kwargs is not None:
            self.__dict__.update(kwargs)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """__str__"""
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """save"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dictionary = self.__dict__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
