#!/usr/bin/python3
# -*- coding: utf-8 -*-
# where.py 

import os
import sys

# Note - once finalised, use the following line
#            import aikif.lib.cls_context as context
# but for now add in the path and use local copy
root_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..") ) 
pth = os.path.join(root_folder, 'AIKIF', 'aikif', 'lib' )
sys.path.append(pth)
import cls_context as context


def main():
    """
    main function used for testing 
    """
    where_am_i()



def where_am_i():
    """
    this script works out where the user is 
    """
    
    # get the standard base line of a users location via GPS
    me = context.where_am_i()
    
    # expand this with details on room/chair via sensors
    
    # 
    
    
    return me
    
    

    
if __name__ == '__main__':
    unittest.main()