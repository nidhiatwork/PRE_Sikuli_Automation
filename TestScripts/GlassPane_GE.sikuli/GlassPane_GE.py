import utils
reload(utils)
from utils import *
import os
import sys
import unittest

class TestGlassPane_GE(unittest.TestCase):

    def setUp(self):       
        utils.cleanCache_And_LaunchPRE()
        
    def test_UI_GlassPane_GE(self):
        print "haha"
        pass
        

    def tearDown(self):
       utils.closePRE()        

