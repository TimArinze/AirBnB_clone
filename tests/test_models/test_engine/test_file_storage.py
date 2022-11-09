#!/usr/bin/python3
'''test_file_storage module'''
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State


hbnb_cls = {
    "BaseModel": BaseModel,
    "User": User,
    "Review": Review,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "State": State
    }


class TestFileStorage(unittest.TestCase):
    """This is a set of test for the file_storage module"""

    @classmethod
    def setUpClass(self):
        """Prepraring test cases"""
        self.fs = FileStorage()
        self.new_fs = FileStorage()

    @classmethod
    def tearDownClass(self):
        if os.path.isfile(self.fs._FileStorage__file_path):
            os.remove(self.fs._FileStorage__file_path)
        self.fs._FileStorage__objects = {}

    def test_isinstance_of_FileStorage(self):
        """Test class of an instance"""
        self.assertIsInstance(self.fs, FileStorage)

    def test__file_path_atribute(self):
        """All individual tests for __file_path attribute"""

        """Testing if an instance has the __file_path attribute"""
        self.assertTrue(hasattr(self.fs, '_FileStorage__file_path'))

        '''Testing if `__file_path` is a public member'''
        self.assertIn('_FileStorage__file_path', dir(self.fs))
        self.assertNotIn('_FileStorage__file_path', self.fs.__dict__)

        '''Testing if `__file_path` is callable member'''
        with self.assertRaises(TypeError):
            self.fs._FileStorage__file_path()

        '''Testing if `__file_path` already exists'''
        self.assertFalse(os.path.isfile(self.fs._FileStorage__file_path))

        with self.assertRaises(FileNotFoundError):
            with open(self.fs._FileStorage__file_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    print(line)

        """Testing current type of __file_path attribute"""
        self.assertIsInstance(self.fs._FileStorage__file_path, str)

        """Testing if the file name is `file.json`"""
        self.assertTrue(self.fs._FileStorage__file_path == 'file.json')

    def test__objects_atribute(self):
        """All individual tests for __objects attribute"""

        """Testing if an instance automatically has the __objects attribute"""
        self.assertTrue(hasattr(self.fs, '_FileStorage__objects'))

        '''Testing if `__objects` is a public attribute'''
        self.assertIn('_FileStorage__objects', dir(self.fs))
        self.assertNotIn('_FileStorage__objects', self.fs.__dict__)

        '''Testing if `__objects` is callable member'''
        with self.assertRaises(TypeError):
            self.fs._FileStorage__objects()

        """Testing current type of __objects attribute"""
        self.assertIsInstance(self.fs._FileStorage__objects, dict)

        '''Testing if `__objects` is empty'''
        self.assertTrue(self.fs._FileStorage__objects == {})

    def test_all(self):
        """All individual tests for `all` method"""

        """Testing if an instance automatically has the new member"""
        self.assertTrue(hasattr(self.fs, 'all'))

        '''Testing more than 1 argument passed'''
        with self.assertRaises(TypeError):
            self.fs.all(1, True)

        '''Testing type of calling all method'''
        self.assertTrue(type(self.fs.all()) == dict)

        '''Testing if `__objects` is empty'''
        self.assertTrue(self.fs.all() == {})

    def test_new(self):
        """All individual tests for `new` method"""

        """Testing if an instance automatically has the new member"""
        self.assertTrue(hasattr(self.fs, 'new'))

        '''Testing missing 1 argument'''
        with self.assertRaises(TypeError):
            self.fs.new()

        '''Testing more than 1 argument passed'''
        with self.assertRaises(TypeError):
            self.fs.new(1, True)

        '''Testing if argument of new is an instance BaseModel or subclass'''
        with self.assertRaises(AttributeError):
            values_test = [1, .1, 'string', [1, 2], {'n1': 1}, True, None]
            for v in values_test:
                self.assertFalse(hasattr(v, 'id'))
                self.fs.new(v)
        inst = ''
        for k in hbnb_cls:
            inst = hbnb_cls[k]()
            self.assertTrue(hasattr(inst, 'id'))
            self.assertTrue(hasattr(inst, '__class__'))
            self.assertTrue(issubclass(inst.__class__, BaseModel))

        '''Testing type of calling all method'''
        self.assertTrue(type(self.fs.all()) == dict)

        '''Testing if `__objects` is not empty'''
        self.assertTrue(self.fs.all() != {})

    def test_save(self):
        """All individual tests for save member"""

        """Testing if an instance automatically has the save member"""
        self.assertTrue(hasattr(self.fs, 'save'))

        '''Testing more than 1 argument passed'''
        with self.assertRaises(TypeError):
            self.fs.save(1, True)

        '''Testing if `save` is a public member of the instance'''
        self.assertIn('save', dir(self.fs))
        self.assertNotIn('save', self.fs.__dict__)

        self.fs.save()
        '''Testing if `__file_path` exists'''
        self.assertTrue(os.path.isfile(self.fs._FileStorage__file_path))
        self.assertTrue(os.stat(self.fs._FileStorage__file_path).st_size != 0)

    def test_reload(self):
        """All individual tests for reload member"""

        """Testing if an instance automatically has the reload member"""
        self.assertTrue(hasattr(self.fs, 'reload'))

        '''Testing more than 1 argument passed'''
        with self.assertRaises(TypeError):
            self.fs.new(1, True)

        '''Testing if `__objects` is not empty'''
        self.fs.reload()
        self.assertTrue(self.fs._FileStorage__objects != {})


if __name__ == '__main__':
    unittest.main(verbosity=2)
