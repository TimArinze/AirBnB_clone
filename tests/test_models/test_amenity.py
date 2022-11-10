#!/usr/bin/python3
'''test_amenity module'''


import unittest
import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
import uuid


class TestAmenity(unittest.TestCase):
    """Never trust Amenity/Builder inputs"""
    @classmethod
    def setUpClass(self):
        """Prepraring test cases"""
        self.my_amenity = Amenity()
        self.tmp = self.my_amenity.updated_at
        self.maxDiff = None

    def test_isinstance_of_Amenity(self):
        """Test class of an instance"""
        self.assertIsInstance(self.my_amenity, Amenity)
        self.assertTrue(issubclass(self.my_amenity.__class__, BaseModel))

    def test_id_attribute(self):
        """All individual tests for id attribute"""

        '''Testing if `id` is a public attribute'''
        self.assertIn('id', dir(self.my_amenity))
        self.assertIn('id', self.my_amenity.__dict__)

        '''Testing if `id` is callable member'''
        with self.assertRaises(TypeError):
            self.my_amenity.id()
        """Testing current type of id"""
        self.assertIsInstance(self.my_amenity.id, str)

        """This test is for the format of id"""
        with self.assertRaises(ValueError):
            string = 'hello'
            self.my_amenity.id = string
            """ID Pattern Testing
                Using uuid.UUID function return the uuid object that gives this
                string."""
            uuid.UUID(self.my_amenity.id)
        '''Testing if `id` is really an attribute'''
        with self.assertRaises(TypeError):
            self.my_amenity.id()

    def test_created_at_attribute(self):
        """All individual tests for created_at attribute"""

        '''Testing if `created_at` is a public attribute'''
        self.assertIn('created_at', dir(self.my_amenity))

        '''Testing if `created_at` is callable member'''
        with self.assertRaises(TypeError):
            self.my_amenity.created_at()

        """Testing type of created_at"""
        self.assertIsInstance(self.my_amenity.created_at, datetime.datetime)

    def test_updated_at_attribute(self):
        """All individual tests for updated_at attribute"""

        '''Testing if `updated_at` is a public attribute'''
        self.assertIn('updated_at', dir(self.my_amenity))
        self.assertIn('updated_at', self.my_amenity.__dict__)

        '''Testing if `updated_at` is callable member'''
        with self.assertRaises(TypeError):
            self.my_amenity.updated_at()

        """Testing type of updated_at"""
        self.assertIsInstance(self.my_amenity.updated_at, datetime.datetime)

    def test_name_attribute(self):
        """All individual tests for name attribute"""

        '''Testing if `name` is a public attribute'''
        self.assertIn('name', dir(self.my_amenity))
        self.assertNotIn('name', self.my_amenity.__dict__)

        self.my_amenity.name = "Hobbyist Tech"
        self.assertIn('name', self.my_amenity.__dict__)

        '''Testing if `name` is callable member'''
        with self.assertRaises(TypeError):
            self.my_amenity.name()

    def test_to_dict(self):
        """All tests for to_dict method"""

        '''Testing if `to_dict` is a member'''
        self.assertIn('to_dict', dir(Amenity))

        the_dict = self.my_amenity.to_dict()
        """Testing if to_dict return a dictionary object"""
        self.assertIs(type(the_dict), dict)

        """Testing expected attribute returned by to_dict"""
        attrs = ['__class__', 'created_at', 'updated_at', 'id']
        for attr in attrs:
            self.assertIn(attr, the_dict)
            self.assertIs(type(attr), str)

    def test_based_from_dictionary(self):
        '''Testing instanciation from a previous instance'''
        the_dict = self.my_amenity.to_dict()
        my_other_model = Amenity(**the_dict)
        self.assertEqual(self.my_amenity.__dict__, my_other_model.__dict__)
        self.assertEqual(self.my_amenity.to_dict(), my_other_model.to_dict())

    def test_save(self):
        """All tests for save method"""

        '''Testing if save is a method of Amenity'''
        self.assertIn('save', dir(Amenity))
        self.my_amenity.save()
        '''Testing if updated_at changes when calling save method'''
        self.assertNotEqual(self.tmp, self.my_amenity.updated_at)

    def test_str_representation(self):
        """All tests for string representation"""

        '''Testing if __str__ is defined in Amenity'''
        self.assertIn('__str__', dir(Amenity))
        class_name = self.my_amenity.__class__.__name__
        my_amenity_id = self.my_amenity.id
        my_amenity_created_at = repr(self.my_amenity.created_at)
        my_amenity_updated_at = repr(self.my_amenity.updated_at)
        s = self.my_amenity.__str__()
        self.assertIn("[{}] ({})".format(class_name, my_amenity_id), s)
        self.assertIn("'id': '{}'".format(my_amenity_id), s)
        self.assertIn("'created_at': " + my_amenity_created_at, s)
        self.assertIn("'updated_at': " + my_amenity_updated_at, s)
        self.assertIn("'name': '{}'".format(self.my_amenity.name), s)


if __name__ == '__main__':
    unittest.main(verbosity=2)
