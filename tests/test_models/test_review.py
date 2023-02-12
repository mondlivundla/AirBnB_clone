#!/usr/bin/python3

"""
Suite to test subclass User in models.user
"""

import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test attributes in user
    """
    def test_class_review(self):
        """
        Assert all attributes of treview
        """
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertEqual(Review.place_id, '')
        self.assertEqual(Review.user_id, '')
        self.assertEqual(Review.text, '')
