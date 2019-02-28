import utils
reload(utils)
from utils import *
import os
import sys
import unittest
import shutil
import datetime

class TestPRE_FaceDetection(unittest.TestCase):

    def setUp(self):
        close_AA_PRE_And_Launch_AA_PRE()

    def test_UI_FaceDetection(self):
        setAutoWaitTimeout(60)
        wait(5)
        os.system("osascript -e 'tell application \"Adobe Premiere Elements\" to activate'")
        wait(2)
        doubleClickElement("Close.png")
        wait(1)
        os.chdir(Constants.CollectionFolder)
        setAutoWaitTimeout(60)
        i=1
        l = get_files_by_file_size(Constants.CollectionFolder)
        for filename in l:
            try:
                os.remove(Constants.Video_CALogs)
            except:
                print("Log files already removed.")
            try:
                os.remove(Constants.Image_FaceInfoLogs)
            except:
                print("Log files already removed.")
            try:
                os.remove(Constants.Video_timerLogs)
            except:
                print("Log files already removed.")

            if filename.find(".")==0:
                continue
            now = datetime.datetime.now()
            postfix = str(now.day) + str(now.month) + str(now.year) + "_" + str(now.hour) + str(now.minute) + str(now.second)
            if Mode == "Image":
                newfilename = "Image#" + str(i) + "_"+ postfix + filename[filename.find("."):]
            else:
                newfilename = "Video#" + str(i) + "_"+ postfix + filename[filename.find("."):]

            shutil.copy(Constants.CollectionFolder+filename,Constants.CollectionFolder+newfilename)
            os.remove(Constants.CollectionFolder+filename)
            print "Filename changed from " + filename + " to " + newfilename           
            # wait(2)
            type('i', KeyModifier.CMD)
            wait(1)
            clickElement("Search.png")
            wait(1)
            type(newfilename)
            type(Key.ENTER)
            wait(2)
            setAutoWaitTimeout(18)
            if Mode=="Image":
                if exists(Pattern("Image_Number.png").similar(0.85)):
                    doubleClickElement(Pattern("Image_Number.png").similar(0.85))
                else:
                    print "Test data not found in system directory. Skipping to next test data."
                    os.system("python " + Constants.BatFilesFolder + "ReadFacesAndTakeScreenshot.py '" + newfilename + "' '" + Mode + "' '" + Technology + "'")
                    type(Key.ESC)
                    wait(1)
                    type(Key.ESC)
                    wait(1)
                    i = i+1
                    continue
            else:
                if exists(Pattern("Video.png").similar(0.85)):
                    doubleClickElement(Pattern("Video.png").similar(0.85))
                else:
                    print "Test data not found in system directory. Skipping to next test data."
                    os.system("python " + Constants.BatFilesFolder + "ReadFacesAndTakeScreenshot.py '" + newfilename + "' '" + Mode + "' '" + Technology + "'")
                    type(Key.ESC)
                    wait(1)
                    type(Key.ESC)
                    wait(1)
                    i = i+1
                    continue
            wait(2)
            os.system("killall 'Elements Auto Creations 2019'")
            print("Launching AA again to ensure process is running")
            os.system("open -a Terminal")
            wait(2)
            os.system("osascript -e 'tell application \"Terminal\" to activate'")
            setAutoWaitTimeout(60)
            wait(1)
            type(Key.UP)
            # type("n", Key.CMD)
            # wait(2)
            # type("sh ~/Desktop/LaunchAA.sh")
            type(Key.ENTER)                 
            wait(2)
            os.system("osascript -e 'tell application \"Adobe Premiere Elements\" to activate'")
            wait(1)
            clickElement("Tools.png")
            if Mode=="Image":
                clickElement("PanZoomTool.png")
                setAutoWaitTimeout(15)
                if exists("Done.png"):
                    print "Pan and zoom workflow complete."
                    os.system("python " + Constants.BatFilesFolder + "ReadFacesAndTakeScreenshot.py '" + newfilename + "' '" + Mode + "' '" + Technology + "'" )
                    clickElement("Done.png")
                elif exists(Pattern(Pattern("AutoAnalyzerError.png").similar(0.80)).similar(0.80)):
                    os.system("python " + Constants.BatFilesFolder + "ReadFacesAndTakeScreenshot.py '" + newfilename + "' '" + Mode + "' '" + Technology + "'")
                    print "Auto AA error appeared on screen. Trying to handle..."
                    type(Key.ESC)
                    wait(1)
                    type(Key.ESC)
                    wait(1)
                    clickElement(Pattern("Done.png").similar(0.90))
                elif exists(Pattern("FocusFrameError.png").similar(0.80)):
                    os.system("python " + Constants.BatFilesFolder + "ReadFacesAndTakeScreenshot.py '" + newfilename + "' '" + Mode + "' '" + Technology + "'")
                    print "Focus frames error appeared on screen. Trying to handle..."
                    type(Key.ESC)
                    wait(1)
                    type(Key.ESC)
                    wait(1)
                    clickElement(Pattern("Done.png").similar(0.90))
                setAutoWaitTimeout(30)
            else:
                clickElement("SmartTrim.png")
                wait(1)
                clickElement("ShowPresets.png")
                wait(1)
                clickElement("People_Preset.png")
                wait(1)
                type(Key.ENTER)
                wait(2)
                setAutoWaitTimeout(3600)
                if exists(Pattern("Playbar.png").similar(0.79)):
                    os.system("python " + Constants.BatFilesFolder + "ReadFacesAndTakeScreenshot.py '" + newfilename + "' '" + Mode + "' '" + Technology + "'" )
                    wait(2)
                    click("CloseWindow.png")
                    clickElement("No_button.png")
                    # clickElement("ContinueEditing.png")
                else:
                    type(Key.ENTER)
                    os.system("python " + Constants.BatFilesFolder + "ReadFacesAndTakeScreenshot.py '" + newfilename + "' '" + Mode + "' '" + Technology + "'" )
                    click("CloseWindow.png")
                    clickElement("No_button.png")
                    type('n', KeyModifier.CMD)
                    findElement("No_button.png")
                    clickElement("No_button.png")
                    wait(1)
                    type(Key.ESC)
                    doubleClickElement("Close.png")
                    
                setAutoWaitTimeout(60)
                
                
            # type('n', KeyModifier.CMD)
            # findElement("No_button.png")
            # clickElement("No_button.png")
            # wait(1)
            # type(Key.ESC)
            # doubleClickElement("Close.png")
            wait(1)
            print "Completed screenshot taking process for file: " + newfilename
            i = i+1
            os.system("killall 'Elements Auto Creations 2019'")
            wait(2)
    def tearDown(self):
       closePRE()