#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def setUp(self):
        """Sets up test methods."""
        self.user = User()

    def tearDown(self):
        """Tears down test methods."""
        FileStorage._FileStorage__objects = {}
        os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Tests instantiation of User class."""
        self.assertIsInstance(self.user, User)
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_attributes(self):
        """Tests the attributes of User class."""
        attributes = storage.attributes()["User"]
        for attr_name, attr_type in attributes.items():
            self.assertTrue(hasattr(self.user, attr_name))
            self.assertIsInstance(getattr(self.user, attr_name, None), attr_type)

    def test_email_attribute(self):
        """Tests the email attribute of User class."""
        self.user.email = "example@example.com"
        self.assertEqual(self.user.email, "example@example.com")
        self.assertRaises(AttributeError, setattr, self.user, "email", 123)

    def test_password_attribute(self):
        """Tests the password attribute of User class."""
        self.user.password = "secret_password"
        self.assertEqual(self.user.password, "secret_password")
        self.assertRaises(AttributeError, setattr, self.user, "password", 123)

    def test_first_name_attribute(self):
        """Tests the first_name attribute of User class."""
        self.user.first_name = "John"
        self.assertEqual(self.user.first_name, "John")
        self.assertRaises(AttributeError, setattr, self.user, "first_name", 123)

    def test_last_name_attribute(self):
        """Tests the last_name attribute of User class."""
        self.user.last_name = "Doe"
        self.assertEqual(self.user.last_name, "Doe")
        self.assertRaises(AttributeError, setattr, self.user, "last_name", 123)
