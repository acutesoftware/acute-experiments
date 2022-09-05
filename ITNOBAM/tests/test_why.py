#!/usr/bin/python3
# coding: utf-8
# test_why.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "itnobam" )

sys.path.append(root_fldr)
import why


class WhyTest(unittest.TestCase):

    def test_01_why(self):
        res = why.why_did_that_happen(why.scenarios[0])
        print(res)
        self.assertEqual(res, 'You just woke up')

    
if __name__ == '__main__':
    unittest.main()

