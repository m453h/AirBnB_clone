#!/usr/bin/python3
"""Command line interpreter for the AirBnB Clone."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):

    """Represents the Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
        """Intercept command entered by user."""
        self._intercept_cmd(line)

    def _intercept_cmd(self, line):
        """Intercepts and parses user entered CMD"""
        pass

    def do_EOF(self, line):
        """
        Exits the cmd interpreter on reading EOF.
        """
        print()
        return True

    def do_quit(self, line):
        """
        Exits the cmd interpreter.
        """
        return True

    def emptyline(self):
        """
        Does nothing on encountering an empty line.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
