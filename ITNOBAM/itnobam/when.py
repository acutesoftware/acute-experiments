#!/usr/bin/python3
# -*- coding: utf-8 -*-
# when.py 

import os
import sys

# Note - once finalised, use the following line
#            import aikif.lib.cls_context as context
# but for now add in the path and use local copy
root_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..") ) 
root_folder = r'U:\dev\src\python'
pth = os.path.join(root_folder, 'AIKIF', 'aikif', 'lib' )
sys.path.append(pth)
import cls_context as context

ontology_time = [
    {'name':'now', 'date_diff':0},
    {'name':'soon', 'date_diff':2},
    {'name':'later', 'date_diff':5},
    {'name':'next week', 'date_diff':7},
    {'name':'at some stage', 'date_diff':20},
    ]
    
event_types = [
    'Birthday',
    'Christmas',
    'Party',
    'Relaxing',
    'Work',
    ]
    
    
def main():
    """
    main function used for testing 
    """
    print('todo')

main()