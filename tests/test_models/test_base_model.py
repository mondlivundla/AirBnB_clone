#!/usr/bin/python3

"""
Module with test suite for class BaseModel
"""

import unittest
from datetime import datetime
import os
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    TestSuite for BaseModel
    """
    def test_if_id_exists(self):
        """
        Case to test if id exists upon initialization
        """
        i = BaseModel()
        self.assertTrue(hasattr(i, "id"))

    def test_unique_id_generated(self):
        """
        Test if a unique id is called each time
        """
        i_a = BaseModel()
        i_b = BaseModel()
        self.assertNotEqual(i_a.id, i_b.id)

    def test_str_print_format(self):
        """
        Test for the rirhst object representation
        """
        i = BaseModel()
        self.assertEqual(str(i),
                         "[BaseModel] ({}) {}".format(i.id, i.__dict__))

    def test_created_at_is_format(self):
        """
        Test if the created_at attribute is datetime format
        """
        i = BaseModel()
        self.assertTrue(type(i.created_at) is datetime)

    def test_updated_at_is_format(self):
        """
        Test if the created_at attribute is datetime format
        """
        i = BaseModel()
        self.assertTrue(type(i.updated_at) is datetime)

    def test_initial_equality_of_times(self):
        """
        Test if 'created_at' and 'updated_at' are equal
        """
        i = BaseModel()
        self.assertEqual(i.created_at, i.updated_at)

    def test_if_save_method_updates_time_attr(self):
        """
        Test functionality of the save method
        """
        i = BaseModel()
        sleep(0.05)
        time_update = i.updated_at
        i.save()
        self.assertLess(i.time_update, i.updated_at)


if __name__ == "__main__":
    unittest.main()
