#!/usr/bin/python3
"""start  user class """
from models.base_model import BaseModel
class User(BaseModel):
    """ User class that help to creat inherits BaseModel """
    
    first_name = ""
    last_name = ""
    email = ""
    password = ""
