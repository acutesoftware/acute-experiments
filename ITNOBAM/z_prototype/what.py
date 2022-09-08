#!/usr/bin/python3
# -*- coding: utf-8 -*-
# what.py 

import os
import sys
import random

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
    viewpoint = 'Lounge - looking North'
    res = get_object_at_location(viewpoint)
    print('This is a ' + res)

def get_object_at_location(viewpoint):
    """
    gets the object visible in focus of the main front camera of the user
    """
    print('Identifying object at ' + str(viewpoint))
    

    return random.choice(things)

main()