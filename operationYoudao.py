#!/usr/bin/python2.7
#coding:utf-8

import urllib2,cookielib,re,urllib,optparse
import cookielib
import re
import urllib
import optparse

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from wordData import mainWordData
from localWord import localWordMain

"""
FUNCTION	:Login youdao Dictionary
VERSION		:0.9v
DATE		:2013-4-25 17:43:25
AUTHOR		:HankZhou
"""

################################################################################

# print 80 "="s

def getPageNums(content):

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(content);
    getContent = soup.find('div',id="wrapper").find('div',id="listmode"). \
        find('div',id="wordfoot").find('div',id="pagination").findAll('a' \
        ,attrs = {'href':re.compile('.*')});
    lens = len(getContent) - 2;
    wordList=["wordlist?p=0&tags="]
    for i in xrange(lens):
        wordList.append(getContent[i]['href']);
    return wordList;

def getWordNums(content):

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(content);
    getWordNums = soup.find('div',id="wrapper").find('div',id="listmode") \
        .find('div',attrs={"class":"right"}).findAll('strong')[1].string
    pageNums = 15
    pages = int(getWordNums)/pageNums + 1
    lastPageNums = int(getWordNums)%pageNums

    return pageNums,pages,lastPageNums


def getPageWord(content,pageNums=15):
    
    from bs4 import BeautifulSoup
 
    getWord = []
    soup = BeautifulSoup(content);
    getContent = soup.find('div',id="wrapper").find('div',id="listmode"). \
        find('div',id="wordlist").find('table').find('tbody')
    for i in xrange(pageNums):
        word0 = getContent.findAll('tr')[i].findAll('td')  \
                [1].find('div')['title'];
        word1 = getContent.findAll('tr')[i].findAll('td')  \
                [2].find('div')['title'];
        word2 = getContent.findAll('tr')[i].findAll('td')  \
                [3].find('div')['title'];
        word3 = getContent.findAll('tr')[i].findAll('td')  \
                [4].string;
        word4 = getContent.findAll('tr')[i].findAll('td')  \
                [5].find('div')['title'];
        getWordCon = [word0,word1,word2,word3,word4];
        getWord.append(getWordCon);
        getWordCon = [];
    return getWord     


def pe(quantity=80):
    print("="*quantity)

# Check  successfully logged in using cookies
def loginCheck(cookieJar):
    checkCookie =['NTES_SESS','P_INFO','S_INFO','NTES_SESS', \
        'OUTFOX_SEARCH_USER_ID','P_INFO','_PREF_USER__MYTH','JSESSIONID']
    checkCookie = {};
    for eachCookieName in checkCookie:
        checkCookie[eachCookieName] = False;
    allCookieFound = True;
    for cookie in cookieJar:
        if(cookie.name in checkCookie):
            checkCookie[cookie.name] = True;
    for eachCookie in checkCookie.keys():
        if(not checkCookie[eachCookie]):
            allCookieFound = False;
            break;
    return allCookieFound;

# print cookie for debug
def prCookie(cookieJar):
    for index, cookie in enumerate(cookieJar):
        print '[',index, ']',cookie;
    pe();

# login youdao
def loginYoudao(deBug=False,sync=0):
    if deBug:
        pe(80);
    else:
        pe(20);
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    resp = urllib2.urlopen("http://account.youdao.com/login?back_url=http://" \
        "dict.youdao.com/wordbook/wordlist?keyfrom=dict.entry"); 

    """
    cookie Debug
    """
    if deBug:prCookie(cj);

    youdaoLoginUrl = "https://reg.163.com/logins.jsp";
    postDict = {
        "url":"http://account.youdao.com/login?back_url=http%3A%2F%2Fdict.youda" \
            "o.com%2Fwordbook%2Fwordlist%3Fkeyfrom%3Ddict.entry&success=1",
        "product":"search",
        "type":"1",
        "username":"15804268950@163.com",
        "password":"2828469"  
    };
    postData = urllib.urlencode(postDict);
    requestHeaders = {
        "Referer":"http://account.youdao.com/login?back_url=http://dict.youdao.c" \
            "om/wordbook/wordlist?keyfrom=dict.entry",
        "User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.31 (KHTML, li" \
            "ke Gecko) Chrome/26.0.1410.64 Safari/537.31"
    };
    req = urllib2.Request(youdaoLoginUrl,postData,requestHeaders);
    resp = urllib2.urlopen(req);

    """
    cookie Debug
    """
    if deBug:prCookie(cj); 

    pattern = re.compile(r'http://reg.youdao.com/next.jsp[a-zA-Z%?&=_.0-9]*');
    getSearch = re.search(pattern,resp.read());
    resp = urllib2.urlopen(getSearch.group(0));
    checkBack = loginCheck(cj);
    if checkBack :
        print("Login success!");
        if sync != 1:return True;
    else:
        print("Login failure");
        return False;
    if sync != 1:return False;



    """
    [syncYoudao]
    """

    wordList = getPageNums(resp.read());
    baseUrl = urllib2.urlopen("http://dict.youdao.com/wordbook/" + wordList[0]);
    pageNums,pages,lastPageNums = getWordNums(baseUrl)
    if deBug:print pageNums,pages,lastPageNums;
    allGetWord = [];
    for index,item in enumerate(wordList):
        nowUrl = "http://dict.youdao.com/wordbook/" + \
            wordList[index]
        nowUrlrq = urllib2.urlopen(nowUrl)
        nowUrlread = nowUrlrq.read();
        if index < (pages - 1):
            getWord = getPageWord(nowUrlread);
        elif index == (pages - 1):
            getWord = getPageWord(nowUrlread,pageNums=lastPageNums);
        else:
            if deBug:print "Than expected error in word";
            getWord == False;
            break;
        if getWord:
            allGetWord += getWord 
    if len(allGetWord) == pageNums*(pages - 1) + lastPageNums:
        localWordMain(allGetWord);

def operationYoudaoMain():
    loginback = loginYoudao(deBug=False,sync=1);
    pe(20);
#    if loginback != False:
#        mainWordData(loginback);
