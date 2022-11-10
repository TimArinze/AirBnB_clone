#!/usr/bin/python3
'''test_place module'''


import unittest
import datetime
from models.base_model import BaseModel
from models.place import Place
import uuid


class TestPlace(unittest.TestCase):
    """Never trust Place/Builder inputs"""
    @classmethod
    def setUpClass(self):
        """Prepraring test cases"""
        self.my_place = Place()
        self.tmp = self.my_place.updated_at
        self.maxDiff = None

    def test_isinstance_of_Place(self):
        """Test class of an instance"""
        self.assertIsInstance(self.my_place, Place)
        self.assertTrue(issubclass(self.my_place.__class__, BaseModel))

    def test_id_attribute(self):
        """All individual tests for id attribute"""

        '''Testing if `id` is a public attribute'''
        self.assertIn('id', dir(self.my_place))
        self.assertIn('id', self.my_place.__dict__)

        '''Testing if `id` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.id()
        """Testing current type of id"""
        self.assertIsInstance(self.my_place.id, str)

        """This test is for the format of id"""
        with self.assertRaises(ValueError):
            string = 'hello'
            self.my_place.id = string
            """ID Pattern Testing
                Using uuid.UUID function return the uuid object that gives this
                string."""
            uuid.UUID(self.my_place.id)
        '''Testing if `id` is really an attribute'''
        with self.assertRaises(TypeError):
            self.my_place.id()

    def test_created_at_attribute(self):
        """All individual tests for created_at attribute"""

        '''Testing if `created_at` is a public attribute'''
        self.assertIn('created_at', dir(self.my_place))

        '''Testing if `created_at` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.created_at()

        """Testing type of created_at"""
        self.assertIsInstance(self.my_place.created_at, datetime.datetime)

    def test_updated_at_attribute(self):
        """All individual tests for updated_at attribute"""

        '''Testing if `updated_at` is a public attribute'''
        self.assertIn('updated_at', dir(self.my_place))
        self.assertIn('updated_at', self.my_place.__dict__)

        '''Testing if `updated_at` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.updated_at()

        """Testing type of updated_at"""
        self.assertIsInstance(self.my_place.updated_at, datetime.datetime)

    def test_city_id_attribute(self):
        """All individual tests for city_id attribute"""

        '''Testing if `city_id` is a public attribute'''
        self.assertIn('city_id', dir(self.my_place))
        self.assertNotIn('city_id', self.my_place.__dict__)

        self.my_place.city_id = "Hobbyist Tech"
        self.assertIn('city_id', self.my_place.__dict__)

        '''Testing if `city_id` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.city_id()

        '''Testing type of city_id'''
        self.assertTrue(type(self.my_place.city_id) == str)

    def test_user_id_attribute(self):
        """All individual tests for user_id attribute"""

        '''Testing if `user_id` is a public attribute'''
        self.assertIn('user_id', dir(self.my_place))
        self.assertNotIn('user_id', self.my_place.__dict__)

        self.my_place.user_id = "BM05"
        self.assertIn('user_id', self.my_place.__dict__)

        '''Testing if `user_id` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.user_id()

        '''Testing type of user_id'''
        self.assertTrue(type(self.my_place.user_id) == str)

    def test_name_attribute(self):
        """All individual tests for name attribute"""

        '''Testing if `name` is a public attribute'''
        self.assertIn('name', dir(self.my_place))
        self.assertNotIn('name', self.my_place.__dict__)

        self.my_place.name = "Hobbyist Tech"
        self.assertIn('name', self.my_place.__dict__)

        '''Testing if `name` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.name()

        '''Testing type of name'''
        self.assertTrue(type(self.my_place.name) == str)

    def test_description_attribute(self):
        """All individual tests for description attribute"""

        '''Testing if `description` is a public attribute'''
        self.assertIn('description', dir(self.my_place))
        self.assertNotIn('description', self.my_place.__dict__)

        self.my_place.description = "The best one !"
        self.assertIn('description', self.my_place.__dict__)

        '''Testing if `description` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.description()

        '''Testing type of description'''
        self.assertTrue(type(self.my_place.description) == str)

    def test_number_rooms_attribute(self):
        """All individual tests for number_rooms attribute"""

        '''Testing if `number_rooms` is a public attribute'''
        self.assertIn('number_rooms', dir(self.my_place))
        self.assertNotIn('number_rooms', self.my_place.__dict__)

        self.my_place.number_rooms = 3
        self.assertIn('number_rooms', self.my_place.__dict__)

        '''Testing if `number_rooms` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.number_rooms()

        '''Testing type of description'''
        self.assertTrue(type(self.my_place.number_rooms) == int)

    def test_number_bathrooms_attribute(self):
        """All individual tests for number_bathrooms attribute"""

        '''Testing if `number_bathrooms` is a public attribute'''
        self.assertIn('number_bathrooms', dir(self.my_place))
        self.assertNotIn('number_bathrooms', self.my_place.__dict__)

        self.my_place.number_bathrooms = 2
        self.assertIn('number_bathrooms', self.my_place.__dict__)

        '''Testing if `number_bathrooms` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.number_bathrooms()

        '''Testing type of description'''
        self.assertTrue(type(self.my_place.number_bathrooms) == int)

    def test_max_guest_attribute(self):
        """All individual tests for max_guest attribute"""

        '''Testing if `max_guest` is a public attribute'''
        self.assertIn('max_guest', dir(self.my_place))
        self.assertNotIn('max_guest', self.my_place.__dict__)

        self.my_place.max_guest = 5
        self.assertIn('max_guest', self.my_place.__dict__)

        '''Testing if `max_guest` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.max_guest()

        '''Testing type of max_guest'''
        self.assertTrue(type(self.my_place.max_guest) == int)

    def test_price_by_night_attribute(self):
        """All individual tests for price_by_night attribute"""

        '''Testing if `price_by_night` is a public attribute'''
        self.assertIn('price_by_night', dir(self.my_place))
        self.assertNotIn('price_by_night', self.my_place.__dict__)

        self.my_place.price_by_night = 34
        self.assertIn('price_by_night', self.my_place.__dict__)

        '''Testing if `price_by_night` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.price_by_night()

        '''Testing type of price_by_night'''
        self.assertTrue(type(self.my_place.price_by_night) == int)

    def test_latitude_attribute(self):
        """All individual tests for latitude attribute"""

        '''Testing if `latitude` is a public attribute'''
        self.assertIn('latitude', dir(self.my_place))
        self.assertNotIn('latitude', self.my_place.__dict__)

        self.my_place.latitude = 34.8
        self.assertIn('latitude', self.my_place.__dict__)

        '''Testing if `latitude` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.latitude()

        '''Testing type of latitude'''
        self.assertTrue(type(self.my_place.latitude) == float)

    def test_amenity_ids_attribute(self):
        """All individual tests for amenity_ids attribute"""

        '''Testing if `amenity_ids` is a public attribute'''
        self.assertIn('amenity_ids', dir(self.my_place))
        self.assertNotIn('amenity_ids', self.my_place.__dict__)

        self.my_place.amenity_ids = []
        self.assertIn('amenity_ids', self.my_place.__dict__)

        '''Testing if `amenity_ids` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.amenity_ids()

        '''Testing type of amenity_ids'''
        self.assertTrue(type(self.my_place.amenity_ids) == list)

    def test_longitude_attribute(self):
        """All individual tests for longitude attribute"""

        '''Testing if `longitude` is a public attribute'''
        self.assertIn('longitude', dir(self.my_place))
        self.assertNotIn('longitude', self.my_place.__dict__)

        self.my_place.longitude = 24.5
        self.assertIn('longitude', self.my_place.__dict__)

        '''Testing if `longitude` is callable member'''
        with self.assertRaises(TypeError):
            self.my_place.longitude()

        '''Testing type of longitude'''
        self.assertTrue(type(self.my_place.longitude) == float)

    def test_to_dict(self):
        """All tests for to_dict method"""

        '''Testing if `to_dict` is a member'''
        self.assertIn('to_dict', dir(Place))

        the_dict = self.my_place.to_dict()
        """Testing if to_dict return a dictionary object"""
        self.assertIs(type(the_dict), dict)

        """Testing expected attribute returned by to_dict"""
        attrs = ['__class__', 'created_at', 'updated_at', 'id']
        for attr in attrs:
            self.assertIn(attr, the_dict)
            self.assertIs(type(attr), str)

    def test_based_from_dictionary(self):
        '''Testing instanciation from a previous instance'''
        the_dict = self.my_place.to_dict()
        my_other_model = Place(**the_dict)
        self.assertEqual(self.my_place.__dict__, my_other_model.__dict__)
        self.assertEqual(self.my_place.to_dict(), my_other_model.to_dict())

    def test_save(self):
        """All tests for save method"""

        '''Testing if save is a method of Place'''
        self.assertIn('save', dir(Place))
        self.my_place.save()
        '''Testing if updated_at changes when calling save method'''
        self.assertNotEqual(self.tmp, self.my_place.updated_at)

    def test_str_representation(self):
        """All tests for string representation"""

        '''Testing if __str__ is defined in Place'''
        self.assertIn('__str__', dir(Place))
        class_name = self.my_place.__class__.__name__
        my_place_id = self.my_place.id
        my_place_created_at = repr(self.my_place.created_at)
        my_place_updated_at = repr(self.my_place.updated_at)
        nr = self.my_place.number_rooms
        nb = self.my_place.number_bathrooms
        mg = self.my_place.max_guest
        pbn = self.my_place.price_by_night
        ltd = self.my_place.latitude
        lgd = self.my_place.longitude
        a_ids = self.my_place.amenity_ids
        s = self.my_place.__str__()
        self.assertIn("[{}] ({})".format(class_name, my_place_id), s)
        self.assertIn("'id': '{}'".format(my_place_id), s)
        self.assertIn("'created_at': " + my_place_created_at, s)
        self.assertIn("'updated_at': " + my_place_updated_at, s)


if __name__ == '__main__':
    unittest.main(verbosity=2)
