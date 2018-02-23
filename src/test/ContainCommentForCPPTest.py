#!/usr/bin/env python
#coding=utf-8
'''
Created on 2018年2月23日

@author: jacket
'''


import unittest
from src.tools.hello import isContainCommentForCPP,openFile

fileText=openFile("/home/jacket/Server/src/main.cpp")
# print fileText

class Test(unittest.TestCase):
    def test_case1(self):
        print isContainCommentForCPP(fileText)
    
        
if __name__=='__main__':
    unittest.main()