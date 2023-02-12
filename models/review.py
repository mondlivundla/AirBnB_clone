#!/usr/bin/python3
<<<<<<< HEAD
"""The `review` module.

It defines one class, `Review(),
which sub-classes the `BaseModel()` class.`
=======
"""
Module Review class
>>>>>>> ebc98b8478f6e8be94390166139c7793502138a3
"""
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """A review of a place/house.

    It represents a review posted by the users
    of the application about a place/house.

    Attributes:
        text
        user_id
        place_id
    """
    text = ""
    user_id = ""
    place_id = ""
=======
    """
    Inherits from BaseModel
    Public class attributes:
        place_id:            (str) will be Place.id
        user_id:             (str) will be User.id
        text:                (str)
    """
    place_id = ""
    user_id = ""
    text = ""
>>>>>>> ebc98b8478f6e8be94390166139c7793502138a3
