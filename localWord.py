#!/user/bin/python
#coding:utf-8

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def getPara():
    pwd = os.getcwd();
    osName = os.name;
    configName = "ReWord.conf"
    wordName = ["localWord",".txt"]
    return pwd,osName,configName,wordName; 


def localWordMain(localWord):

    pwd,osName,configName,wordName = getPara();
    if osName == "posix":
        s = '/';
    else:
        s = "\\";
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
    
def localArray():
    pwd,osName,configName,wordName = getPara();
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
