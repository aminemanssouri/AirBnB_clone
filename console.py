#!/usr/bin/python3
""" Holberton AirBnB Console project  """
import json
import os
import cmd
import sys
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models import storage
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage

class HBNBCommand(cmd.Cmd):
    """ Interactive command-line interface for HBNB """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

    def do_quit(self, arg):
        """ Exit the command line interface """
        exit()

    def do_EOF(self, arg):
        """ Exit when the end of the file is reached """
        print('')
        exit()

    def emptyline(self):
        """ Do nothing on an empty line """
        pass

    def do_create(self, arg):
        """ Create a new instance of a class """
        if len(arg) == 0:
            print('** class name missing **')
            return
        new_instance = None
        if arg in self.classes:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Display the string representation of an instance """
        if len(arg) == 0:
            print('** class name missing **')
            return
        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) > 1:
            instance_id = arg_list[1]
            key = f'{class_name}.{instance_id}'
            if key in storage.all():
                instance = storage.all()[key]
                print(instance)
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    # ... (similar changes for other methods)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

