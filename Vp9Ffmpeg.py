import os
import subprocess

os.system("echo hello world")
fileList = os.listdir()
for i in fileList:
    print([i])
    n = i.split(".")
    print(n[0])
    print(subprocess.run("ffmpeg -i %s -c:v libvpx-vp9 -b:v 0 -crf 30 -pass 1 -threads 8 -row-mt 1 -an -f null NUL && ^"
                         "ffmpeg -i %s -c:v libvpx-vp9 -b:v 0 -crf 30 -pass 2 -threads 8 -row-mt 1 -c:a libopus %s_vp9.webm" % (i, i, n[0]), shell=True))
input()
