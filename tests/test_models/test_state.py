#!/usr/bin/python3
'''test_state module'''


import unittest
import datetime
from models.base_model import BaseModel
from models.state import State
import uuid


class TestState(unittest.TestCase):
    """Never trust State/Builder inputs"""
    @classmethod
    def setUpClass(self):
        """Prepraring test cases"""
        self.my_state = State()
        self.tmp = self.my_state.updated_at
        self.maxDiff = None

    def test_isinstance_of_State(self):
        """Test class of an instance"""
        self.assertIsInstance(self.my_state, State)
        self.assertTrue(issubclass(self.my_state.__class__, BaseModel))

    def test_id_attribute(self):
        """All individual tests for id attribute"""

        '''Testing if `id` is a public attribute'''
        self.assertIn('id', dir(self.my_state))
        self.assertIn('id', self.my_state.__dict__)

        '''Testing if `id` is callable member'''
        with self.assertRaises(TypeError):
            self.my_state.id()
        """Testing current type of id"""
        self.assertIsInstance(self.my_state.id, str)

        """This test is for the format of id"""
        with self.assertRaises(ValueError):
            string = 'hello'
            self.my_state.id = string
            """ID Pattern Testing
                Using uuid.UUID function return the uuid object that gives this
                string."""
            uuid.UUID(self.my_state.id)
        '''Testing if `id` is really an attribute'''
        with self.assertRaises(TypeError):
            self.my_state.id()

    def test_created_at_attribute(self):
        """All individual tests for created_at attribute"""

        '''Testing if `created_at` is a public attribute'''
        self.assertIn('created_at', dir(self.my_state))

        '''Testing if `created_at` is callable member'''
        with self.assertRaises(TypeError):
            self.my_state.created_at()

        """Testing type of created_at"""
        self.assertIsInstance(self.my_state.created_at, datetime.datetime)

    def test_updated_at_attribute(self):
        """All individual tests for updated_at attribute"""

        '''Testing if `updated_at` is a public attribute'''
        self.assertIn('updated_at', dir(self.my_state))
        self.assertIn('updated_at', self.my_state.__dict__)

        '''Testing if `updated_at` is callable member'''
        with self.assertRaises(TypeError):
            self.my_state.updated_at()

        """Testing type of updated_at"""
        self.assertIsInstance(self.my_state.updated_at, datetime.datetime)

    def test_name_attribute(self):
        """All individual tests for name attribute"""

        '''Testing if `name` is a public attribute'''
        self.assertIn('name', dir(self.my_state))
        self.assertNotIn('name', self.my_state.__dict__)

        self.my_state.name = "Senegal"
        self.assertIn('name', self.my_state.__dict__)

        '''Testing if `name` is callable member'''
        with self.assertRaises(TypeError):
            self.my_state.name()

    def test_to_dict(self):
        """All tests for to_dict method"""

        '''Testing if `to_dict` is a member'''
        self.assertIn('to_dict', dir(State))

        the_dict = self.my_state.to_dict()
        """Testing if to_dict return a dictionary object"""
        self.assertIs(type(the_dict), dict)

        """Testing expected attribute returned by to_dict"""
        attrs = ['__class__', 'created_at', 'updated_at', 'id']
        for attr in attrs:
            self.assertIn(attr, the_dict)
            self.assertIs(type(attr), str)

    def test_based_from_dictionary(self):
        '''Testing instanciation from a previous instance'''
        the_dict = self.my_state.to_dict()
        my_other_model = State(**the_dict)
        self.assertEqual(self.my_state.__dict__, my_other_model.__dict__)
        self.assertEqual(self.my_state.to_dict(), my_other_model.to_dict())

    def test_save(self):
        """All tests for save method"""

        '''Testing if save is a method of State'''
        self.assertIn('save', dir(State))
        self.my_state.save()
        '''Testing if updated_at changes when calling save method'''
        self.assertNotEqual(self.tmp, self.my_state.updated_at)

    def test_str_representation(self):
        """All tests for string representation"""

        '''Testing if __str__ is defined in State'''
        self.assertIn('__str__', dir(State))
        class_name = self.my_state.__class__.__name__
        my_state_id = self.my_state.id
        my_state_created_at = repr(self.my_state.created_at)
        my_state_updated_at = repr(self.my_state.updated_at)
        s = self.my_state.__str__()
        self.assertIn("[{}] ({})".format(class_name, my_state_id), s)
        self.assertIn("'id': '{}'".format(my_state_id), s)
        self.assertIn("'created_at': " + my_state_created_at, s)
        self.assertIn("'updated_at': " + my_state_updated_at, s)
        self.assertIn("'name': '{}'".format(self.my_state.name), s)


if __name__ == '__main__':
    unittest.main(verbosity=2)
