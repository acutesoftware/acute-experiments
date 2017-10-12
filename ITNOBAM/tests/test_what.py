#!/usr/bin/python3
# coding: utf-8
# test_what.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "itnobam" )

sys.path.append(root_fldr)
import what


class WhatTest(unittest.TestCase):

    def test_01_what(self):
        res = what.what_is_that('Chair')
        print(res)
        self.assertEqual(res, 'Furniture')

    
if __name__ == '__main__':
    unittest.main()

