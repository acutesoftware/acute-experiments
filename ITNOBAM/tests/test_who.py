#!/usr/bin/python3
# coding: utf-8
# test_who.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "itnobam" )

sys.path.append(root_fldr)
import who

class WhoTest(unittest.TestCase):

    def test_01_who(self):
        p = who.People()

        print(p)

        #self.assertEqual(loc, 'HomeBedroom')

        
    def test_02_family(self):
        p = who.People()
        fam = p.get_family()
        self.assertEqual(fam, ['Wife', 'Son'])
        print('Family = ', fam)    
     
if __name__ == '__main__':
    unittest.main()

