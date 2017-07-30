#!/usr/bin/python3
# coding: utf-8
# test_where.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "itnobam" )

sys.path.append(root_fldr)
import where


class ConfigTest(unittest.TestCase):

    def test_01_areas(self):
        
        loc = where.where_am_i()
        #print('loc=', loc)
        self.assertTrue(len(loc), 'Home')

     
if __name__ == '__main__':
    unittest.main()

