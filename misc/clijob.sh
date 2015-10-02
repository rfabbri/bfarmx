#!/bin/sh

myblender="blender -b -noaudio"
nohup $myblender prj.blend -o /home/rfabbri/ -P  -F PNG -x 1 clijob.py&
