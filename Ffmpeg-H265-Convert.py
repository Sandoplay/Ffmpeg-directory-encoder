import os
import shutil
import pathlib
import subprocess
from os import path

startPath = pathlib.Path().resolve()
print(startPath)
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
    if ((fileext == '.mp4') or fileext == '.mkv' or fileext == '.MOV' or fileext == '.webm' or fileext == '.MP4'
            or fileext == '.m4v'):
        oldName = i
        n= i.rsplit(".", 1)
        newName = i.replace(" ", "_")
        os.rename(startPath+"\\"+oldName, startPath+"\\"+newName)
        # print(n[0])
        print(subprocess.run(
            #"ffmpeg -i %s -c:v libx265 -crf 28 -preset medium -color_primaries 1 -color_trc 1 -colorspace 1 -movflags +write_colr -c:a aac -b:a 128k %s%s_vp9.mp4"
            #"ffmpeg -y -i \"%s\" -c:v libx265 -crf 30 -preset medium -map 0 -map_metadata 0 -color_primaries 1 -color_trc 1 -colorspace 1 -movflags +write_colr -pass 1 -r 30 -an -f null NUL && ^"
            "ffmpeg -i \"%s\" -c:v libx265 -crf 30 -preset fast -map 0:v -map 0:a:0 -map_metadata 0 -color_primaries 1 -color_trc 1 -colorspace 1 -movflags +write_colr -c:a aac -b:a 96k -r 30 \"%s%s%s_h265.mp4\""% (
                newName, conVidPath, n[0], n[-1]), shell=True))
        shutil.move(str(startPath) + "\\" + newName, str(startPath) + "\\" + origVidPath + "\\" + newName)
input()
