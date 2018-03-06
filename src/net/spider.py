#!/usr/bin/env python
#coding=utf-8
'''
Created on 2018年3月5日

@author: jacket
'''
import urllib2
import sys

type=sys.getfilesystemencoding()
url="http://www.shenpinwu.com/7/7311/"

response=urllib2.urlopen(url)
html=response.read()
htmlWithutf8=html.decode("gbk").encode(type)

print htmlWithutf8