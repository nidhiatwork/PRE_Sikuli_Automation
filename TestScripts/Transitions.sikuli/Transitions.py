import utils
reload(utils)
from utils import *
import os
import sys
import unittest

class TestTransitions(unittest.TestCase):

    def setUp(self):       
        utils.cleanCache_And_LaunchPRE()
        
    def test_UI_Transitions(self):
        print "haha"
        pass
        
    def tearDown(self):
        print "teardown"