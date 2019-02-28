from sikuli import *
import os, sys
import traceback
from TestScripts import Constants as Constants
reload(Constants)

if len(sys.argv)>3:
        Technology = sys.argv[2]
        Mode = sys.argv[3]
else:
        Technology = Constants.Tech
        Mode = Constants.M

def close_AA_PRE_And_Launch_AA_PRE():

        print "Technology is: " + Technology + " and Mode is: " + Mode
        setAutoWaitTimeout(60)
        
        print "\n~~~~~~~~Closing Auto creations~~~~~~~~"
        os.system("sh " + Constants.BatFilesFolder + "Mac_Kill_AA.sh")
        os.system("sh " + Constants.BatFilesFolder + "Mac_Kill_PRE.sh")
        os.system("open -a Terminal")
        # wait(2)
        # type("n", Key.CMD)
        wait(2)
        type("sh ~/Desktop/LaunchAA.sh")
        type(Key.ENTER)
        wait(2)
        type("n", Key.CMD)
        wait(2)
        type("sh ~/Desktop/LaunchPRE.sh")
        type(Key.ENTER)
        wait(1)
        type("`", Key.CMD)
        wait(1)
        setAutoWaitTimeout(30)

def closePRE():
        print "~~~~~~~~Closing any open instance of PRE application~~~~~~~~"
        os.system("sh " + Constants.BatFilesFolder + "Mac_Kill_PRE.sh")
        wait(3)

def launchAA():
        print "~~~~~~~~~~Launching AA ~~~~~~~~~~~~~~"
        os.system("open -a Terminal") 
        type("n", Key.CMD)
        type("sh ~/Desktop/LaunchAA.sh")
        type(Key.ENTER)
        wait(2)

def get_files_by_file_size(dirname, reverse=False):
    # Get list of files
    filepaths = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isfile(filename):
            filepaths.append(basename)

    # Re-populate list with filename, size tuples
    for i in xrange(len(filepaths)):
        filepaths[i] = (filepaths[i], os.path.getsize(dirname+filepaths[i]))

    # Sort list by file size
    # If reverse=True sort from largest to smallest
    # If reverse=False sort from smallest to largest
    filepaths.sort(key=lambda filename: filename[1], reverse=reverse)

    # Re-populate list with just filenames
    for i in xrange(len(filepaths)):
        filepaths[i] = filepaths[i][0]

    return filepaths

def findElement( element ):       
        print "Finding element: " + str(element)
        try:
                find(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to find element: " + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def clickElement( element ):
        print "Clicking on element: " + str(element)
        try:
                
                click(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to click element: " + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def doubleClickElement( element ):
        print "Double clicking on element: " + str(element)
        try:                
                doubleClick(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to double click element: " + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def assertElementExists( element ):
        print "Asserting whether element exists: " + str(element)
        if not exists(element):
                stack = traceback.extract_stack(limit = 2)
                print "Unable to assert image exists: " + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False

def hoverElement( element ):       
        print "Hovering on element: " + str(element)
        try:
                
                hover(element)
        except:
                stack = traceback.extract_stack(limit = 2)
                print "Unable to hover on element: " + str(element) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
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
                print "Unable to drag and drop: " + str(sourceImg) + " to " + str(destImg) + "\nBelow are exception details:\n" + str(sys.exc_info()[0]) + " -- line no. " + str(stack[0][1])
                assert False
