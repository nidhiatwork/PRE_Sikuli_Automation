import utils
reload(utils)
from utils import *
import os
import sys
from sikuli import *
import unittest

class TestEffects(unittest.TestCase):

    def setUp(self):       
        utils.cleanCache_And_LaunchPRE()
                  
    def test_UI_Effects(self):
        print "effects"
        pass
        
    def tearDown(self):
       utils.closePRE()        

