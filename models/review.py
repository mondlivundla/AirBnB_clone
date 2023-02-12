#!/usr/bin/python3
"""The `review` module.

It defines one class, `Review(),
which sub-classes the `BaseModel()` class.`
=======
"""
Module Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
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
