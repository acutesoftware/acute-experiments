#!/usr/bin/python3
# -*- coding: utf-8 -*-
# why.py 

import os
import sys

import who
import what
import where

scenarios = [
    {'name':'memory loss'},
    {'name':'lack of movement'},
    {'name':'mild confusion'},
    ]
            

preferred_outcome = [
    'cognitive ability',
    'physical freedom',
    'financial independance',
    ]
    
    
path_to_solve = []
 


 
            
def main():
    """
    main function used for testing 
    """
    print(why_did_that_happen(scenarios[0]))
 

def why_did_that_happen(scenario):
    """
    uses the other modules with sensors to try 
    and identify why the 'scenario' occurred.
    """
    print('calculating best response why ' + scenario['name'] + ' occurred')
    
    loc = where.which_room_am_i_in()
    
    print('loc = ' + loc)
    
    if loc == 'Bedroom':
        return 'You just woke up'
    
    
    return 'No idea'
   
    
    
    
    

    
    
main()
