#!/usr/bin/python3

'''console module is the entry point of the command interpreter'''
import cmd
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
import models


classes = {
    "BaseModel":BaseModel,
    "User":User,
    "Review":Review,
    "Place":Place,
    "Amenity":Amenity,
    "City":City,
    "State":State
    }

cmd_functions = {
    "create":do_create,
    "show":do_show,
    "destroy":do_destroy,
    "all":do_all,
    "update":do_update
}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        '''Quit command to exit the program'''
        print()
        return True

    def do_help(self, arg):
        '''Help command to display documention of its argument'''
        return super().do_help(arg)

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")

        if arg not in classes.keys():
            print("** class doesn't exist **")

        if arg in classes.keys():
            new = classes[arg]()
            print(new.id)
            new.save()

    def do_show(self, arg):
        all_objs = models.storage.all()

        arg = arg.split()

        if not arg:
            print("** class name missing **")
            return

        if arg[0] and arg[0] not in classes.keys():
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print("** instance id missing **")
            return

        if arg[0] in classes.keys() and arg[1]:
            attr = arg[0] + '.' + arg[1]
            if attr not in all_objs:
                print("** no instance found **")
                return
            else:
                print(all_objs[attr])

    def do_destroy(self, arg):
        all_objs = models.storage.all()

        arg = arg.split()
        if not arg:
            print("** class name missing **")
            return

        if arg[0] and arg[0] not in classes.keys():
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print("** instance id missing **")
            return

        if arg[0] in classes.keys() and arg[1]:
            attr = arg[0] + '.' + arg[1]
            if attr not in all_objs:
                print("** no instance found **")
                return
            else:
                del all_objs[attr]

    def do_all(self, arg):
        arg = arg.split()
        all_objs = models.storage.all()

        if len(arg) == 1 and arg[0] in classes.keys():
            arr = list()
            for obj_id in all_objs:
                if arg[0] == obj_id.split('.')[0]:
                    arr.append(str(all_objs[obj_id]))
            print(arr)
        elif not arg:
            arr = list()
            for obj_id in all_objs:
                arr.append(str(all_objs[obj_id]))
            print(arr)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        arg = arg.split()
        all_objs = models.storage.all()

        if not arg:
            print("** class name missing **")
            return

        if arg[0] and arg[0] not in classes.keys():
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print("** instance id missing **")
            return

        attr = arg[0] + '.' + arg[1]
        if len(arg) == 2:
            if attr not in all_objs.keys():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
            return

        if len(arg) == 3:
            if attr not in all_objs.keys():
                print("** no instance found **")
            else:
                print("** value missing **")
            return

        if len(arg) == 4:
            if attr not in all_objs.keys():
                print("** no instance found **")

            else:
                an_obj = all_objs[attr]
                an_obj.__dict__.update([(arg[2], arg[3])])
                an_obj.save()

    def default(self, arg):
        args = arg.split('.')
        cls_name = args[0]
        remain_args = arg[1]
        

    def do_clear(self, arg):
        from os import system
        system('clear')

if __name__ == '__main__':
    HBNBCommand().cmdloop()























