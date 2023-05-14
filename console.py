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

    def _parse_user_cmd(self, line):
        """Parses user entered command using regular expressions"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return None

        return {'classname': match.group(1),
                'method': match.group(2),
                'args': match.group(3)}

    def _parse_user_args(self, args):
        """
        Parses user entered agruments using regular expressions
        """
        match = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match:
            uid = match.group(1)
            return {'uid': match.group(1),
                    'attr_or_dict': match.group(2)}
        else:
            return {'uid': args,
                    'attr_or_dict': False}

    def _intercept_cmd(self, line):
        """
        Intercepts and parses user entered CMD
        """
        usr_cmd = self._parse_user_cmd(line)

        if usr_cmd is None:
            return line

        classname = usr_cmd['classname']
        method = usr_cmd['method']
        args = usr_cmd['args']

        usr_args = self._parse_user_args(args)
        uid = usr_args['uid']
        is_attr_or_dict = usr_args['attr_or_dict']

        attr_val = ""
        if method == "update" and is_attr_or_dict:
            match = re.search('^({.*})$', is_attr_or_dict)
            if match:
                self.update_from_dict(classname, uid, match.group(1))
                return ""
            match_attr_val = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', is_attr_or_dict)
            if match_attr_val:
                attr_val = f"{match_attr_val.group(1) or ''}\
                {match_attr_val.group(2) or ''}"

        command = f"{method} {classname} {uid} {attr_val}"
        self.onecmd(command)
        return command

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

    def display(self, message):
        """
        Displays message to the console
        """
        print("** {} **".format(message))

    def do_create(self, line):
        """
        Creates a new instance, saves it (to JSON file) and prints the id.
        """
        if line == "" or line is None:
            self.display("class name missing")
        elif line not in storage.classes():
            self.display("class doesn't exist")
        else:
            model = storage.classes()[line]()
            model.save()
            print(model.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        if line == "" or line is None:
            self.display("class name missing")
        else:
            instance = line.split(' ')

            if instance[0] not in storage.classes():
                self.display("class doesn't exist")
            elif len(instance) < 2:
                self.display("instance id missing")
            else:
                key = "{}.{}".format(instance[0], instance[1])
                if key not in storage.all():
                    self.display("no instance found")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        if line == "" or line is None:
            self.display("class name missing")
        else:
            instance = line.split(' ')
            if instance[0] not in storage.classes():
                self.display("class doesn't exist")
            elif len(instance) < 2:
                self.display("instance id missing")
            else:
                key = "{}.{}".format(instance[0], instance[1])
                if key not in storage.all():
                    self.display("no instance found")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances.
        """
        if line != "":
            instance = line.split(' ')
            if instance[0] not in storage.classes():
                self.display("class doesn't exist")
            else:
                x = []
                for key, obj in storage.all().items():
                    if type(obj).__name__ == instance[0]:
                        x.append(str(obj))
                print(x)
        else:
            new_list = []
            for key, obj in storage.all().items():
                new_list.append(str(obj))
            print(new_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        instance = " ".join(line.split())
        instance = instance.split(' ')

        if not line:
            self.display("class name missing")
            return

        classname = instance[0] if len(instance) > 0 else None
        uid = instance[1] if len(instance) > 1 else None
        attribute = instance[2] if len(instance) > 2 else None
        value = instance[3] if len(instance) > 3 else None
        print(classname)

        if classname not in storage.classes():
            self.display("class doesn't exist")
            return

        if not uid:
            self.display("instance id missing")
            return

        key = "{}.{}".format(classname, uid)
        if key not in storage.all():
            self.display("no instance found")
            return

        if not attribute:
            self.display("attribute name missing")
            return

        if not value:
            self.display("value missing")
            return

        value = value.replace('"', '')
        attributes = storage.attributes()[classname]
        if attribute not in attributes:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass

        if attribute in attributes:
            value = attributes[attribute](value)

        setattr(storage.all()[key], attribute, value)
        storage.all()[key].save()

    def update_from_dict(self, classname, uid, input_dict):
        """
        Updates an instance based on its ID with a dictionary
        """
        string = input_dict.replace("'", '"')
        ob = json.loads(string)
        if not classname:
            self.display("class name missing")
        elif classname not in storage.classes():
            self.display("class doesn't exist")
        elif uid is None:
            self.display("instance id missing")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                self.display("no instance found")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in ob.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_count(self, line):
        """
        Retrieves the number of instances of a class
        """
        instance = line.split(' ')
        if not instance[0]:
            self.display("class name missing")
            return

        classname = instance[0]
        if classname not in storage.classes():
            self.display("class doesn't exist")
            return

        instance_counter = 0
        for key in storage.all().keys():
            if key.startswith(classname + '.'):
                instance_counter += 1

        print(instance_counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
