import os,sys
import time
from pathlib import Path

Mode = sys.argv[1]
print "Mode is: " + Mode
sys.stdout.flush()

PRE_FD_location = "/Applications/Adobe Premiere Elements 2019/Support Files/Adobe Premiere Elements dev.app"
PRE_orig_location = "/Applications/Adobe Premiere Elements 2019/Support Files/Adobe Premiere Elements orig.app"
PRE_GM_location = "/Applications/Adobe Premiere Elements 2019/Support Files/Adobe Premiere Elements.app"
AA_FD_location = "/Applications/Adobe Elements 2019 Organizer.app/Contents/Elements Auto Creations 2019 dev.app"
AA_orig_location = "/Applications/Adobe Elements 2019 Organizer.app/Contents/Elements Auto Creations 2019 orig.app"
AA_GM_location = "/Applications/Adobe Elements 2019 Organizer.app/Contents/Elements Auto Creations 2019.app"

os.system("killall 'Terminal'")

if Path(PRE_orig_location).exists():
    print "Found Mona Settings for PRE. Changing back to Cognitec"
    sys.stdout.flush()
    os.rename(PRE_GM_location, PRE_FD_location)
    os.rename(PRE_orig_location, PRE_GM_location)
if Path(AA_orig_location).exists():
    print "Found Mona Settings for AA. Changing back to Cognitec"
    sys.stdout.flush()
    os.rename(AA_GM_location, AA_FD_location)
    os.rename(AA_orig_location, AA_GM_location)

os.system("killall 'Terminal'")
time.sleep(2)
os.system("open -a Terminal")
os.system("java -jar '/Applications/SikuliX.app/Contents/Java/sikulix.jar' -r '/Users/nbhushan/Desktop/FD_Automation/TestScripts/TestDriver.sikuli' --args 'TestPRE_FaceDetection.test_UI_FaceDetection' \"Cognitec\" \"" + Mode + "\"")

print "Workflow completed with Cognitec technology for " + Mode
sys.stdout.flush()

time.sleep(5)

if Path(PRE_FD_location).exists():
    print "Found Cognitec Settings for PRE. Changing back to Mona"
    sys.stdout.flush()
    os.rename(PRE_GM_location, PRE_orig_location)
    os.rename(PRE_FD_location, PRE_GM_location)
if Path(AA_FD_location).exists():
    print "Found Cognitec Settings for AA. Changing back to Mona"
    sys.stdout.flush()
    os.rename(AA_GM_location, AA_orig_location)
    os.rename(AA_FD_location, AA_GM_location)

os.system("java -jar '/Applications/SikuliX.app/Contents/Java/sikulix.jar' -r '/Users/nbhushan/Desktop/FD_Automation/TestScripts/TestDriver.sikuli' --args 'TestPRE_FaceDetection.test_UI_FaceDetection' \"Mona\" \"" + Mode + "\"")

print "Workflow completed with Mona technology for " + Mode
sys.stdout.flush()
