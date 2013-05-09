#!/user/bin/python
#coding:utf-8

import os
import sys
from common import comPara

reload(sys)
sys.setdefaultencoding('utf-8')



pa = comPara();
pwd = pa.pwd;
osName = pa.osName;
configName = pa.configName;
wordName = pa.wordName;


#同步单词函数
def localWordMain(localWord):

    backslash = pa.backslash();
    out="";
    fileName = wordName[0] + wordName[1]
    if os.path.isfile(fileName):
        os.remove(fileName);
    fp =open(fileName,"w") 
    for i in range(len(localWord)):
        for m in localWord[i]:
            m = m.replace("\r","");
            m = m.replace("\n","");
            out += m + "#";
        out = out.rstrip('#')
        out += "\n";
    
    fp.write(out)
    fp.close()
    sys.stdout.write("单词同步成功。\n\r");

#打印单词
def openLocalWordMain():
   
    import re    

    wordList = localArray();
    for index,item in enumerate(wordList):
        sys.stdout.write("<" + str(index + 1) + "> ");
        sys.stdout.write("" + item[0] + " \n\r");
        if item[1]:
            sys.stdout.write("音标: " + item[1] + " \n\r");
        sys.stdout.write("" + item[2] + " \n\r");
        sys.stdout.write("\n\r");
#打开本地单词本并以列表返回
def localArray():
    fileName = wordName[0] + wordName[1];
    if not os.path.isfile(fileName):
        return False;
    fp = open(fileName,"r").readlines();
    wordList=[]
    for index,item in enumerate(fp):
        item = item.strip('\n');
        item = item.replace(' ','');
        wordList.append(item.split("#"));
    return wordList;
