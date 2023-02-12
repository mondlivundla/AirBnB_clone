#!/usr/bin/python3

"""
Test modules forclass City  in models.city
"""
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test case for class City
    """
    def initEnv(self):
        self.city = City()
        self.city_attr = ["state_id", "name"]

    def test_has_attributes(self):
        for items in self.city_attr:
            self.assertIs(type(getattr(self.city, items)), str)
