#coding:utf-8
#iterateDir.py
import os
import os.path
import codecs

from chardet.universaldetector import UniversalDetector

rootdir=os.getcwd()

for fdir,cdir,filenames in os.walk(rootdir):
    print "dir:",fdir
    for filename in filenames:
        if os.path.splitext(filename)[1] == '.py':        
            fp = open(fdir+"\\"+filename,'r')
            detector = UniversalDetector()
            for line in fp.readlines():
                detector.feed(line)
                if detector.done : break
            detector.close()
            fp.close()
            print "filename:",filename
            print "encoding:",detector.result['encoding']


raw_input("Please enter")
