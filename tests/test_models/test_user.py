#!/usr/bin/python3

"""
Suite to test subclass User in models.user
"""

import unittest

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test attributes in user
    """
    def test_subclass_in_user(self):
        """
        Test user attributes
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes_in_user(self):
        i = User()
        self.assertIs(type(i.first_name), str)
        self.assertIs(type(i.last_name), str)
        self.assertTrue(i.first_name == "")
        self.assertTrue(i.last_name == "")
        self.assertIs(type(u.passworrd), str)
        self.assertIs(type(u.email), str)
        self.assertTrue(u.password == "")
        self.assertTrue(u.email == "")
