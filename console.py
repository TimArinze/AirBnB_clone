#!/usr/bin/python3
"""
A program that contains the entry point of the command interpreter
"""

from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNB Command """

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """EOF key combination can be used to log out of the file\n"""

        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""

        exit()

    def do_create(self, line):
        """Creates a new instance of Basemodel, saves it (to the JSON file)
        And prints the id
        """
        if line:
            if line == 'BaseModel':
                new = BaseModel()
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist")
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    HBNBCommand().emptyline()
