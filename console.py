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
        '''Initializes a new instance by specifying only a class name'''
        if not arg:
            print("** class name missing **")
            return

        if arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if arg in HBNBCommand.__classes.keys():
            new = HBNBCommand.__classes[arg]()
            print(new.id)
            new.save()

    def do_count(self, arg):
        '''Gives the number of instances of a class'''
        all_objs = models.storage.all()
        count = 0
        if not arg:
            print("** class name missing **")
            return

        if arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(arg) == 1 and arg[0] in HBNBCommand.__classes.keys():
            for obj_id in all_objs:
                if arg[0] == obj_id.split('.')[0]:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        '''Prints an instance based on its class an id'''
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
        '''Deletes an instance based on its class an id'''
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
                models.storage.save()

    def do_all(self, arg):
        '''Prints all instances of a class name if specified, otherwise all
            instances are printed'''
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
        '''Update an instance based on its class name, its id, a name attribute
            and a its value'''
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
                if arg[3].isdigit():
                    arg[3] = int(arg[3])
                elif isfloat(arg[3]):
                    arg[3] = float(arg[3])
                else:
                    arg[3] = arg[3].replace('"', '')

                an_obj.__dict__[arg[2]] = arg[3]
                all_objs[arg[0] + '.' + arg[1]] = an_obj
                an_obj.save()

    def default(self, line):
        '''Handle unrecognized syntax'''
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
                        print('*** Unknown syntax:', line)
                        return

                    if cmd_func in ['all', 'count']:
                        if (i == len(cmd_1) - 1 and cmd_1[i] != ')') or\
                                (i < len(cmd_1) - 1 and cmd_1[i] == ')'):
                            print('*** Unknown syntax', line)
                            return

                        cmd_functions[cmd_func](cls_name)

                    if cmd_func in ['show', 'destroy']:
                        cmd_arg = cmd_1[i:].replace('(', '').replace('"', '')
                        cmd_arg = cmd_arg.replace(')', '')
                        cmd_functions[cmd_func](cls_name + ' ' + cmd_arg)

                    if cmd_func == 'update':
                        cmd_args = cmd_1[i:].replace('(', '').replace('"', '')
                        cmd_args = cmd_args.replace(')', '').replace('{', '')
                        cmd_args = cmd_args.split(',')

                        if len(cmd_args) > 2:
                            first = cmd_args[0]
                            second = cmd_args[1]
                            last = cmd_args[2]

                            the_args = first + ' ' + second + ' ' + last
                            cmd_functions[cmd_func](cls_name + ' ' + the_args)

                        else:
                            print('*** Unknown syntax:', line)
                            return

                else:
                    print('*** Unknown syntax:', line)
                    return

    def do_clear(self, arg):
        '''clear the stdin'''
        from os import system
        system('clear')

    def occurrence(word, c):
        '''Return the number of occurrence of a character in a string'''
        count = 0
        for i in word:
            if i == c:
                count += 1
        return count

def isfloat(string):
    '''Checks if a string can be converted to float
        Return: True if the string can be converted into Python Float
                False, otherwhise'''
    if '.' in string and occurrence(string, '.') == 1:
        n = string.replace('.', '')
        if n.isdigit():
            return True
        else:
            False
    else:
        False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
