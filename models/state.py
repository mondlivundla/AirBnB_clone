#!/usr/bin/python3

"""
This module provides the class State
"""


from models import base_model


class State(base_model.BaseModel):
    """
    State class that inherits form BaseModel
    """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
