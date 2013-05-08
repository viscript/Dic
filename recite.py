#!/user/bin/python
#coding:utf-8

import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#调用localword打开本地单词本函数
def prepareRecite():
    
    from localWord import localArray

    wordList = localArray();
    return wordList;

#看汉语背英语单词
def reciteC2E():


    wordList = prepareRecite();
    sys.stdout.write("开始背单词(看汉语背英语)");
    raw_input ();
    length = len(wordList);
    for index,item in enumerate(wordList):
        reciteC2EOne(item,index,length);

def reciteC2EOne(word,index,length):

    os.system('clear');
    sys.stdout.write("-"*25 + str(index + 1) + "/" + str(length) + "\n\r");
    sys.stdout.write(word[2] + "\n\r");
    sys.stdout.write("- "*15 + "\n\r");
    wordRe = raw_input();
    if wordRe == word[0]:
        sys.stdout.write(" √ \n\r");
    else:
        sys.stdout.write(" ×  \n\r");
        sys.stdout.write(wordRe + " -> " + word[0] + "\n\r");
    sys.stdout.write("-"*30 + "\n\r");
    raw_input ();   


