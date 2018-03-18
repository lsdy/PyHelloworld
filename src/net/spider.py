#!/usr/bin/env python
#coding=utf-8
'''
Created on 2018年3月5日

@author: jacket
'''
import urllib2
import urllib
import sys
from bs4 import BeautifulSoup
import bs4
from platform import node


def recurse(node):
    a=type(node)
#     print a
    if a==bs4.element.Tag:
#         print node.name
        for child in node:
            recurse(child)
    elif a==bs4.element.NavigableString:
#         print node.parent.attr
#         print node.string
        pass
       
        

                
def main():
    # type=sys.getfilesystemencoding()
    # print type #在windows下编码有问题，不对其进行编码了
    url="http://www.shenpinwu.com/7/7311/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}
#     values = {'username' : 'cqc',  'password' : 'XXXX' }
#     data = urllib.urlencode(values) 
#     print data
    data=None
    request=urllib2.Request(url,data,headers)
    response=urllib2.urlopen(request)
    html=response.read()
#     print html
    soup=BeautifulSoup(html,"lxml")
    
#     print soup.prettify()
    div=soup.find('div', class_='article_texttitleb')
    print div
    # print type(soup.html.meta) #<class 'bs4.element.Tag'>获得其在python的类型
    # print soup.html.name.name #如果xml有个标记<name></name>那会发生不能找到该节点的错误，因为已经被Tag的name属性占用
#     print soup #bs4已经完成转码了
#     print soup.html.center
#     print soup.html.head.meta.attrs
    start=soup.html.body.center
#     print type(start)
    for child in start:
#         print child
#         print "==========================================="
        recurse(child)
     
    
if __name__=='__main__':
    main()