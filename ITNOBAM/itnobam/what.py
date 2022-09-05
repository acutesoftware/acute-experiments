#!/usr/bin/python3
# -*- coding: utf-8 -*-
# what.py 

import os
import sys

things = [
    'chair',
    'bed',
    'TV',
    'Computer',
    'Mobile',
    ]
    
    
def main():
    """
    main function used for testing 
    """
    print('todo')

def what_is_that(thing_to_identify):
    if type(thing_to_identify) is str:
        return 'Furniture'
    else:
        return 'TODO'