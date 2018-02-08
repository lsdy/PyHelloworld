#!/usr/bin/python
# coding=utf-8
'''
Created on 2018年2月8日

@author: jacket
'''
import os

def openFile(filename):
    f=open(filename,'r')
    print(f.read())
    f.close()

def modifyFile(filename):
    print(filename)
    openFile(filename)
    

all_file = os.listdir('./')

print(all_file)

for each_file in all_file:
    #由是否进位决定是否还在for循环内
    modifyFile(each_file)
