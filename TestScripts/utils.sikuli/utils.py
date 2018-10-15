from sikuli import *
import os, sys
import traceback
from TestScripts import Constants as Constants
reload(Constants)
import BaselineImages
reload(BaselineImages)

def cleanCache_And_LaunchPRE():
        
        setAutoWaitTimeout(60)
        
        print "\n~~~~~~~~Cleaning cache files and launching PRE application~~~~~~~~"
        os.system("sh " + Constants.BatFilesFolder + "Mac_Kill_PRE.sh")
        os.system("open '" + Constants.AppPath_PRE + "'")
        
        try:
                setBundlePath(Constants.BaselineFolder)
                find(Pattern("Button_GoalScreen_CloseGoalScreen.png").similar(0.80))
                wait(3)
        except:
                print("Unable to launch PRE application after waiting for 60 seconds. End of execution.")
                closePRE()
                sys.exit(0)

        setAutoWaitTimeout(15)

def closePRE():
        print "~~~~~~~~Closing any open instance of PRE application~~~~~~~~"
        os.system("sh " + Constants.BatFilesFolder + "Mac_Kill_PRE.sh")
        wait(3)

def findElement( element ):       
        print "Finding element: " + str(element)
        try:
                
                find(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to find element: " + Constants.BaselineFolder + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def clickElement( element ):
        print "Clicking on element: " + str(element)
        try:
                
                click(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to click element: " + Constants.BaselineFolder + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def doubleClickElement( element ):
        print "Double clicking on element: " + str(element)
        try:
                
                doubleClick(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to double click element: " + Constants.BaselineFolder + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def assertElementExists( element ):
        print "Asserting whether element exists: " + str(element)
        if not exists(element):
                stack = traceback.extract_stack(limit = 2)
                print "Unable to assert image exists: " + Constants.BaselineFolder + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def hoverElement( element ):       
        print "Hovering on element: " + str(element)
        try:
                
                hover(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to hover on element: " + Constants.BaselineFolder + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def typeKeys( data ):
        print "Typing: " + str(data)
        try:

                type(data)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to type: " + str(data) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False


def dragAndDropElement( sourceImg, destImg ):       
        print "Dragging and dropping: " + str(sourceImg) + " to " + str(destImg)
        try:
                clickElement(sourceImg)
                mouseDown(Button.LEFT)
                mouseMove(4,4)
                wait(1)
                mouseMove(sourceImg)
                wait(1)
                mouseMove(destImg)
                wait(1)
                mouseUp()

        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to drag and drop: " + Constants.BaselineFolder + str(sourceImg) + " to " + Constants.BaselineFolder + str(destImg) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False
