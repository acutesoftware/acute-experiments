#!/usr/bin/python3
# -*- coding: utf-8 -*-
# brain.py 

"""
This is the main brain of the AI that determines the general
list of tasks to perform.

It can be run on a PC, robot, sensor and the first thing it does
is confirm with 'base' (?) about the goals for THIS instance.

The brain does 
"""

import sys
import time
from config import valid_lists

def main():
    my_def = load_definition()
    # we have a valid definition, so start up now
    my_name = my_def.robot_name   

    my_def.generate_output('hello, my name is ' + my_name)

    while(1):
        ip = my_def.read_input()
        if str(ip) == ':q!':
            print('shutting down')
            exit(0)
        
        my_def.process_command(ip)
        time.sleep(my_def.poll_frequency)


def load_definition():
    if len(sys.argv) != 2:
        raise ValueError('Please provide definition file as command line argument (e.g. def_console or def_robot)')
    
    print(f'Script Name is {sys.argv[0]}')
    
    def_name = sys.argv[1]    
    if def_name not in valid_lists.all_bots:
        raise ValueError('Not a valid bot definition')


    # should use import based on name, but for now a quick and dirty hack 
    if def_name == 'def_robot':
        from config import def_robot as my_def

    if def_name == 'def_console':
        from config import def_console as my_def

    if not my_def:
        raise ValueError('invalid definition')


    for op in my_def.outputs:
        if op not in valid_lists.all_outputs:
            raise ValueError('invalid output defined ' + op)


    return my_def




main()