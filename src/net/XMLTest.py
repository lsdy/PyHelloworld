#/usr/bin/env python
#coding=utf-8
'''
Created on 2018年3月7日

@author: admin01
'''
import unittest
from bs4 import BeautifulSoup
import spider


# xml='<meta http-equiv="Content-Type" content="text/html; charset=gbk"/>'
xml="<html/>"

class Test(unittest.TestCase):



    def setUp(self):
        pass


    def tearDown(self):
        pass


#     def test1(self):
#         print xml
#         
#     def test2(self):
#         decodeXml=xml.decode("gbk")
#         print decodeXml
#     
#     def test3(self):
#         soup=BeautifulSoup(xml,"lxml")
#         print soup
#         pass
    def test4(self):
        print 'Test 4'
#         testdiv='<div class="nav">'
        testdiv='''
        <div class="nav_1">
        <a>
        <p></p>
        </a>
        </div>
        '''
        node=BeautifulSoup(testdiv,'lxml')
        print node.prettify()
        result=spider.isContainChild(node.html.body.div)
        print result
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()