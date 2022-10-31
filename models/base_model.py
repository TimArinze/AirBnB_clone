#!/usr/bin/python3


""" BaseModel that defines all common attributes/methods for other classes """


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Base Model """

    def __init__(self, *args, **kwargs):
        """initialization of the class"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """__str__"""
        cls = __class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """save"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
