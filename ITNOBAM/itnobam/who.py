#!/usr/bin/python3
# -*- coding: utf-8 -*-
# who.py 

import os
import sys

# Note - once finalised, use the following line
#            import aikif.lib.cls_context as context
# but for now add in the path and use local copy
root_folder = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..") ) 
root_folder = r'U:\dev\src\python'
pth = os.path.join(root_folder, 'AIKIF', 'aikif' )
sys.path.append(pth)

import core_data

def TEST():
    p = People()
    print(p)
    
    fam = p.get_family()
    print(fam)

class People:
    """
    manages all the people user has contact with 
    """
    def __init__(self):
        everyone = core_data.CoreDataWho('Everyone')
        family = core_data.CoreDataWho('Family',  parent=everyone)
        carers = core_data.CoreDataWho('Carers',  parent=everyone)
        friends = core_data.CoreDataWho('Friends',  parent=everyone)


        self.people = []
        self.people.append(core_data.CoreDataWho('Me',   ['Frank',  'Physical', 'Self'],    parent=everyone))
        self.people.append(core_data.CoreDataWho('Wife', ['Maggie', 'Physical', 'Family'],  parent=family))
        self.people.append(core_data.CoreDataWho('Son',  ['George', 'Physical', 'Family'],  parent=family))
        self.people.append(core_data.CoreDataWho('Doctor',  ['Doctor Nick', 'Physical', 'Carer'],  parent=carers))
        self.people.append(core_data.CoreDataWho('John',  ['John', 'Physical', 'Friend'],  parent=friends))
        self.people.append(core_data.CoreDataWho('Jane',  ['Jane', 'Physical', 'Friend'],  parent=friends))
    
    def __str__(self):
        res = ''
        for p in self.people:
            res += p.format_dict() + '\n'
        
        return res

    
    def get_family(self):
        res = []
        for p in self.people:
            if p.data[2] == 'Family':
                res.append(p.name)
                
        return res
    
    
if __name__ == '__main__':
    TEST()