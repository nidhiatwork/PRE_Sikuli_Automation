from sikuli import*
import HTMLTestRunner 
reload(HTMLTestRunner)
import unittest
import os,sys
import xlrd
import datetime

userdir = os.path.expanduser('~')
userdir.replace("//", "////")
RootFolder = userdir + "/Desktop/PRE_Sikuli_Automation"

if not RootFolder in sys.path: 
    sys.path.append(RootFolder)

from TestScripts import Constants as Constants
from Effects import *
from Transitions import *
from GlassPane_GE import *

workbook = xlrd.open_workbook(Constants.PRE_Test_Execution_Data)
worksheet = workbook.sheet_by_index(0)

testcase_list = []
for row in range(worksheet.nrows):
    area_flag = worksheet.cell(row, 3).value
    if area_flag == 1:
        testcase_list.append(worksheet.cell(row, 1).value)

suite = unittest.TestSuite()

for testcase in testcase_list:
    if testcase == "Effects":
        suite.addTest(TestEffects("test_UI_Effects"))
    elif testcase == "Transitions":
        suite.addTest(TestTransitions("test_UI_Transitions"))
    elif testcase == "GlassPane_GE":
        suite.addTest(TestGlassPane_GE("test_UI_GlassPane_GE"))

now = datetime.datetime.now()
outputfilename = Constants.RootFolder + "//Output//TestReport_" + str(now.day) + str(now.month) + str(now.year) + "_" + str(now.hour) + str(now.minute) + str(now.second) + ".html"
outfile = file(outputfilename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='PRE UI Tests Execution Report', description='This is test report for test execution of UI tests for Premiere Elements application.' )
runner.run(suite)