import pyautogui
from word2number import w2n
import os,sys
import time
userdir = os.path.expanduser('~')

name = str(sys.argv[1])
mode = str(sys.argv[2])
technology = str(sys.argv[3])

# name = "Video#1_2343.mp4"
# mode = "Video"
# technology = "Mona"

def main():
        timeTaken = -1
        total = -1
        if mode == "Image":
                LogFile = userdir + "/Documents/Adobe/Elements Organizer/17.0/FaceInfo.log"        
                if not os.path.exists(LogFile):
                    print("Face data log file for image not present!")
                else:
                        with open(LogFile) as f:
                                f = f.readlines()
                        print("Printing data from log file: \n" + str(f))
                        total = f[0].replace("Total: ", "")
                        total = total.replace("\n","")
                takeshot(technology, total, timeTaken)
        else:
                LogFile = userdir + "/Documents/Adobe/Elements Organizer/17.0/CALog.log"
                performanceLogFile = userdir + "/Documents/Adobe/Premiere Elements/17.0/timerlog.log"  
                if not os.path.exists(LogFile):
                    print("Face data log file for video not present!")
                else:
                        with open(LogFile) as f:
                                f = f.readlines()
                        # print("Printing data from log file: \n" + str(f))
                        start = "Tag Category  : Pan\n"
                        end = "Tag Category  : Number of Faces\n"

                        f.reverse()
                        faces = f[(f.index(start))+3:(f.index(end))]
                        print(' '.join(faces))
                        final = list()
                        for face in faces:
                                n = face.split("-")
                                final.append(n[1].split(" ")[1])

                        total = 0
                        for n in final:
                                if n=="No" or n=="Small" or n=="Large":
                                        continue
                                else:
                                        total = total + w2n.word_to_num(n)
                        
                        print("Number of faces detected in CA Logs: " + str(total))  
                        timeout = 0
                        while (not os.path.exists(performanceLogFile) and timeout<=60):
                                time.sleep(1)
                                timeout+=1
                        with open(performanceLogFile) as p:
                                p = p.readlines()
                        print("Printing performance number for the video :" + str(p))
                        timeTaken = p[0].replace("Total time: ","")
                        timeTaken = timeTaken.replace("\n","")
                takeshot(technology, total, timeTaken)
                time.sleep(2)

def takeshot(technology, total, timeTaken):
        screenshotdir = userdir + "/Desktop/FD_Automation/ScreenshotSamples/" + technology + "/" + mode + "/TensedFaces/"
        if not os.path.exists(screenshotdir):
                os.makedirs(screenshotdir)
        
        screenshotName = screenshotdir + "Screenshot_" + technology + "_" + name[:name.find("_")] + "_" + str(total) + "_" + str(timeTaken) + ".jpg"

        pyautogui.screenshot(screenshotName)

        timeout=0
        while (not os.path.exists(screenshotName) and timeout<=60):
                        time.sleep(1)
                        timeout+=1
        if os.path.exists(screenshotName):
                print("Successfully saved screenshot under: " + screenshotName)
        else:
                print("Screenshot not saved!!")
if __name__=="__main__":
        main()