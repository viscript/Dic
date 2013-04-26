#!/usr/bin/python2.7
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from trans import transMain


"""
================================================================================
"""


def options():

    from optparse import OptionParser

    MSG_USAGE = "reword [-d] [-r] [-s] [word] [+] [-h]"
    options = OptionParser(MSG_USAGE)
    options.add_option("-d" , "--debug" , action = "store_false" , \
         dest = "debug" , default = 1 , help = "turn on the model of debug")
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
        

if __name__ == "__main__":
    (opts,args) = main();
    lens = len(args);
    if len(args) > 0 and checkArgs(lens,args):
        transMain(args[0]); 
    elif lens == 0:
        pass;
