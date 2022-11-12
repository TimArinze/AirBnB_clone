#!/usr/bin/python3
'''console module is the entry point of the command interpreter'''

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)' if sys.__stdin__.isatty() else ''
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
        arg = arg.split()
        all_objs = models.storage.all()
        count = 0
        if len(arg) == 1 and arg[0] in HBNBCommand.__classes.keys():
            arr = list()
            for obj_id in all_objs:
                if arg[0] == obj_id.split('.')[0]:
                    count += 1
            print(count)
        elif not arg:
            arr = list()
            for obj_id in all_objs:
                count += 1
            print(count)

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

                arg[2] = arg[2].replace('"', '').replace("'", '')

                if arg[3].isdigit():
                    arg[3] = int(arg[3])
                elif isfloat(arg[3]):
                    arg[3] = float(arg[3])
                else:
                    arg[3] = arg[3].replace('"', '').replace("'", '')

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

        chars = [chr(32), chr(8), chr(9), chr(10), chr(11), chr(12), chr(13)]
        for char in chars:
            clean_line = line.replace(char, '')

        if '.' not in line:
            print('*** Unknown syntax:', line)
            return

        dot_idx = clean_line.find('.')
        if dot_idx == -1:
            print('*** Unknown syntax:', line)
            return

        if dot_idx + 1 >= len(line):
            print('*** Unknown syntax:', line)
            return

        cmd_cls = clean_line[:dot_idx]
        if cmd_cls not in HBNBCommand.__classes.keys():
            print('*** Unknown syntax:', line)
            return

        remain = clean_line[dot_idx + 1:]

        if '(' not in remain or ')' not in remain\
                or ('(' in remain and remain[len(remain) - 1] !=')'):
            print('*** Unknown syntax:', line)
            return

        op_idx = remain.index('(')
        cmd_func = remain[:op_idx]
        if cmd_func not in cmd_functions:
            print('*** Unknown syntax:', line)
            return

        if remain.find('(', op_idx + 1) != -1:
                print('*** Unknown syntax:', line)
                return
        if cmd_func in ['all', 'count']:
            cp_idx = remain.find(')',op_idx + 1)
            if cp_idx != -1 and remain.find(')', cp_idx + 1) != -1:
                print('*** Unknown syntax:', line)
                return

            cmd_functions[cmd_func](cmd_cls)
            return

        if remain[op_idx + 1] not in ['"', "'"]:
            print('*** Unknown syntax:', line)
            return

        if cmd_func in ['show', 'destroy']:
            if (remain[op_idx + 1] == '"' and remain[len(remain) - 2] != '"')\
                    or (remain[op_idx + 1] == "'"\
                    and remain[len(remain) - 2] != "'"):
                print('*** Unknown syntax:', line)
                return
            cmd_arg = remain[op_idx + 2:len(remain) - 1]
            cmd_arg = cmd_arg.replace('"', '').replace("'", '')

            cmd_functions[cmd_func](cmd_cls + ' ' + cmd_arg)
            return

        if cmd_func == 'update':
            if '{' not in remain:
                if ',' in remain and occurrence(remain, ',') == 2:
                    the_args = remain[len(cmd_func) + 1:].split(',')
                    if len(the_args) == 3:
                        id_arg = the_args[0].replace('"', '').replace("'", '')
                        key_arg = the_args[1].replace('"', '').replace("'", '')
                        value_arg = the_args[2].replace(')', '')
                        value_arg = value_arg.replace('"', '').replace("'", '')
                        args = id_arg + ' ' + key_arg + ' ' + value_arg

                        cmd_functions[cmd_func](cmd_cls + ' ' + args)

                    else:
                        print('*** Unknown syntax:', line)
                        return

                else:
                    print('*** Unknown syntax:', line)
                    return

            else:
                if remain[len(remain) - 2] == '}':
                    comma_idx = remain.find(',')
                    if comma_idx == - 1:
                        print('*** Unknown syntax:', line)
                        return

                    id_arg = remain[op_idx + 1:comma_idx].replace("'", '')
                    id_arg = id_arg.replace('"', '')
                    ob_idx = remain.find('{')
                    cb_idx = remain.find('}')
                    the_dict = remain[ob_idx + 1: cb_idx]

                    if ',' not in the_dict:
                        the_args = the_dict.split(':')
                        if len(the_args) == 2:
                            for i in range(len(the_args)):
                                the_args[i].replace("'", '').replace('"', '')

                            args = ' '.join([id_arg, the_args[0], the_args[1]])
                            cmd_functions[cmd_func](cmd_cls + ' ' + args)
                        else:
                            print('*** Unknown syntax:', line)
                            return
                    else:
                        kv = the_dict.split(',')
                        key = value = args = ''
                        if len(kv) % 2 == 0:
                            for i in range(len(kv)):
                                if i % 2 == 0:
                                    key = kv[i]
                                    key = key.replace("'", '')
                                if i % 2 != 0:
                                    value = kv[i]
                                    value = key.replace("'", '')
                                    value = key.replace('"', '')
                                    value = key.replace(')', '')

                                args = id_arg + ' ' + key_arg + ' ' + value_arg

                                cmd_functions[cmd_func](cmd_cls + ' ' + args)
                        else:
                            print('*** Unknown + syntax:', line)
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
