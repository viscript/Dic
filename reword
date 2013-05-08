#!/usr/bin/python2.7
#coding:utf-8

import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
from trans import transMain


"""
================================================================================
"""

def screenClear():
    os.system("clear");    


def screenMenu():
    welcome();
    sys.stdout.write("* 您的位置在 [ 首页 ] \n\r \n\r")
    menuDict = [];
    menuDict.append("MyWords [本地单词本]");
    menuDict.append("Recite Word [背单词]");
    menuDict.append("Accurate Translation [精确翻译]");
    menuDict.append("Exit Reword [退出]");
    for index,item in enumerate(menuDict):
        sys.stdout.write("[" + str(index+1) + "] " + item + "\n\r");
    switchMenu();
    

def screenMyWords():
    welcome();
    sys.stdout.write("* 您的位置在 [ 首页 ] -> [ 本地单词本 ] \n\r \n\r");
    menuMyWords = []
    menuMyWords.append("List word [显示单词]");
    menuMyWords.append("SYNCYouDao[与有道单词本同步]");
    menuMyWords.append("Back [返回主菜单]");
    menuMyWords.append("Exit ReWord [退出ReWord]");
    for index,item in enumerate(menuMyWords):
        sys.stdout.write("[" + str(index+1) + "] " + item + "\n\r");  
    switchMyWords();

def screenListWord():

    from  localWord import openLocalWordMain

    welcome();
    sys.stdout.write("* 您的位置在 [ 首页 ] -> [ 本地单词本 ] -> [ 显示单词 ] \n\r \n\r");
    
    openLocalWordMain()
    menuWordList = [];
    menuWordList.append("[要删除单词的序号]");
    menuWordList.append("Back [返回主菜单]");
    menuWordList.append("Exit ReWord [退出ReWord]");
    for index,item in enumerate(menuWordList):
        sys.stdout.write("[" + str(index+1) + "] " + item + "\n\r");
    switchListWord();

def welcome():

    screenClear();
    softName = "ReWord";
    softVersion = "V0.9";
    author = "HankZhou";

    w1 = "*";
    w2 = " ";
    content = softVersion + w2*2 + author;
    enter = "\n\r";
    l = 60;
    l2 = (l - len(content) - 2)/4;
    l3 = (l - len(softName) -2)/2;
    sys.stdout.write(w1*l + enter);
    sys.stdout.write(w1 + w2*l3 + softName + w2*l3 + w1 + enter);
    sys.stdout.write(w1 + w2*l2*3 + content + w2*l2 + w1 + enter);
    sys.stdout.write(w1*l + enter);

def options():

    from optparse import OptionParser

    MSG_USAGE = "reword [-d] [-r] [-s] [word] [+] [-h]"
    options = OptionParser(MSG_USAGE)
    options.add_option("-d" , "--debug" , action = "store_true" , \
         dest = "debug" , default = False , help = "turn on the model of debug")
    return options

def main():
    opt = options();
    (opts,args) = opt.parse_args();
    return opts,args 
    
def checkArgs(lens,argsArray):

    import re

    error = 0;
    word = 0;
    plus = 0;
    if lens >= 1:
        wordPattern = re.compile(r'[a-zA-Z]+');
        match = wordPattern.match(argsArray[0]);

        if match:
            error =1
        else:
            print("The word is not legitimate!Error:10001")
        if  lens ==2 and argsArray[1] != "+":
            error = 0;
    return error
    
def switchMenu():
        
    from recite  import reciteC2E
    from souptest import accurate
 
    switchId = raw_input("->>");
    swithcMenuSwitch = {
        '1':lambda:screenMyWords(),
        '2':lambda:reciteC2E(),
        '3':lambda:accurate(),
        '4':lambda:exitReWord()
        };
    if not switchId in swithcMenuSwitch.keys():
        sys.stdout.write("错误，请输入菜单序号！\n\r");
        return switchMenu(); 
    swithcMenuSwitch[switchId]();
    return screenMenu();

def switchMyWords():

    from  operationYoudao import operationYoudaoMain
    from  localWord import openLocalWordMain

    switchMyWordsId = raw_input("|->>");
    switchMyWordsSwitch = {
        '1':lambda:screenListWord(),           #penLocalWordMain(),
        '2':lambda:operationYoudaoMain(),
        '3':lambda:screenMenu(),
        '4':lambda:exitReWord()
        };
    if not switchMyWordsId in switchMyWordsSwitch.keys():
        sys.stdout.write("错误，请输入菜单序号！\n\r");
        return switchMyWords();
    switchMyWordsSwitch[switchMyWordsId]();
    return screenMyWords();

def switchListWord():
    
    switchListWordId = raw_input("||->>");
    switchListWordSwitch = {
        '1':lambda:sys.stdout.write("1"),
        '2':lambda:screenMenu(),
        '3':lambda:exitReWord()
        };
    if not switchListWordId in switchListWordSwitch.keys():
        sys.stdout.wtrite("错误，请输入菜单序号！\n\r");
        return switchListWord();
    switchListWordSwitch[switchListWordId]();
    return screenListWord();





"""
reform
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

def exitReWord():
    sys.stdout.write("退出中...\n\r")
    exit(1);

"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

if __name__ == "__main__":
    (opts,args) = main();
    lens = len(args);
    if len(args) > 0 and checkArgs(lens,args):
        transMain(args[0]); 
    elif lens == 0:
        screenMenu();
