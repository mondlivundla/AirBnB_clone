#!/usr/bin/python3
"""
This module creatres a unique FileStorage instance for my application.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
