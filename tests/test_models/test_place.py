#!/usr/bin/python3

"""
Suite to test subclass place in models.place
"""

import unittest

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test attributes in place
    """
    def test_class_place(self):
        """
        Assert all attributes of place
        """
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertEqual(Place.city_id, '')
        self.assertEqual(Place.user_id, '')
        self.assertEqual(Place.name, '')
        self.assertEqual(Place.description, '')

        self.assertTrue(type(Place.number_rooms) is int)
        self.assertEqual(Place.number_rooms, 0)

        self.assertTrue(type(Place.number_bathrooms) is int)
        self.assertEqual(Place.number_bathrooms, 0)

        self.assertTrue(type(Place.max_guest) is int)
        self.assertEqual(Place.max_guest, 0)

        self.assertTrue(type(Place.price_by_night) is int)
        self.assertEqual(Place.price_by_night, 0)

        self.assertTrue(type(Place.latitude) is float)
        self.assertEqual(Place.latitude, 0.0)

        self.assertTrue(type(Place.longitude) is float)
        self.assertEqual(Place.longitude, 0.0)

        self.assertTrue(type(Place.amenity_ids) is list)
        self.assertEqual(Place.amenity_ids, [])
