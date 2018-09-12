import os, sys, platform
from sikuli import *


AppPath_PRE = "//Applications//Adobe Premiere Elements 2019//Support Files//Adobe Premiere Elements.app"
userdir = os.path.expanduser('~')

RootFolder = userdir + "/Desktop/PRE_Sikuli_Automation"
BaselineFolder = RootFolder + "/BaselineImages/"
OutputFolder = RootFolder + "/Output/"
TestDataFile_path = RootFolder + "/TestData/test.mp4"
Sikuli_Path = userdir + "/Downloads"
PRE_Test_Execution_Data = RootFolder + "/TestData/PRE_Test_Execution_Data.xls"
ScreenshotsFolder = OutputFolder + "Screenshots"