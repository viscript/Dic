#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import urllib2,cookielib,re,urllib,optparse

"""
FUNCTION	:Login youdao Dictionary
VERSION		:0.9v
DATE		:2013-4-25 17:43:25
AUTHOR		:HankZhou
"""

################################################################################

# print 80 "="s

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
     pe();
     for index, cookie in enumerate(cookieJar):
         print '[',index, ']',cookie;

# login youdao
def loginYoudao(deBug):
     pe();
     cj = cookielib.CookieJar();
     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
     urllib2.install_opener(opener);
     resp = urllib2.urlopen("http://account.youdao.com/login?back_url=http://" \
          "dict.youdao.com/wordbook/wordlist?keyfrom=dict.entry"); 

     """
     cookie Debug
     """
     if deBug == 1 :prCookie(cj);

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
     if deBug == 1 :prCookie(cj); 

     pattern = re.compile(r'http://reg.youdao.com/next.jsp[a-zA-Z%?&=_.0-9]*');
     getSearch = re.search(pattern,resp.read());
     resp = urllib2.urlopen(getSearch.group(0));
     checkBack = loginCheck(cj);
     if checkBack :
         print("Login success!");
         return True;
     else:
         print("Login failure");
         return Flase;

# main
if __name__ == "__main__":
    loginback = loginYoudao(0);
    pe(20);
