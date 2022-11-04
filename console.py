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


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Review": Review,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "State": State
    }

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

        if arg not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")

        if arg in HBNBCommand.__classes.keys():
            new = HBNBCommand.__classes[arg]()
            print(new.id)
            new.save()

    def do_count(self, arg):
        arg = arg.split()
        all_objs = models.storage.all()
        count = 0
        if not arg:
            print("** class name missing **")

        if arg[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")

        if len(arg) == 1 and arg[0] in HBNBCommand.__classes.keys():
            for obj_id in all_objs:
                if arg[0] == obj_id.split('.')[0]:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        all_objs = models.storage.all()

        arg = arg.split()

        if not arg:
            print("** class name missing **")
            return

        if arg[0] and arg[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print("** instance id missing **")
            return

        if arg[0] in HBNBCommand.__classes.keys() and arg[1]:
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

        if arg[0] and arg[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print("** instance id missing **")
            return

        if arg[0] in HBNBCommand.__classes.keys() and arg[1]:
            attr = arg[0] + '.' + arg[1]
            if attr not in all_objs:
                print("** no instance found **")
                return
            else:
                del all_objs[attr]

    def do_all(self, arg):
        arg = arg.split()
        all_objs = models.storage.all()

        if len(arg) == 1 and arg[0] in HBNBCommand.__classes.keys():
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

        if arg[0] and arg[0] not in HBNBCommand.__classes.keys():
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
                an_obj = all_objs[arg[0] + '.' + arg[1]]
                an_obj.__dict__[arg[2]] = arg[3][1: len(arg[3]) - 1]

    def default(self, line):
        cmd_functions = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }

        cmd_line = line.split('.')
        if len(cmd_line) == 1:
            print('*** Unknown syntax:', line)
            return

        if len(cmd_line) == 2:
            cmd_0 = cmd_line[0].replace(" ", "")
            cmd_1 = cmd_line[1].replace(" ", "")
            if cmd_0 not in HBNBCommand.__classes.keys():
                print('*** Unknown syntax:', line)
                return
            else:
                cls_name = cmd_0
                len_cmd_1 = len(cmd_1)
                if '(' in cmd_1:
                    cmd_func = str()
                    i = 0
                    for c in cmd_1:
                        if c != "(":
                            cmd_func += c
                            i += 1
                        if c == "(":
                            break

                    if cmd_func not in cmd_functions:
                        print('*** Unknown syntax:', line)
                        return

                    i = i + 1
                    if i >= len(cmd_1):
                        print('missing ")" at the end')
                        return

                    if i < len(cmd_1):
                        if cmd_1[i] == ')':
                            cmd_functions[cmd_func](cls_name)
                            return

                        if cmd_1[i] != '"' or cmd_1[len_cmd_1 - 2] != '"'\
                                or cmd_1[len_cmd_1 - 1] != ')':
                            print('missing ")(" at the end')
                            return

                        if cmd_1[i] == '"' and cmd_1[len_cmd_1 - 2] == '"':
                            cmd_args = cmd_line[1][i+1:len_cmd_1 - 2]
                            if ',' not in cmd_args:
                                the_args = cls_name + ' ' + cmd_args
                                cmd_functions[cmd_func](the_args)
                            else:
                                the_args = str()
                                for i in cmd_args.split(','):
                                    the_args += i + ' '
                                the_args = the_args.replace('"', '')

                                cmd_functions[cmd_func](cls_name + " " + the_args)

    def do_clear(self, arg):
        from os import system
        system('clear')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
