import os
import sys
from os import listdir
from os import chdir
import gzip
import magic
import codecs
from  subprocess32 import call
from subprocess32 import check_output

import re
import time
from HTMLParser import HTMLParser

def clearCache(cachedir):
    command = "rm -rf " + cachedir
    result = call(command, shell=True)
    time.sleep(1)

def firefox(url):
    command = "firefox " + url + " &"
    os.system(command)
    time.sleep(20)
    command = "pkill firefox -f"
    os.system(command)

def readCache(cachedir):
    files = listdir(cachedir)
    filelist = []
    for file in files:
        if "gzip" in magic.from_file(cachedir + file):
            command = "mv " + cachedir + file + " " + cachedir + file + ".gz"
            result = call(command, shell=True)
            command = "gunzip " + cachedir + file + ".gz"
            result = call(command, shell=True)
            filelist.append(cachedir + file)

    return filelist



def getData(cachedir,url):
    flag = False

    clearCache(cachedir)
    firefox(url)

    files = readCache(cachedir)

    for file in files:
        print file
        #
        # Insert code to parse through files here
        #


