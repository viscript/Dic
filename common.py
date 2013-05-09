#!/user/bin/python
#coding:utf-8

import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

class comPara:

    pwd = os.getcwd();
    osName = os.name;
    configName = "ReWord.conf";
    wordName = ["localWord",".txt"];

    def __init__(self):
        pass;

    def clearScreen(self):
        if self.osName == "posix":
            os.system("clear");
        else:
            os.system("cls");

    def backslash(self):
        backslash = ""
        if self.osName == "posix":
            backslash = '/';
        else:
            backslash = "\\";
        return backslash;
