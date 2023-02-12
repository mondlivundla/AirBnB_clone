#!/usr/bin/python3

"""
This module provides the class User
"""


from models import base_model


class User(base_model.BaseModel):
    """
    class User that inherits from BaseModel.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
