#!/usr/bin/python3
<<<<<<< HEAD

import unittest
import os
import pep8
from models.user import User
=======
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
>>>>>>> ebc98b8478f6e8be94390166139c7793502138a3
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
<<<<<<< HEAD

    @classmethod
    def setUpClass(cls):
        cls.my_user = User()
        cls.my_user.first_name = "Betty"
        cls.my_user.last_name = "Holberton"
        cls.my_user.email = "airbnb@holbertonshool.com"
        cls.my_user.password = "root"

    @classmethod
    def tearDownClass(cls):
        del cls.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('id' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.first_name), str)

    def test_save(self):
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.my_user), True)


if __name__ == "__main__":
    unittest.main()
=======
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
>>>>>>> ebc98b8478f6e8be94390166139c7793502138a3
