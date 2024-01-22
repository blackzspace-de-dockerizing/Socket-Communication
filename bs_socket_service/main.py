#!/usr/bin/python3
# check dependencies before start
from .core.services import check_dependencies
check_dependencies()
import cmd
import os
import sys
import socket
import subprocess
import logging
import time
import threading
import json
import re
import shlex


from cmd import Cmd

HOST = "0.0.0.0"
PORT = 5333





from .mods import *
from .mods import module_list, all_modules
from .core.services import logo, update


completions = module_list()


class Main(cmd.Cmd):
    # check for update
    update(where="main_menu")

    intro = logo()
    cp = CPrint()

    prompt = 'wsf > '
    doc_header = 'Commands'
    undoc_header = 'Undocumented Commands'

    def do_use(self, line):
        """Select module for modules"""
        if line in module_list():

            module = globals()[line]
            if hasattr(module, 'Main'):
                module = module.Main()
                module.prompt = f"bS Sockez > {line} > "
                module.cmdloop()
            else:
                self.cp.error(text=f"*** Module `{module}` not has `Main` class!")

        else:
            self.cp.warning(text=f"*** Module {line} not found!")

    def do_show(self, line):
        """Show available modules"""
        all_modules()

    def do_exit(self, line):
        """Exit"""
        return True

    def complete_use(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in completions if s.startswith(mline)]

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        func = [getattr(self, n) for n in self.get_names() if n.startswith('do_' + cmd)]
        if func: 
            func[0](arg)
        else:
            os.system(line)

    def do_about(self, line):
        """About Us"""
        about()

    def do_update(self, line):
        """Check for update"""
        update(where="update_command")


def loop():
    try:
        Main().cmdloop()
    except KeyboardInterrupt:
        print("\nBye!")

if __name__ == '__main__':
    loop()
