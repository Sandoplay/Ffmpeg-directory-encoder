import os
import shutil
import pathlib
import subprocess
from os import path

startPath = pathlib.Path().resolve()
print(startPath)
#os.system("echo hello world")
fileList = os.listdir()
finalPath = path.join('Converted_Videos')
origVidPath = path.join('Original_Videos_Converted')
conVidPath = str(startPath) + "\\" + finalPath + "\\"
startPath = str(startPath)
print(conVidPath)
if not os.path.isdir(finalPath):
    os.makedirs(finalPath)
if not os.path.isdir(origVidPath):
    os.makedirs((origVidPath))
for i in fileList:
    fileext = os.path.splitext(i)[1]
    if (fileext == '.mp4') or fileext == '.mov' or fileext == '.MOV':
        oldName = i
        n = i.split(".")
        newName = i.replace(" ", "")
        os.rename(startPath+"\\"+oldName, startPath+"\\"+newName)
        # print(n[0])
        print(subprocess.run(
            "ffmpeg -i %s -c:v libvpx-vp9 -b:v 0 -crf 30 -pass 1 -threads 12 -row-mt 1 -an -f null NUL && ^"
            "ffmpeg -i %s -c:v libvpx-vp9 -b:v 0 -crf 30 -pass 2 -threads 12 -row-mt 1 -c:a libopus %s%s_vp9.mp4" % (
                i, i, conVidPath, n[0]), shell=False))
        shutil.move(str(startPath) + "\\" + newName, str(startPath) + "\\" + origVidPath + "\\" + newName)
input()
