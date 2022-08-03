#!/usr/bin/python3

"""
A module that defines the command line interpreter for AirBnB project
"""

from models.base_model import BaseModel
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command line interpreter
    """
    prompt = '(hbnb) '
    __classes = {
        'BaseModel': BaseModel
    }

    def do_create(self, arg):
        """Creates an instance of `BaseModel`
        Usage: create BaseModel
        """
        args = self.__filter(arg)
        try:
            if len(args) < 1:
                raise Exception('** class name missing **')
            self.__checkModel(args)
        except Exception as e:
            print(e)
        else:
            newBaseModel = self.__classes[args[0]]
            new = newBaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """
        Shows string representation of a class id given

        Attr:
            arg (str): string of arguments
        """
        args = self.__filter(arg)
        print(args)
        try:
            if len(args) < 1:
                raise Exception('** class name missing **')
            elif len(args) < 2:
                raise Exception('** instance id missing **')
            self.__checkModel(args)
        except Exception as e:
            print(e)
        else:
            key = '.'.join(args[:2])
            objs = self.__queryDB()
            print(objs.get(key, '** no instance found **'))

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id

        Attr:
            arg (str): string of arguments
        """
        try:
            if len(args) < 1:
                raise Exception('** class name missing **')
            elif len(args) < 2:
                raise Exception('** instance id missing **')
            self.__checkModel(args)
        except Exception as e:
            print(e)
        else:
            key = '.'.join(args[:2])
            objs = self.__queryDB()
            
            

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Exits the interpreter
        """
        return True

    def __filter(self, arg):
        """
        Converts arguments to a valid list that can be worked with
        """
        sep = ' '
        count = arg.count('"')
        if count and (not count%2):
            sep = '"'
        return list(
            filter(lambda s: s.split(), arg.strip().split(sep))
        )

    def __checkModel(self, args):
        """
        Checks for a valid model

        Attr:
            arg (list): list of args

        Raises:
            Exceptions: with the right messages
        """
        if args[0] not in self.__classes:
            raise Exception('** class doesn\'t exist **')

    def __queryDB(self):
        """
        Queries the database

        Return:
            (dict): a dictionary of all items in the database
        """
        from model import storage
        objs = storage.all()
        return objs


if __name__ == '__main__':
    HBNBCommand().cmdloop()
