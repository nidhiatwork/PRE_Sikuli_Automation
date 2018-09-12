from sikuli import *
import os, sys
import traceback
from TestScripts import Constants as Constants
reload(Constants)
import BaselineImages
reload(BaselineImages)

reg = Region()

def cleanCache_And_LaunchPRE():
        setAutoWaitTimeout(60)
        
        print "\n~~~~~~~~Cleaning cache files and launching PRE application~~~~~~~~"
        #os.system("sh " + Constants.RootFolder + "/BatFiles/Mac_Kill_PRE.sh")
        os.system("open '/Applications/Adobe Premiere Elements 2019/Support Files/Adobe Premiere Elements.app'")       
        
        try:
                setBundlePath(Constants.BaselineFolder)
                #find(Pattern("Button_GoalScreen_CloseGoalScreen.png").similar(0.80))
        except:
                print("Unable to launch PRE application after waiting for 60 seconds. End of execution.")
                closePRE()
                sys.exit(0)

        global reg
        reg = Region(App("Adobe Premiere Elements").window())
        reg.setAutoWaitTimeout(10)


def closePRE():
        #os.system("sh " + Constants.RootFolder + "/BatFiles/Mac_Kill_PRE.sh")
        pass
def findElement( element ):       
        print "Finding element: " + element
        try:
                with reg:
                        find(Pattern(element).similar(0.80))
        except:
                        stack = traceback.extract_stack(limit = 2)
                        print "Unable to find element: " + Constants.BaselineFolder + element + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                        raise

def clickElement( element ):
        print "Clicking on element: " + element
        try:
                with reg:
                        click(Pattern(element).similar(0.80))
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to click element: " + Constants.BaselineFolder + element + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise

def assertElementExists( element ):
        print "Asserting whether element exists: " + element
        try:
                with reg:
                        assert(exists(Pattern(element).similar(0.80)))
        except AssertionError:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to assert image exists: " + Constants.BaselineFolder + element + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise
