#!/usr/bin/python3

<<<<<<< HEAD

"""
A class that serializes instances to a JSON file and deserializes
JSON file to instances
"""

import json


class FileStorage():
    """A class that serializes instances to a JSON file and deserializes"""


    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary """

        return FileStorage.__objects

    def new(self, obj):
        """ sets in __object with the key <obj class name>.id"""

        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj
	
    def save(self):
        """ serializes __objects to the JSON file """

        with open(FileStorage.__file_path, 'w', encoding='utf8') as f:
            new_dictionary = FileStorage.__objects
            for key, value in FileStorage.__objects.items():
                new_dictionary[key] = value.to_dict()
            json.dump(new_dictionary, f)
    
    def reload(self):
        """ deserializes the JSON file to __objects """

        try:
        	with open(FileStorage.__file_path, 'r', encoding='utf8') as f:
        		reloaded = json.load(f)
        		for value in reloaded.values():
        			name = value["__class__"]
        			del value["__class__"]
        			self.new(eval(name)(**value))
        			
        except FileNotFoundError:
        	return
=======
'''filestorage module contains the FileStorage class that serializes instances
    to a JSON file and deserializes JSON file to instances'''


from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State


all_cls = {
    "BaseModel":BaseModel,
    "User":User,
    "Review":Review,
    "Place":Place,
    "Amenity":Amenity,
    "City":City,
    "State":State
    }


class FileStorage:
    '''FileStorage : a class for manipulating objects from type object to JSON
        format and vice-versa'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns the dictionary `__objects`'''
        return self.__objects

    def new(self, obj):
        '''Sets in `__objects` the `obj` with the key `<obj class name>.id`'''
        attr = obj.__class__.__name__ + '.' + obj.id
        self.__objects[attr] = obj

    def save(self):
        '''Serializes `__objects` to the JSON file (path: `__file_path`)'''
        to_json = dict()
        for key, value in FileStorage.__objects.items():
            to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            from json import dump
            dump(to_json, f)

    def reload(self):
        """Deserializes the JSON file `__file_path` to `__objects`,
            if it exists."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                from json import load
                loaded_obj = load(f)
                for i in loaded_obj:
                    self.__objects[i] =\
                        all_cls[loaded_obj[i]["__class__"]](**loaded_obj[i])
        except Exception:
            return





















>>>>>>> black
