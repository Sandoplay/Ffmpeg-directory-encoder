import os
import pathlib
import subprocess
from os import path

startPath = pathlib.Path().resolve()
print(startPath)
os.system("echo hello world")
fileList = os.listdir()
finalPath = path.join('Converted_Videos')
conVidPath = str(startPath) + "\\" + finalPath + "\\"
print(conVidPath)
if not os.path.isdir(finalPath):
    os.makedirs(finalPath)
for i in fileList:
    filext = os.path.splitext(i)[1]
    if (filext == '.mp4') or filext == '.mov' or filext == '.MOV':
        n = i.split(".")
        # print(n[0])
        print(subprocess.run(
            "ffmpeg -i %s -c:v libvpx-vp9 -b:v 0 -crf 30 -pass 1 -threads 12 -row-mt 1 -an -f null NUL && ^"
            "ffmpeg -i %s -c:v libvpx-vp9 -b:v 0 -crf 30 -pass 2 -threads 12 -row-mt 1 -c:a libopus %s%s_vp9.webm" % (
                i, i, conVidPath, n[0]), shell=True))
input()
