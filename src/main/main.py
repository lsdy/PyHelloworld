#!/usr/bin/env python
#coding=utf-8
'''
Created on 2018年2月23日

@author: jacket
'''

import sys
from src.step1 import hello

def main():
    #修改路径
    all_argv=sys.argv
    # print(all_argv)
    if len(all_argv) < 3 :
        print 'Argments Input Wrong!'
        sys.exit(1)
    
    destPath=sys.argv[1]
    # print(destPath)
    
    srcFile=sys.argv[2]
    
    srcFile=hello.getAbsFilePath(srcFile)
#     print(srcFile)
    
    comment=hello.openFile(srcFile)
#     print comment #我确定输入比如：./Comment也可以打开对应文件
    hello.modifyFileRecursion(destPath,srcFile,comment)
    
    sys.exit(0)
    
if __name__=='__main__':
    main()

