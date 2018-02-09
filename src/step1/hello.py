#!/usr/bin/python
# coding=utf-8
'''
Created on 2018年2月8日

@author: jacket
'''
import os
import sys

#file type
FILE=1
DIR=0
UNKOWN=-1

def openFile(filename):
    f=open(filename,'r')
    fCon=f.read()
#     print(fCon)
    f.close()
    return fCon


def modifyFile(filename,comment):
#     print(filename)
    current_file_content=openFile(filename)
    new_file_content=comment+current_file_content
    f=open(filename,'w')
    f.write(new_file_content)
    
def fileType(filepath):
    if os.path.isdir(filepath):
        return DIR
    elif os.path.isfile(filepath):
        return FILE
    else:
        print('Unkown file :'+filepath)
        return UNKOWN

def modifyFileRecursion(destPath):
    all_file = os.listdir(destPath)
    # print(all_file)
    for each_file in all_file:
        #由是否进位决定是否还在for循环内
    #     print(destPath+each_file)
    #     print(srcFile)
        OneDir=destPath+each_file;
        
        filetype=fileType(OneDir)
        if filetype==FILE:
            if srcFile!=OneDir:
                print 'Modify '+destPath+each_file
                modifyFile(destPath+each_file,comment)
        elif filetype==DIR:
            modifyFileRecursion(OneDir+'/')
            
#修改路径
all_argv=sys.argv
# print(all_argv)
if len(all_argv) < 3 :
    print 'Argments Input Wrong!'
    exit(1)

destPath=sys.argv[1]
# print(destPath)
srcFile=sys.argv[2]
# print(srcFile)

comment=openFile(srcFile)

modifyFileRecursion(destPath)

exit(0)