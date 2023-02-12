#!/usr/bin/python3
<<<<<<< HEAD
"""
Module: __init__.py
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
=======
'''comment'''
from models.engine.file_storage import FileStorage

storage = FileStorage()
>>>>>>> ebc98b8478f6e8be94390166139c7793502138a3
storage.reload()
