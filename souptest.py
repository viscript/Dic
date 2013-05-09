#!/usr/bin/python
#coding=utf-8

"""
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
title:mini YouDao
author:HankZhou
mail:z15804268950@icloud.com
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib2
import re
import sys
import os
from common import comPara



"""
-----------------------------------
get the contents of the url
-----------------------------------
"""

def getHtml(htmlurl):
    page = urlopen(urllib2.Request(htmlurl),timeout=10)
    content = page.read()
    page.close()
    return content



"""
----------------------------------
put translations to array
----------------------------------
"""

def getDiv(content):
    soup = BeautifulSoup(content)
    getContent = soup.find('div',id='doc').find('div',id='scontainer').find('div',id='container').find('div',id='results').find('div',id='results-contents').find('div',id='phrsListTab').find('div',class_='trans-container').ul.strings
    for i in getContent:
        yield i



"""
----------------------------------
print the translation
----------------------------------
"""

def prTrans(arrTrans):
    for i in arrTrans:
        if i.strip()!= "":
            print(i)



"""
----------------------------------
set url 
----------------------------------
"""

def urlset(word):
    htmlurl="http://dict.youdao.com/search?le=eng&q=" + word + "&keyfrom=dict.index"
    return htmlurl



"""
*********************************
main function
*********************************
"""

def accurate():

    pa = comPara();
    pa.clearScreen();
    word = raw_input("查询:");
    htmlurl = urlset(word);
    content = getHtml(htmlurl);
    arrTrans = getDiv(content);
    sys.stdout.write("-"*30 + "\n\r");
    prTrans(arrTrans);
    sys.stdout.write("-"*30 + "\n\r");
    raw_input ();
