#!/usr/bin/python3
# -*- coding: utf-8 -*-
# who.py 

import os
import sys

# Note - once finalised, use the following line
#            import aikif.lib.cls_context as context
# but for now add in the path and use local copy
root_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..") ) 
pth = os.path.join(root_folder, 'AIKIF', 'aikif' )
sys.path.append(pth)

import core_data

def main():
    """
    main function used for testing 
    """
    everyone = core_data.CoreDataWho('Everyone')
    family = core_data.CoreDataWho('Family',  parent=everyone)
    carers = core_data.CoreDataWho('Carers',  parent=everyone)
    friends = core_data.CoreDataWho('Friends',  parent=everyone)


    people = []
    people.append(core_data.CoreDataWho('Me',   ['Frank',  'Physical', 'Self'],    parent=everyone))
    people.append(core_data.CoreDataWho('Wife', ['Maggie', 'Physical', 'Family'],  parent=family))
    people.append(core_data.CoreDataWho('Son',  ['George', 'Physical', 'Family'],  parent=family))
    people.append(core_data.CoreDataWho('Doctor',  ['Doctor Nick', 'Physical', 'Carer'],  parent=carers))
    people.append(core_data.CoreDataWho('John',  ['John', 'Physical', 'Friend'],  parent=friends))
    people.append(core_data.CoreDataWho('Jane',  ['Jane', 'Physical', 'Friend'],  parent=friends))
    
    
    for p in people:
        print(p.format_dict())
    


    
if __name__ == '__main__':
    main()