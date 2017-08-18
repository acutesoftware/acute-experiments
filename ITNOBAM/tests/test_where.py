#!/usr/bin/python3
# coding: utf-8
# test_where.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "itnobam" )

sys.path.append(root_fldr)
import where


class WhereTest(unittest.TestCase):

    def test_01_whereami(self):
        
        loc = where.where_am_i()
        print('loc=', loc)
        self.assertEqual(loc, 'HomeBedroom')

    def test_02_environment(self):
        
        #e = where.environment.Environment('test_where')
        #self.assertEqual(str(e), 'Environment: test_where\n')
        #print(e)
        e = where.setup_environments()
        print(e)
     
if __name__ == '__main__':
    unittest.main()

