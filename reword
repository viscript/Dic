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

def screenMenu():
    menuDict = [''];
    menuDict.append("Local Word [查看本地单词本]");
    menuDict.append("Recite Word [背单词]");
    menuDict.append("Accurate Translation [精确翻译]");
    menuDict.append("SYNCYouDao[同步有道单词本]");
    menuDict.append("Exit [退出]");
    count = 1;
    for index,item in enumerate(menuDict):
        if index == 0:continue;
        sys.stdout.write("[" + str(index) + "] " + item + "\n\r");

def welcome():

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
         
    from  operationYoudao import operationYoudaoMain
     
    switchId = raw_input("->>");
    swithcMenuSwitch = {
        '1':lambda:sys.stdout.write("1"),
        '2':lambda:sys.stdout.write("2"),
        '3':lambda:sys.stdout.write("3"),
        '4':lambda:operationYoudaoMain(),
        '5':lambda:exitReWord()
        };
    if not switchId in swithcMenuSwitch.keys():
        sys.stdout.write("错误，请输入菜单序号！\n\r");
        return switchMenu(); 
    swithcMenuSwitch[switchId]();
    return True;

    
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
    os.system("clear");
    (opts,args) = main();
    lens = len(args);
    if len(args) > 0 and checkArgs(lens,args):
        transMain(args[0]); 
    elif lens == 0:
        welcome();
        screenMenu();
        while 1:
            IsOK = switchMenu();
            if IsOK:sys.stdout.write("测试结束。\n\r");
