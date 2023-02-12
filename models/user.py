<<<<<<< HEAD
#!usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new user"""
=======
#!/usr/bin/python3
"""user class
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''base model class'''

>>>>>>> ebc98b8478f6e8be94390166139c7793502138a3
    email = ""
    password = ""
    first_name = ""
    last_name = ""
