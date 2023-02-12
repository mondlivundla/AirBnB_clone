#!/usr/bin/python3
"""
This module provides the class FileStorage
"""
import json
import os.path


class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        cls_name = type(obj).__name__
        idd = obj.id
        key = str(cls_name) + "." + str(idd)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        js_str = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as fd:
            fd.write(js_str)

    def reload(self):
        """
        desrializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="UTF-8") as fd:
                js_str = fd.readline()
            FileStorage.__objects = json.loads(js_str)
