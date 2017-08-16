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

places = [
    'home',
    'work',
    'sons house',
    'daughters house',
    'friend#1',
    'friend#2',
    'friend#3',
    'restaurant#1',
    'restaurant#2',
    'restaurant#3',
    'park',
    'beach',
    'doctors',
    'hospital',
    ]
    

home = [
    'lounge',
    'kitchen',
    'bedroom',
    'spare room',
    'front yard',
    'back yard',
    'garage'
    ]
    
    
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
    me += which_room_am_i_in()
    
    return me

    
def which_room_am_i_in():
    """
    uses the monitor module to determine which room the user is in
    """
    import monitor
    s = monitor.Sensors()
    s.scan()
    return s.which_room_am_i_in()
   
    
    
    return me
    
    

    
if __name__ == '__main__':
    unittest.main()