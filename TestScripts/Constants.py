import os, sys, platform
from sikuli import *

AppPath_PRE = "/Applications/Adobe Premiere Elements 2019/Support Files/Adobe Premiere Elements.app/Contents/MacOS/Adobe Premiere Elements"
AAPath = "/Applications/Adobe Elements 2019 Organizer.app/Contents/Elements Auto Creations 2019.app/Contents/MacOS/Elements Auto Creations 2019"
userdir = os.path.expanduser('~')

RootFolder = userdir + "/Desktop/FD_Automation"
OutputFolder = RootFolder + "/Output/"
Sikuli_Path = userdir + "/Downloads"
FD_Test_Execution_Data = RootFolder + "/TestData/FD_Test_Execution_Data.xls"
ScreenshotsFolder = OutputFolder + "Screenshots"
BatFilesFolder = RootFolder + "/BatFiles/"
CollectionFolder = RootFolder + "/Collection/"
Video_CALogs = userdir + "/Documents/Adobe/Elements Organizer/17.0/CALog.log"
Image_FaceInfoLogs = userdir + "/Documents/Adobe/Elements Organizer/17.0/FaceInfo.log"
Video_timerLogs = userdir + "/Documents/Adobe/Premiere Elements/17.0/timerlog.log"
# Tech = "Cognitec"
Tech = "Mona"
# M = "Image"
M = "Video"