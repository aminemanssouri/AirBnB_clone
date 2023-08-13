#!/usr/bin/python3
""" class of  FileStorage
    serializes instances to a JSON file
    as well as deserializes JSON file to be  instances """

import uuid
import os
import json
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State

class FileStorage:
    """start  construct """
    __file_path = "creat file.json"
    __objects = {}

    def all(self):
        """ return of dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """ start sets in dictionary the object with key <obj class name>.id """
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """ serializes objectss to be the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fname:
            new_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(new_dict, fname)

    def reload(self):
        """start   Reload the file """
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fname:
                l_json = json.load(fname)
                for key, val in l_json.items():
                    FileStorage.__objects[key] = eval(
                        val['__class__'])(**val)
