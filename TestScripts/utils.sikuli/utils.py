from sikuli import *
import os, sys
import traceback
from TestScripts import Constants as Constants

def cleanCache_And_LaunchPRE():
        print "\n~~~~~~~~Cleaning cache files and launching PRE application~~~~~~~~"
        os.system("sh " + Constants.RootFolder + "/BatFiles/Mac_Kill_PRE.sh")
        os.system("open '/Applications/Adobe Premiere Elements 2019/Support Files/Adobe Premiere Elements.app'")
        
        setAutoWaitTimeout(60)


        print getBaselineImg('Button_GoalScreen_CloseGoalScreen.png')
        click("/Users/nbhushan/Desktop/Button_GoalScreen_CloseGoalScreen.png")
        
       # click('/Users/nbhushan/Desktop/Button_GoalScreen_CloseGoalScreen.png')

        

        setAutoWaitTimeout(15)

def closePRE():
        os.system("sh " + Constants.RootFolder + "/BatFiles/Mac_Kill_PRE.sh")

def getBaselineImg( img_name ):
        return Constants.BaselineFolder+ img_name
        
def findElement( element ):       
        element_name = getElementNameFromFullPath(element)
        print "Finding element: " + element_name
        try:
                find(element)
        except:
                        stack = traceback.extract_stack(limit = 2)
                        print "Unable to find element: " + element_name + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                        raise

def clickElement( element ):
        element_name = getElementNameFromFullPath(element)
        print "Clicking on element: " + element_name
        try:
                click(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to click element: " + element_name + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise

def assertElementExists( element ):
        element_name = getElementNameFromFullPath(element)
        print "Asserting whether element exists: " + element_name
        try:
                assert(exists(element))
        except AssertionError:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to assert image exists: " + element_name + "\nBelow are details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                raise

def getElementNameFromFullPath( image_path ):
        element_path_list = image_path.split("//")
        image_item = element_path_list[len(element_path_list)-1]
        return image_item