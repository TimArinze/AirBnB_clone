#!/usr/bin/python3
"""base_model module contains the BaseModel class implementation"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """"BaseModel : a base class for common attributes and methods for futures
        classes"""

    def __init__(self, *args, **kwargs):
        '''Initializes an new instance with an optional dictionary of a
            previous instance passed to `kwargs`'''
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            for attr, value in kwargs.items():
                if attr != '__class__':
                    if attr in ['created_at', 'updated_at']:
                        fmt = "%Y-%m-%dT%H:%M:%S.%f"
                        value = datetime.strptime(value, fmt)
                        setattr(self, attr, value)
                    setattr(self, attr, value)

    def __str__(self):
        """Readabe representation of an instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """Beautifies and returns the dictionary of an instance"""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

    def save(self):
        """Indicates when the instance is last used before adding (again)
            it in the JSON file"""
        self.updated_at = datetime.now()
        models.storage.save()