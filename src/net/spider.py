#!/usr/bin/env python
#coding=utf-8
'''
Created on 2018年3月5日

@author: jacket
'''
import urllib2
import sys
from bs4 import BeautifulSoup


def main():
    # type=sys.getfilesystemencoding()
    # print type #在windows下编码有问题，不对其进行编码了
    url="http://www.shenpinwu.com/7/7311/"
    
    response=urllib2.urlopen(url)
    html=response.read()
#     print html
    soup=BeautifulSoup(html,"lxml")
    
    
    # print type(soup.html.meta) #<class 'bs4.element.Tag'>获得其在python的类型
    # print soup.html.name.name #如果xml有个标记<name></name>那会发生不能找到该节点的错误，因为已经被Tag的name属性占用
#     print soup #bs4已经完成转码了
    print soup.html.head.meta
    print soup.html.head.meta.attrs
    
if __name__=='__main__':
    main()