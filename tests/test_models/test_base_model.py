#!/usr/bin/python3

import unittest
import datetime
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    """Never trust User/Builder inputs"""

    def setUp(self):
        """Prepraring test cases"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.tmp = self.my_model.updated_at
        self.maxDiff = None

    def test_isinstance_of_BaseModel(self):
        """Test class of an instance"""
        self.assertIsInstance(self.my_model, BaseModel)

    def test_id_attribute(self):
        """All individual tests for id attribute"""

        """Testing if an instance automatically has the id attribute"""
        self.assertTrue(hasattr(self.my_model, 'id'))

        """Testing current type of id"""
        self.assertIsInstance(self.my_model.id, str)

        """This test is for the format of id"""
        with self.assertRaises(ValueError):
            string = 'hello'
            self.my_model.id = string
            """ID Pattern Testing
                Using uuid.UUID function return the uuid object that gives this
                string."""
            uuid.UUID(self.my_model.id)

    def test_created_at_attribute(self):
        """All individual tests for created_at attribute"""

        """Testing if an instance automatically has the created_at attribute"""
        self.assertTrue(hasattr(self.my_model, 'created_at'))

        """Testing type of created_at"""
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)

    def test_updated_at_attribute(self):
        """All individual tests for updated_at attribute"""

        """Testing if an instance automatically has the updated_at attribute"""
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

        """Testing type of updated_at"""
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

    def test_to_dict(self):
        """All test for to_dict method"""
        the_dict = self.my_model.to_dict()
        """Testing if to_dict return a dictionary object"""
        self.assertIs(type(the_dict), dict)

        """Testing expected attribute returned by to_dict"""
        attrs = ['__class__', 'created_at', 'updated_at', 'id']
        for attr in attrs:
            self.assertIn(attr, the_dict)
            self.assertIs(type(attr), str)

    def test_based_from_dictionary(self):
        the_dict = self.my_model.to_dict()
        my_other_model = BaseModel(**the_dict)
        self.assertEqual(self.my_model.__dict__, my_other_model.__dict__)
        self.assertEqual(self.my_model.to_dict(), my_other_model.to_dict())

    def test_save(self):
        self.my_model.save()
        self.assertNotEqual(self.tmp, self.my_model.updated_at)


if __name__ == '__main__':
    unittest.main(verbosity=2)
