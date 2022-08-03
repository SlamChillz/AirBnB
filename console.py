#!/usr/bin/python3

"""
A module that defines the command line interpreter for AirBnB project
"""

from models.base_model import BaseModel
from models import storage
import cmd


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
        invalid = self.__validateArgs('create', args)
        if invalid:
            return (print(invalid))
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
        invalid = self.__validateArgs('show', args)
        if invalid:
            return (print(invalid))
        key = '.'.join(args[:2])
        obj = storage.all()
        obj = self.__convert(obj.get(key, None))
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
        obList = [v for v in (storage.all()).values()]
        if model:
            obList = list(filter(lambda o: o['__class__'] == model, obList))
        objs = list(map(lambda o: self.__convert(o), obList))
        print(objs)

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
        if not obj:
            return (print('** no instance found **'))
        if len(args) < 3:
            return (print('** attribute name missing **'))
        if len(args) < 4:
            return (print('** value missing **'))
        obj.update({args[2]: args[3]})
        objs.update({key: obj})
        storage.save()



    def __convert(self, dictionary):
        """
        Attr:
            model (str): name of the model
            dictionary (dict): dictionary of instance values

        Return:
            (str): string representation
        """
        if dictionary is not None:
            model = dictionary['__class__']
            Model = self.__classes[model]
            return str(Model(**dictionary))
        return None
 
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
