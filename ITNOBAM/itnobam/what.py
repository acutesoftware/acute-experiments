#!/usr/bin/python3
# -*- coding: utf-8 -*-
# what.py 

import os
import sys

# Note - once finalised, use the following line
#            import aikif.lib.cls_context as context
# but for now add in the path and use local copy
root_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..") ) 
pth = os.path.join(root_folder, 'AIKIF', 'aikif', 'environments' )
sys.path.append(pth)
import room as env
pth2 = os.path.join(root_folder, 'AIKIF', 'aikif', 'lib' )
sys.path.append(pth2)
import cls_context as context

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

