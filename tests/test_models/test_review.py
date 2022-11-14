#!/usr/bin/python3
'''test_review module'''


import unittest
import datetime
from models.base_model import BaseModel
from models.review import Review
import uuid


class TestReview(unittest.TestCase):
    """Never trust Review/Builder inputs"""
    @classmethod
    def setUpClass(self):
        """Prepraring test cases"""
        self.my_review = Review()
        self.tmp = self.my_review.updated_at
        self.id = self.my_review.id
        self.maxDiff = None

    def test_isinstance_of_Review(self):
        """Test class of an instance"""
        self.assertIsInstance(self.my_review, Review)
        self.assertTrue(issubclass(self.my_review.__class__, BaseModel))

    def test_id_attribute(self):
        """All individual tests for id attribute"""

        '''Testing if `id` is a public attribute'''
        self.assertIn('id', dir(self.my_review))
        self.assertIn('id', self.my_review.__dict__)

        '''Testing if `id` is callable member'''
        with self.assertRaises(TypeError):
            self.my_review.id()
        """Testing current type of id"""
        self.assertIsInstance(self.my_review.id, str)

        """This test is for the format of id"""
        with self.assertRaises(ValueError):
            string = 'hello'
            self.my_review.id = string
            """ID Pattern Testing
                Using uuid.UUID function return the uuid object that gives this
                string."""
            uuid.UUID(self.my_review.id)
        '''Testing if `id` is really an attribute'''
        with self.assertRaises(TypeError):
            self.my_review.id()

        self.my_review.id = self.id

    def test_created_at_attribute(self):
        """All individual tests for created_at attribute"""

        '''Testing if `created_at` is a public attribute'''
        self.assertIn('created_at', dir(self.my_review))

        '''Testing if `created_at` is callable member'''
        with self.assertRaises(TypeError):
            self.my_review.created_at()

        """Testing type of created_at"""
        self.assertIsInstance(self.my_review.created_at, datetime.datetime)

    def test_updated_at_attribute(self):
        """All individual tests for updated_at attribute"""

        '''Testing if `updated_at` is a public attribute'''
        self.assertIn('updated_at', dir(self.my_review))
        self.assertIn('updated_at', self.my_review.__dict__)

        '''Testing if `updated_at` is callable member'''
        with self.assertRaises(TypeError):
            self.my_review.updated_at()

        """Testing type of updated_at"""
        self.assertIsInstance(self.my_review.updated_at, datetime.datetime)

    def test_place_id_attribute(self):
        """All individual tests for place_id attribute"""

        '''Testing if `place_id` is a public attribute'''
        self.assertIn('place_id', dir(self.my_review))
        self.assertNotIn('place_id', self.my_review.__dict__)

        self.my_review.place_id = "SN"
        self.assertIn('place_id', self.my_review.__dict__)

        '''Testing if `place_id` is callable member'''
        with self.assertRaises(TypeError):
            self.my_review.place_id()

        '''Testing type of place_id'''
        self.assertTrue(type(self.my_review.place_id) == str)

    def test_user_id_attribute(self):
        """All individual tests for user_id attribute"""

        '''Testing if `user_id` is a public attribute'''
        self.assertIn('user_id', dir(self.my_review))
        self.assertNotIn('user_id', self.my_review.__dict__)

        self.my_review.user_id = "SN"
        self.assertIn('user_id', self.my_review.__dict__)

        '''Testing if `user_id` is callable member'''
        with self.assertRaises(TypeError):
            self.my_review.user_id()

        '''Testing type of user_id'''
        self.assertTrue(type(self.my_review.user_id) == str)

    def test_text_attribute(self):
        """All individual tests for text attribute"""

        '''Testing if `text` is a public attribute'''
        self.assertIn('text', dir(self.my_review))
        self.assertNotIn('text', self.my_review.__dict__)

        self.my_review.text = "Some text"
        self.assertIn('text', self.my_review.__dict__)

        '''Testing if `text` is callable member'''
        with self.assertRaises(TypeError):
            self.my_review.text()

    def test_to_dict(self):
        """All tests for to_dict method"""

        '''Testing if `to_dict` is a member'''
        self.assertIn('to_dict', dir(Review))

        the_dict = self.my_review.to_dict()
        """Testing if to_dict return a dictionary object"""
        self.assertIs(type(the_dict), dict)

        """Testing expected attribute returned by to_dict"""
        attrs = ['__class__', 'created_at', 'updated_at', 'id']
        for attr in attrs:
            self.assertIn(attr, the_dict)
            self.assertIs(type(attr), str)

    def test_based_from_dictionary(self):
        '''Testing instanciation from a previous instance'''
        the_dict = self.my_review.to_dict()
        my_other_model = Review(**the_dict)
        self.assertEqual(self.my_review.__dict__, my_other_model.__dict__)
        self.assertEqual(self.my_review.to_dict(), my_other_model.to_dict())

    def test_save(self):
        """All tests for save method"""

        '''Testing if save is a method of Review'''
        self.assertIn('save', dir(Review))
        self.my_review.save()
        '''Testing if updated_at changes when calling save method'''
        self.assertNotEqual(self.tmp, self.my_review.updated_at)

        '''Testing if the instance is save in the file storage'''
        key = self.my_review.__class__.__name__ + '.' + self.my_review.id
        with open('file.json', 'r') as f:
            from json import load
            json_obj = load(f)
            self.assertEqual(json_obj[key], self.my_review.to_dict())

    def test_str_representation(self):
        """All tests for string representation"""

        '''Testing if __str__ is defined in Review'''
        self.assertIn('__str__', dir(Review))
        class_name = self.my_review.__class__.__name__
        my_review_id = self.my_review.id
        my_review_created_at = repr(self.my_review.created_at)
        my_review_updated_at = repr(self.my_review.updated_at)
        s = self.my_review.__str__()
        self.assertIn("[{}] ({})".format(class_name, my_review_id), s)
        self.assertIn("'id': '{}'".format(my_review_id), s)
        self.assertIn("'created_at': " + my_review_created_at, s)
        self.assertIn("'updated_at': " + my_review_updated_at, s)


if __name__ == '__main__':
    unittest.main(verbosity=2)
