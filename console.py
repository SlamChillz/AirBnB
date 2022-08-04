#!/usr/bin/python3

"""
A module that defines the command line interpreter for AirBnB project
"""

import re
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command line interpreter
    """
    prompt = '(hbnb) '
    __classes = {
        'BaseModel': BaseModel,
        'User': User
    }

    def parseline(self, line):
        """Parse the line into a command name and a string containing
        the arguments.  Returns a tuple containing (command, args, line).
        'command' and 'args' may be None if the line couldn't be parsed.
        """
        line = self.__parseline(line)
        line = line.strip()
        if not line:
            return None, None, line
        elif line[0] == '?':
            line = 'help ' + line[1:]
        elif line[0] == '!':
            if hasattr(self, 'do_shell'):
                line = 'shell ' + line[1:]
            else:
                return None, None, line
        i, n = 0, len(line)
        while i < n and line[i] in self.identchars: i = i+1
        cmd, arg = line[:i], line[i:].strip()
        return cmd, arg, line

    def do_create(self, arg):
        """Creates an instance of `BaseModel`
        Usage: create BaseModel
        """
        args = self.__filter(arg)
        invalid = self.__validateArgs('create', args)
        if invalid:
            return (print(invalid))
        newBaseModel = self.__classes[args[0]]
        new = newBaseModel()
        print(new.id)

    def do_show(self, arg):
        """
        Shows string representation of a class id given

        Attr:
            arg (str): string of arguments
        """
        args = self.__filter(arg)
        invalid = self.__validateArgs('show', args)
        if invalid:
            return (print(invalid))
        key = '.'.join(args[:2])
        objs = storage.all()
        obj = objs.get(key, None)
        if (obj):
            return print(obj)
        print('** no instance found **')

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id

        Attr:
            arg (str): string of arguments
        """
        args = self.__filter(arg)
        invalid = self.__validateArgs('destroy', args)
        if invalid:
            return (print(invalid))
        key = '.'.join(args[:2])
        objs = storage.all()
        if objs.pop(key, None):
            return (storage.save())
        print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of 
        all instances based or not on the class name

        Attr:
            arg (str): string or arguments
        """
        args = self.__filter(arg)
        model = None
        if len(args) > 0:
            invalid = self.__validateArgs('all', args)
            if invalid:
                return (print(invalid))
            model = args[0]
        obList = [str(v) for v in (storage.all()).values()]
        if model:
            match = '[{}]'.format(model)
            obList = list(filter(lambda s: s.startswith(match), obList))
        print(obList)

    def __updateMePlease(self, obj, args):
        """
        Checks if update inputs are valid

        Attr:
            obj (BaseModel): instance to be updated
            args (list): list of passed arguments

        Return:
            (str): error message
            (None): if no parameters are valid and all set
        """ 
        if not obj:
            return ('** no instance found **')
        if len(args) < 3:
            return ('** attribute name missing **')
        if len(args) < 4:
            return ('** value missing **')
        return None

    def do_update(self, arg):
        """
         Updates an instance based on the class name and id by adding or
         updating attribute 

         Attr:
            arg (str): string or arguments
        """
        args = self.__filter(arg)
        invalid = self.__validateArgs('update', args)
        if invalid:
            return (print(invalid))
        key = '.'.join(args[:2])
        objs = storage.all()
        obj = objs.get(key, None)
        no = self.__updateMePlease(obj, args)
        if no:
            return print(no) # gotyah!!! LMAO
        setattr(obj, args[2], args[3]) # sad face, I get you for mind.
        obj.save()

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
        return shlex.split(arg) 

    def __validateArgs(self, query, args):
        """
        Validates given parameters

        Attr:
            query (str): action to be performed
            args (list): list of parameters

        Return:
            None: on valid inputs
            (str): on invalid inputs
        """
        actions = ['all', 'create', 'destroy', 'show', 'update']
        if len(args) < 1:
            if query != actions[0]:
                return ('** class name missing **')
        if not (self.__classes.get(args[0], None)):
            return ('** class doesn\'t exist **')
        if query in actions[2:]:
            if len(args) < 2:
                return ('** instance id missing **')
        return None

    def __parseline(self, line):
        """
        Parse command formats like `<Model>.<action>(<*args>)`
        to native formats
        """
        newLine = line.strip()
        args = re.search(r'\(.*?\)', newLine)
        if args is not None:
            newargs = re.search(r'"(.+?)*"', args.group())
            action = shlex.split(
                newLine[:args.span()[0]]
            )[0].split(".")
            if len(action) == 2:
                if newargs is not None:
                    newargs = " ".join(newargs.group().split(", "))
                    line = "{} {} {}".format(action[1], action[0], newargs)
                else:
                    line = "{} {}".format(action[1], action[0])
        return line
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
