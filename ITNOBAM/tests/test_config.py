#!/usr/bin/python3
# coding: utf-8
# test_config.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "itnobam" )

sys.path.append(root_fldr)
import itnobam_config as config
import json

class ConfigTest(unittest.TestCase):

    def test_01_areas(self):
        self.assertTrue(len(config.areas) > 4)
        print(json.dumps(config.areas, indent=2, sort_keys=True))

    def test_02_people(self):
        self.assertTrue(len(config.people) > 1)
        print(json.dumps(config.people, indent=2, sort_keys=True))
   
    
if __name__ == '__main__':
    unittest.main()

