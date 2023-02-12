#!/usr/bin/python3

"""
Suite to test amenity in modules.amenity
"""
import unittest

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.Test6Case):
    """
    TestCase for amenity
    """
    def initEnv(self):
        self.amenity = Amenity()

    def test_class_attribute(self):
        """
        Test if amenity has attribute name
        """
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_if_amenity_is_a_basemodel_item(self):
        """
        Testy if Amenity is asubclass of baseModel
        """
        self.assertTrue(issubclass(type(self.amenity), BaseModel))
