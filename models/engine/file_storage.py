#!/usr/bin/python3


"""
A class that serializes instances to a JSON file and deserializes
JSON file to instances
"""

import json


class FileStorage():
    """A class that serializes instances to a JSON file and deserializes"""

    __file_path = 'file.JSON'
    __objects = {}

    def all(self):
        """ returns dictionary of __objects """
        return __objects

    def new(self, obj):
        """ sets the objects """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file(path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value
        with open('file.JSON', 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file if it exists otherwise do nothing"""
        if 'file.JSON':
            self.__objects = open('file.JSON')
            self.__objects = json.load(self.__objects)
        else:
            return
