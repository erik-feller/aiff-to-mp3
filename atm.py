###############################################################################
#
# Python script to convert a database of .aiff audio files to mp3 using the
# ffmpeg audio converter.
#
# Ver 0.0 (2015.8.8)
# Erik Feller
#
###############################################################################

import sys, os

## Find OS string. 
if sys.platform == 'linux' or sys.platform == 'linux2':
    operating_sys = 'linux'
elif sys.platform == 'darwin':
    operating_sys = 'mac'
elif sys.platform == 'win32':
    operating_sys = 'windows'
else:
    operating_sys = 'unkown'

## Read in the two directories as command line arguments
source_dir = sys.argv[1]
target_dir = sys.argv[2]

## for now assume that ffmpeg is installed and in the PATH

## now inventory the directory. this might need to be changed for performance reasons
source_list = os.listdir(source_dir)

## iterate throught the list of files in the dir and check to see if each is aiff then run it through ffmpeg

   

