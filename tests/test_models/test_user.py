#!/usr/bin/python3
'''test_user module'''


import unittest
import datetime
from models.base_model import BaseModel
from models.user import User
import uuid


class TestUser(unittest.TestCase):
    """Never trust User/Builder inputs"""

    def setUp(self):
        """Prepraring test cases"""
        self.my_user = User()
        self.tmp = self.my_user.updated_at
        self.id = self.my_user.id
        self.maxDiff = None

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_isinstance_of_User(self):
        """Test class of an instance"""
        self.assertIsInstance(self.my_user, User)
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel))

    def test_id_attribute(self):
        """All individual tests for id attribute"""

        '''Testing if `id` is a public attribute'''
        self.assertIn('id', dir(self.my_user))
        self.assertIn('id', self.my_user.__dict__)

        '''Testing if `id` is callable member'''
        with self.assertRaises(TypeError):
            self.my_user.id()
        """Testing current type of id"""
        self.assertIsInstance(self.my_user.id, str)

        """This test is for the format of id"""
        with self.assertRaises(ValueError):
            string = 'hello'
            self.my_user.id = string
            """ID Pattern Testing
                Using uuid.UUID function return the uuid object that gives this
                string."""
            uuid.UUID(self.my_user.id)
        '''Testing if `id` is really an attribute'''
        with self.assertRaises(TypeError):
            self.my_user.id()
        self.my_user.id = self.id

    def test_created_at_attribute(self):
        """All individual tests for created_at attribute"""

        '''Testing if `created_at` is a public attribute'''
        self.assertIn('created_at', dir(self.my_user))

        '''Testing if `created_at` is callable member'''
        with self.assertRaises(TypeError):
            self.my_user.created_at()

        """Testing type of created_at"""
        self.assertIsInstance(self.my_user.created_at, datetime.datetime)

    def test_updated_at_attribute(self):
        """All individual tests for updated_at attribute"""

        '''Testing if `updated_at` is a public attribute'''
        self.assertIn('updated_at', dir(self.my_user))
        self.assertIn('updated_at', self.my_user.__dict__)

        '''Testing if `updated_at` is callable member'''
        with self.assertRaises(TypeError):
            self.my_user.updated_at()

        """Testing type of updated_at"""
        self.assertIsInstance(self.my_user.updated_at, datetime.datetime)

    def test_email_attribute(self):
        """All individual tests for email attribute"""

        '''Testing if `email` is a public attribute'''
        self.assertIn('email', dir(User))
        self.assertNotIn('email', self.my_user.__dict__)

        '''Testing type of `email`'''
        self.assertTrue(type(self.my_user.email) == str)

        self.my_user.email = "black@email.com"
        self.assertIn('email', self.my_user.__dict__)

        '''Testing if `email` is callable member'''
        with self.assertRaises(TypeError):
            self.my_user.email()

    def test_password_attribute(self):
        """All individual tests for password attribute"""

        '''Testing if `password` is a public attribute'''
        self.assertIn('password', dir(User))
        self.assertNotIn('password', self.my_user.__dict__)

        '''Testing type of `password`'''
        self.assertTrue(type(self.my_user.password) == str)

        self.my_user.password = "pswrd"
        self.assertIn('password', self.my_user.__dict__)

        '''Testing if `password` is callable member'''
        with self.assertRaises(TypeError):
            self.my_user.password()

    def test_first_name_attribute(self):
        """All individual tests for first_name attribute"""

        '''Testing if `first_name` is a public attribute'''
        self.assertIn('first_name', dir(User))
        self.assertNotIn('first_name', self.my_user.__dict__)

        '''Testing type of `first_name`'''
        self.assertTrue(type(self.my_user.first_name) == str)

        self.my_user.first_name = "BLACK"
        self.assertIn('first_name', self.my_user.__dict__)

        '''Testing if `first_name` is callable member'''
        with self.assertRaises(TypeError):
            self.my_user.first_name()

    def test_last_name_attribute(self):
        """All individual tests for last_name attribute"""

        '''Testing if `last_name` is a public attribute'''
        self.assertIn('last_name', dir(self.my_user))
        self.assertNotIn('last_name', self.my_user.__dict__)

        '''Testing type of `last_name`'''
        self.assertTrue(type(self.my_user.last_name) == str)

        self.my_user.last_name = "MIGHT"
        self.assertIn('last_name', self.my_user.__dict__)

        '''Testing if `last_name` is callable member'''
        with self.assertRaises(TypeError):
            self.my_user.last_name()

    def test_to_dict(self):
        """All tests for to_dict method"""

        '''Testing if `to_dict` is a member'''
        self.assertIn('to_dict', dir(User))

        the_dict = self.my_user.to_dict()
        """Testing if to_dict return a dictionary object"""
        self.assertIs(type(the_dict), dict)

        """Testing expected attribute returned by to_dict"""
        attrs = ['__class__', 'created_at', 'updated_at', 'id']
        for attr in attrs:
            self.assertIn(attr, the_dict)
            self.assertIs(type(attr), str)

    def test_based_from_dictionary(self):
        '''Testing instanciation from a previous instance'''
        the_dict = self.my_user.to_dict()
        my_other_user = User(**the_dict)
        self.assertEqual(self.my_user.__dict__, my_other_model.__dict__)
        self.assertEqual(self.my_user.to_dict(), my_other_model.to_dict())

    def test_save(self):
        """All tests for save method"""

        '''Testing if save is a method of User'''
        self.assertIn('save', dir(User))
        self.my_user.save()
        '''Testing if updated_at changes when calling save method'''
        self.assertNotEqual(self.tmp, self.my_user.updated_at)

        '''Testing if the instance is save in the file storage'''
        key = self.my_user.__class__.__name__ + '.' + self.my_user.id
        with open('file.json', 'r') as f:
            from json import load
            json_obj = load(f)
            self.assertEqual(json_obj[key], self.my_user.to_dict())


    def test_str_representation(self):
        """All tests for string representation"""

        '''Testing if __str__ is defined in User'''
        self.assertIn('__str__', dir(User))
        class_name = self.my_user.__class__.__name__
        my_user_id = self.my_user.id
        my_user_created_at = repr(self.my_user.created_at)
        my_user_updated_at = repr(self.my_user.updated_at)
        self.my_user.email = "black@email.com"
        self.my_user.password = "pswrd"
        self.my_user.first_name = "BLACK"
        self.my_user.last_name = "MIGHT"
        s = self.my_user.__str__()
        self.assertIn("[{}] ({})".format(class_name, my_user_id), s)
        self.assertIn("'id': '{}'".format(my_user_id), s)
        self.assertIn("'created_at': " + my_user_created_at, s)
        self.assertIn("'updated_at': " + my_user_updated_at, s)
        self.assertIn("'email': '{}'".format(self.my_user.email), s)
        self.assertIn("'password': '{}'".format(self.my_user.password), s)
        self.assertIn("'email': '{}'".format(self.my_user.email), s)
        self.assertIn("'first_name': '{}'".format(self.my_user.first_name), s)
        self.assertIn("'last_name': '{}'".format(self.my_user.last_name), s)


if __name__ == '__main__':
    unittest.main(verbosity=2)
