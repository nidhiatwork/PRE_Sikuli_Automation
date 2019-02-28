import os,sys
import time
from pathlib import Path

tech = sys.argv[1]
# tech = "Cognitec"
print("Technology is: " + tech)
sys.stdout.flush()
os.system("killall 'Terminal'")

PRE_FD_location = "/Applications/Adobe Premiere Elements 2019/Support Files/Adobe Premiere Elements dev.app"
PRE_orig_location = "/Applications/Adobe Premiere Elements 2019/Support Files/Adobe Premiere Elements orig.app"
PRE_GM_location = "/Applications/Adobe Premiere Elements 2019/Support Files/Adobe Premiere Elements.app"
AA_FD_location = "/Applications/Adobe Elements 2019 Organizer.app/Contents/Elements Auto Creations 2019 dev.app"
AA_orig_location = "/Applications/Adobe Elements 2019 Organizer.app/Contents/Elements Auto Creations 2019 orig.app"
AA_GM_location = "/Applications/Adobe Elements 2019 Organizer.app/Contents/Elements Auto Creations 2019.app"

if tech=="Cognitec":
    if Path(PRE_orig_location).exists():
        print("Found Mona Settings for PRE. Changing back to Cognitec")
        sys.stdout.flush()
        os.rename(PRE_GM_location, PRE_FD_location)
        time.sleep(1)
        os.rename(PRE_orig_location, PRE_GM_location)
        time.sleep(1)
    if Path(AA_orig_location).exists():
        print("Found Mona Settings for AA. Changing back to Cognitec")
        sys.stdout.flush()
        os.rename(AA_GM_location, AA_FD_location)
        time.sleep(1)
        os.rename(AA_orig_location, AA_GM_location)
        time.sleep(1)
if tech=="Mona":
    if Path(PRE_FD_location).exists():
        print("Found Cognitec Settings for PRE. Changing back to Mona")
        sys.stdout.flush()
        os.rename(PRE_GM_location, PRE_orig_location)
        time.sleep(1)
        os.rename(PRE_FD_location, PRE_GM_location)
        time.sleep(1)
    if Path(AA_FD_location).exists():
        print("Found Cognitec Settings for AA. Changing back to Mona")
        sys.stdout.flush()
        os.rename(AA_GM_location, AA_orig_location)
        time.sleep(1)
        os.rename(AA_FD_location, AA_GM_location)
        time.sleep(1)

print("Completed setting build paths for technology: " + tech)
sys.stdout.flush()
