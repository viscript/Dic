#!/usr/bin/python
#coding=utf-8

import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


"""
================================================================================
"""


def cmdPr(explain):
	trans=""
	print("音标: [ %s ]" % explain['basic']['phonetic'])
	for i in explain['basic']['explains']:
		print(i)

def key():
	key = '258070906'
	keyfrom = 'commandtranslation'
	keyArray = [ key , keyfrom ]
	return keyArray

def getExplain(word):
	keyArray = key()
        url='http://fanyi.youdao.com/openapi.do?keyfrom=' + keyArray[1] + \
        	'&key=' + keyArray[0] + '&type=data&doctype=json&version' \
        	+ '=1.1&q=' + word
        transJson = requests.get(url).text
	explain = json.loads(transJson)
	return explain
	
def transMain(word):
	explain = getExplain(word)
	cmdPr(explain)

