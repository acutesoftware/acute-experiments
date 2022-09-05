#!/usr/bin/python3
# -*- coding: utf-8 -*-
# run_tests.py

import os
import glob
import time
import unittest as unittest

# run all tests in tests folder
all_tests = unittest.TestLoader().discover('.', pattern='test*.py')
unittest.TextTestRunner().run(all_tests)    
