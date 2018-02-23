#!/usr/bin/env python
# coding=utf-8
'''
Created on 2018年2月8日

@author: jacket
'''
import os
import re

CppSuffixList=['cpp','c','cc','hpp','h']

#file type
FILE=1
DIR=0
UNKOWN=-1

#获得文件的决定路径
def getAbsFilePath(inFilePath):
    return os.path.abspath(inFilePath)


def openFile(filename):
    f=open(filename,'r')
    fCon=f.read()
#     print(fCon)
    f.close()
    return fCon

#判断是否以及存在注释
def isContainCommentForCPP(fileText):
#     print re.match(r"\s*/\*[\w\W]*?\*/",fileText).span()
#     print re.match(r'\s*(//.*\s*)*', fileText).span()
    return (re.match(r"\s*/\*[\w\W]*?\*/",fileText)!=None) \
        or(re.match(r'\s*(//.*\s*)*', fileText)!=None);

#判断是否为Cpp的文件0     
def isCppFile(filename):
    for suffix in CppSuffixList:
        if(filename.endswith('.'+suffix)):
            return True
    return False

#修改CPP或C类型的注释
def modifyCPPFile(filename,comment):
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



def modifyFileRecursion(destPath,srcFile,comment):
    all_file = os.listdir(destPath)
    # print(all_file)
    for each_file in all_file:
        #忽略.*的文件或目录下的所有文件
        if(each_file.startswith('.')):
            continue
        
        OneDir=destPath+each_file;
        
        filetype=fileType(OneDir)
        
        
        if filetype==FILE:
            if srcFile!=OneDir:
                print OneDir
                if isCppFile(OneDir):
                    print 'Modify '+OneDir
                    modifyCPPFile(OneDir,comment)
        elif filetype==DIR:
            modifyFileRecursion(OneDir+'/',srcFile,comment)
            
            
