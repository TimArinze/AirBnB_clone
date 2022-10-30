#!/usr/bin/python3


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