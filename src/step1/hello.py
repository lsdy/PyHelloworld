#!/usr/bin/python
# coding=utf-8
'''
Created on 2018年2月8日

@author: jacket
'''
import os
import sys

def openFile(filename):
    f=open(filename,'r')
    fCon=f.read()
    print(fCon)
    f.close()
    return fCon

def modifyFile(filename):
    print(filename)
    openFile(filename)
    
#修改路径
destPath=sys.argv[1]
print(destPath)
srcFile=sys.argv[2]
print(srcFile)

all_file = os.listdir('./')

print(all_file)

for each_file in all_file:
    #由是否进位决定是否还在for循环内
    modifyFile(each_file)
