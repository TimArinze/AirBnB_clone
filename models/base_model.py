#!/usr/bin/python3

"""base_model module contains the BaseModel class implementation"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """"BaseModel : a base class for common attributes and methods for futures
        classes"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for attr, value in kwargs.items():
                if attr == '__class__':
                    pass
                if attr in ['created_at', 'updated_at']:
                    setattr(self, attr, value)

    def __str__(self):
        """Readabe representation of an instance"""
        return "[Basemodel] ({}) {}".format(self.id, self.__dict__)

    def to_dict(self):
        instance_dict = self.__dict__

        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat('T')
        instance_dict['updated_at'] = self.updated_at.isoformat('T')
        return instance_dict

    def save(self):
        self.updated_at = datetime.now()
